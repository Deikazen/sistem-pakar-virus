from fastapi import APIRouter, HTTPException

# Membuat instance APIRouter khusus untuk user
router = APIRouter()


@router.get("/latar")
def latar_page():
    return "Ini adalah latar belakang page"
