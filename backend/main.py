from fastapi import FastAPI

# 1. Membuat instance/objek dari FastAPI
app = FastAPI()

# 2. Membuat rute (endpoint) utama dengan metode GET
@app.get("/")
def baca_akar():
    return {"pesan": "Halo! Ini adalah API pertama Anda menggunakan FastAPI dan Uvicorn."}

# 3. Membuat rute dengan parameter dinamis
@app.get("/items/{item_id}")
def baca_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query_pencarian": q}
