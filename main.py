from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import uvicorn
from typing import Optional
from pydantic import BaseModel
import json
import os
from database import products
print(f"Total products: {len(products)}")


app = FastAPI(title="ProKart API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# COMMENT OUT OR REMOVE THIS LINE:
# app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

cart_data = {"items": [], "total": 0}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serve your ProKart HTML"""
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="Please place index.html in the root directory")

# Rest of your endpoints remain the same...
@app.get("/api/products")
async def get_products(category: str = "all"):
    if category == "all":
        return {"products": products}
    filtered = [p for p in products if p["category"] == category]
    return {"products": filtered}

@app.get("/api/categories")
async def get_categories():
    categories = list(set(p["category"] for p in products))
    return {"categories": categories}

@app.get("/api/stats")
async def get_stats():
    return {
        "products": len(products),
        "customers": 50000,
        "orders": 25000,
        "reviews": 12000
    }

@app.post("/api/cart/add")
async def add_to_cart(request: Request):
    global cart_data
    cart_data["items"].append({
        "id": len(cart_data["items"]) + 1,
        "name": "Sample Product",
        "price": 9999
    })
    cart_data["total"] += 9999
    return {"status": "added", "cart": cart_data}

@app.get("/api/cart")
async def get_cart():
    return cart_data

@app.post("/api/checkout")
async def checkout(request: Request):
    global cart_data
    cart_data = {"items": [], "total": 0}
    return {"status": "success", "message": "Order placed successfully!"}

@app.get("/api/health")
async def health_check():
    return {"status": "ProKart API is running 🚀"}

if __name__ == "__main__":
    print("🚀 ProKart Backend Starting...")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
