from fastapi import APIRouter, HTTPException

# Membuat instance APIRouter khusus untuk user
router = APIRouter()


@router.get("/artikel")
def artikel_page():
    return "Ini adalah artikel edukasi page"
