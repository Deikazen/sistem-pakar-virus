from fastapi import APIRouter, HTTPException

# Membuat instance APIRouter khusus untuk user
router = APIRouter(
    prefix="/latar",
    tags=["Latar Belakang"]
)


@router.get("/")
def latar_page():
    return "Ini adalah latar belakang page"
