from fastapi import FastAPI, Request, status
# from .models import Base
# from .database import engine
# from .routers import art, home, paintings
from routers import home,product,search,link
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}

app.include_router(home.router)
app.include_router(product.router)
app.include_router(search.router)
app.include_router(link.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=800,reload=True)