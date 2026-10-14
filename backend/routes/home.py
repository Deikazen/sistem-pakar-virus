from fastapi import APIRouter, HTTPException

# Membuat instance APIRouter khusus untuk user
router = APIRouter()


@router.get("/")
def home_page():
    return "Ini adalah home page"
