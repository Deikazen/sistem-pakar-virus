from fastapi import APIRouter
from pydantic import BaseModel
# Membuat instance APIRouter khusus untuk user
router = APIRouter(
    prefix="/gejala",
    tags=["Gejala"]
)


# untuk validasi input data
class SkriningInput(BaseModel):
    nama: str
    usia: int
    jenis_kelamin: str


@router.get("/")
def gejala_page():
    return "Ini adalah gejala page"
