from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory database for products
products = {}

class Product(BaseModel):
    id: int
    name: str
    price: float

@app.get("/products")
def get_products():
    return {"products": list(products.values())}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = products.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products")
def create_product(product: Product):
    if product.id in products:
        raise HTTPException(status_code=400, detail="Product ID already exists")
    products[product.id] = product.dict()
    return {"message": "Product created successfully"}

@app.put("/products/{product_id}")
def update_product(product_id: int, name: str = None, price: float = None):
    product = products.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if name:
        product["name"] = name
    if price is not None:
        product["price"] = price
    return {"message": "Product updated successfully"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    del products[product_id]
    return {"message": "Product deleted successfully"}
