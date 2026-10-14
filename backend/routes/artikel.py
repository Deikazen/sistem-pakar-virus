from fastapi import APIRouter, HTTPException

# Membuat instance APIRouter khusus untuk user
router = APIRouter(
    prefix="/artikel",
    tags=["Artikel"]
)


@router.get("/")
def artikel_page():
    return "Ini adalah artikel edukasi page"
