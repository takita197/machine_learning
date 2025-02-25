from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Olá, Mundo!"}

@app.get("/saudacao/{nome}")
def read_item(nome: str):
    return {"message": f"Olá, {nome}!"}