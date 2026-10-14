from fastapi import APIRouter, HTTPException

# Membuat instance APIRouter khusus untuk user
router = APIRouter()


@router.get("/skrining")
def skrining_page():
    return "Ini adalah skirning page"
