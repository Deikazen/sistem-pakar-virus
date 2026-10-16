from fastapi import APIRouter
from pydantic import BaseModel

# Membuat instance APIRouter khusus untuk skrining
router = APIRouter(
    prefix="/skrining",
    tags=["Skrining"]
)


# Schema untuk validasi data input
class SkriningInput(BaseModel):
    nama: str
    usia: int
    jenis_kelamin: str
    gejala: list[str]


@router.get("/")
def skrining_page():
    return {"message": "Ini adalah halaman skrining"}


@router.post("/proses")
def skrining_proses(payload: SkriningInput):
    # 1. Ambil data dari payload
    nama = payload.nama
    usia = payload.usia
    jenis_kelamin = payload.jenis_kelamin
    daftar_gejala = payload.gejala

    # logika cf disini

    return {
        "status": "success",
        "pasien": {
            "nama": nama,
            "usia": usia,
            "jenis_kelamin": jenis_kelamin
        },
        "gejala": daftar_gejala,
    }
