from routes import home, artikel, latar, skrining, gejala, lab
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# route home_page
app.include_router(home.router)
app.include_router(artikel.router)
app.include_router(latar.router)
app.include_router(skrining.router)
app.include_router(gejala.router)
app.include_router(lab.router)
