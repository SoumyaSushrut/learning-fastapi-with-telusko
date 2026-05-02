from fastapi import FastAPI
from models import Product

app = FastAPI()


@app.get("/")
def greet():
    return "Welcom bot 192006"

products=[
    Product(1,"mobile","budget mobile",99,10),
    Product(2,"Laptop","Gaming laptop",999,6)

]

@app.get("/products")
def get_all_products():
    return products
