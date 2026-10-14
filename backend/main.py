from routes import home, artikel, latar, skrining
from fastapi import FastAPI


app = FastAPI()


# route home_page
app.include_router(home.router)
app.include_router(artikel.router)
app.include_router(latar.router)
app.include_router(skrining.router)
