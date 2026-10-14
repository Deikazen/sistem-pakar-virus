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
    gejala = [
        {
            "G01": "Demam",
            "G02": "Batuk",
            "G03": "Sesak Napas",
            "G04": "Pilek",
        }
    ]

    return gejala
