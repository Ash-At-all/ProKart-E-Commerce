from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from mongo import cart_collection, user_collection, products_collection
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="ProKart API", version="5.0.0")

# ================= STATIC FILES =================
app.mount("/static", StaticFiles(directory="static"), name="static")

# ================= CORS =================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://pro-kart-e-commerce.vercel.app",
        "http://localhost:5500",   
        "http://127.0.0.1:5500", 
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================= AUTH SETUP =================
SECRET_KEY = os.getenv("SECRET_KEY") or "fallback_secret_key"
ALGORITHM = "HS256"
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME") or "admin"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_token(data: dict):
    data_copy = data.copy()
    data_copy.update({"exp": datetime.utcnow() + timedelta(hours=2)})
    return jwt.encode(data_copy, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["username"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_admin_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    username = get_current_user(credentials)
    if username != ADMIN_USERNAME:
        raise HTTPException(status_code=403, detail="Admin access only")
    return username

# ================= HOME =================
@app.get("/", response_class=HTMLResponse)
async def home():
    return FileResponse("index.html")

# ================= PRODUCTS =================
@app.get("/api/products")
async def get_products(category: str = "all"):
    if category == "all":
        prods = list(products_collection.find({}, {"_id": 0}))
    else:
        prods = list(products_collection.find({"category": category}, {"_id": 0}))
    return {"products": prods}

# ================= AUTH =================
@app.post("/api/signup")
async def signup(username: str, password: str):
    if user_collection.find_one({"username": username}):
        raise HTTPException(status_code=400, detail="User already exists")

    user_collection.insert_one({
        "username": username,
        "password": hash_password(password)
    })

    return {"status": "User created ✅"}

@app.post("/api/login")
async def login(username: str, password: str):
    user = user_collection.find_one({"username": username})

    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"username": username})

    return {"access_token": token}

# ================= CART =================
@app.post("/api/cart/add")
async def add_to_cart(product_id: int, username: str = Depends(get_current_user)):

    product = products_collection.find_one({"id": product_id}, {"_id": 0})

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    cart = cart_collection.find_one({"username": username})

    if not cart:
        cart_collection.insert_one({
            "username": username,
            "items": [product],
            "total": product["price"]
        })
    else:
        cart_collection.update_one(
            {"username": username},
            {
                "$push": {"items": product},
                "$inc": {"total": product["price"]}
            }
        )

    return {"status": "added ✅"}

@app.get("/api/cart")
async def get_cart(username: str = Depends(get_current_user)):
    cart = cart_collection.find_one({"username": username}, {"_id": 0})
    return cart if cart else {"items": [], "total": 0}

@app.delete("/api/cart/remove")
async def remove_from_cart(product_id: int, username: str = Depends(get_current_user)):

    cart = cart_collection.find_one({"username": username})

    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

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
        {"username": username},
        {"$set": {"items": new_items, "total": total}}
    )

    return {"status": "removed ✅"}

# ================= CHECKOUT =================
@app.post("/api/checkout")
async def checkout(username: str = Depends(get_current_user)):
    cart_collection.delete_one({"username": username})
    return {"status": "Order placed ✅"}

# ================= ADMIN =================
@app.get("/api/admin/stats")
async def admin_stats(username: str = Depends(get_admin_user)):
    total_products = products_collection.count_documents({})
    total_users = user_collection.count_documents({})
    total_orders = cart_collection.count_documents({})
    return {
        "products": total_products,
        "users": total_users,
        "orders": total_orders
    }

@app.get("/api/admin/products")
async def admin_get_products(username: str = Depends(get_admin_user)):
    prods = list(products_collection.find({}, {"_id": 0}))
    return {"products": prods}

@app.post("/api/admin/add-product")
async def admin_add_product(
    name: str,
    price: float,
    original: float,
    category: str,
    image: str = "",
    badge: str = "",
    rating: float = 4.0,
    reviews: int = 0,
    username: str = Depends(get_admin_user)
):
    import time
    product = {
        "id": int(time.time() * 1000) % 2147483647,
        "name": name,
        "price": price,
        "original": original,
        "category": category,
        "image": image,
        "badge": badge,
        "rating": rating,
        "reviews": reviews
    }
    products_collection.insert_one(product)
    return {"status": "Product added ✅", "product": {k: v for k, v in product.items() if k != "_id"}}

@app.delete("/api/admin/delete-product/{product_id}")
async def admin_delete_product(product_id: int, username: str = Depends(get_admin_user)):
    result = products_collection.delete_one({"id": product_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"status": "Product deleted ✅"}

@app.get("/api/admin/users")
async def admin_get_users(username: str = Depends(get_admin_user)):
    users = list(user_collection.find({}, {"_id": 0, "password": 0}))
    return {"users": users}

# ================= HEALTH =================
@app.get("/api/health")
async def health():
    return {"status": "API running 🚀"}

@app.get("/api/stats")
async def get_stats():
    total_products = products_collection.count_documents({})
    return {
        "products": total_products,
        "customers": 50000,
        "orders": 21288,
        "reviews": 18392
    }

# ================= RUN =================
if __name__ == "__main__":
    print("SECRET:", SECRET_KEY)
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
