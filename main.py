from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def greet():
    return "Welcom bot 192006"
