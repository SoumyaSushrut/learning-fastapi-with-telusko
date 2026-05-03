from fastapi import FastAPI
from models import Product
from database import session

app = FastAPI()


@app.get("/")
def greet():
    return "Welcom bot 192006"


products = [
    Product(id=1, name="mobile", description="budget mobile", price=99, quantity=10),
    Product(id=6, name="Laptop", description="Gaming laptop", price=999, quantity=6),
]


@app.get("/products")
def get_all_products():
    db=session()
    db.query()
    return products


@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product

    return "product not found"


@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product


@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product added succesfully"

    return "Product was not found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return "product deleted succesfully"
        
    return "Product was not found"