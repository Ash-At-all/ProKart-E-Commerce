from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import Dict
import json
import os

from database import products

app = FastAPI(title="ProKart API", version="2.0.0")

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ USER-BASED CART (IMPORTANT)
cart_data: Dict[int, dict] = {}

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

# ---------------- CATEGORIES ----------------
@app.get("/api/categories")
async def get_categories():
    categories = list(set(p["category"] for p in products))
    return {"categories": categories}

# ---------------- STATS ----------------
@app.get("/api/stats")
async def get_stats():
    return {
        "products": len(products),
        "customers": 50000,
        "orders": 25000,
        "reviews": 12000
    }

# ---------------- ADD TO CART ----------------
@app.post("/api/cart/add")
async def add_to_cart(user_id: int, product_id: int):
    global cart_data

    # 🔍 Find product
    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        return {"error": "Product not found"}

    # 👤 Create cart for user if not exists
    if user_id not in cart_data:
        cart_data[user_id] = {"items": [], "total": 0}

    # ➕ Add product
    cart_data[user_id]["items"].append(product)

    price = product.get("price", 0)
    cart_data[user_id]["total"] += price

    return {"status": "added ✅", "cart": cart_data[user_id]}

# ---------------- GET CART ----------------
@app.get("/api/cart/{user_id}")
async def get_cart(user_id: int):
    return cart_data.get(user_id, {"items": [], "total": 0})

# ---------------- REMOVE FROM CART ----------------
@app.delete("/api/cart/remove")
async def remove_from_cart(user_id: int, product_id: int):
    if user_id not in cart_data:
        return {"error": "Cart not found"}

    cart = cart_data[user_id]
    new_items = []
    removed = False

    for item in cart["items"]:
        if item["id"] == product_id and not removed:
            cart["total"] -= item.get("price", 0)
            removed = True
            continue
        new_items.append(item)

    cart["items"] = new_items

    return {"status": "removed ✅", "cart": cart}

# ---------------- CHECKOUT ----------------
@app.post("/api/checkout")
async def checkout(user_id: int):
    global cart_data

    if user_id in cart_data:
        cart_data[user_id] = {"items": [], "total": 0}

    return {"status": "success ✅", "message": "Order placed successfully!"}

# ---------------- HEALTH ----------------
@app.get("/api/health")
async def health_check():
    return {"status": "ProKart API running 🚀"}

# ---------------- RUN ----------------
if __name__ == "__main__":
    print("🚀 ProKart Backend Starting...")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
