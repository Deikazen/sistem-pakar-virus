from fastapi import APIRouter, HTTPException

# Membuat instance APIRouter khusus untuk user
router = APIRouter(
    prefix="/lab",
    tags=["Laboratorium"]
)


@router.get("/")
def latar_page():
    return "Ini adalah laboratorium page"
