from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from database import products
from mongo import cart_collection

app = FastAPI(title="ProKart API", version="3.0.0")

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- HOME ----------------
@app.get("/", response_class=HTMLResponse)
async def read_root():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except:
        return HTMLResponse(content="index.html not found")

# ---------------- PRODUCTS ----------------
@app.get("/api/products")
async def get_products(category: str = "all"):
    if category == "all":
        return {"products": products}
    
    filtered = [p for p in products if p["category"] == category]
    return {"products": filtered}

# ---------------- ADD TO CART ----------------
@app.post("/api/cart/add")
async def add_to_cart(user_id: int, product_id: int):

    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        return {"error": "Product not found"}

    cart = cart_collection.find_one({"user_id": user_id})

    if not cart:
        cart_collection.insert_one({
            "user_id": user_id,
            "items": [product],
            "total": product["price"]
        })
    else:
        cart_collection.update_one(
            {"user_id": user_id},
            {
                "$push": {"items": product},
                "$inc": {"total": product["price"]}
            }
        )

    return {"status": "added ✅"}

# ---------------- GET CART ----------------
@app.get("/api/cart/{user_id}")
async def get_cart(user_id: int):
    cart = cart_collection.find_one({"user_id": user_id}, {"_id": 0})
    return cart if cart else {"items": [], "total": 0}

# ---------------- REMOVE FROM CART ----------------
@app.delete("/api/cart/remove")
async def remove_from_cart(user_id: int, product_id: int):

    cart = cart_collection.find_one({"user_id": user_id})

    if not cart:
        return {"error": "Cart not found"}

    items = cart.get("items", [])
    new_items = []
    removed = False
    total = cart.get("total", 0)

    for item in items:
        if item["id"] == product_id and not removed:
            total -= item.get("price", 0)
            removed = True
            continue
        new_items.append(item)

    cart_collection.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "items": new_items,
                "total": total
            }
        }
    )

    return {"status": "removed ✅"}

# ---------------- CHECKOUT ----------------
@app.post("/api/checkout")
async def checkout(user_id: int):

    cart_collection.delete_one({"user_id": user_id})

    return {"status": "success ✅", "message": "Order placed!"}

# ---------------- HEALTH ----------------
@app.get("/api/health")
async def health_check():
    return {"status": "ProKart API running 🚀"}

# ---------------- RUN ----------------
if __name__ == "__main__":
    print("🚀 ProKart Backend Starting...")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
