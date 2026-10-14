from fastapi import APIRouter
from pydantic import BaseModel
# Membuat instance APIRouter khusus untuk user
router = APIRouter(
    prefix="/skrining",
    tags=["Skrining"]
)


# untuk validasi input data
class SkriningInput(BaseModel):
    nama: str
    usia: int
    jenis_kelamin: str


@router.get("/")
def skrining_page():
    return "Ini adalah skirning page"


@router.post("/input")
def skrining_input(payload: SkriningInput):
    return {
        "nama": payload.nama,
        "usia": payload.usia,
        "jenis_kelamin": payload.jenis_kelamin,
    }
