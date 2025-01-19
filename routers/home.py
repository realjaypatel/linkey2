from starlette import status
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, HTTPException, Path, Request, status,Query
import json
import database
templates = Jinja2Templates(directory="templates")
import requests



router = APIRouter(
    # prefix='/',
    tags=['home']
)


@router.get('/', status_code=status.HTTP_200_OK)
async def return_home(request: Request,p: int = Query(1, alias="p"), c: str = Query("all", alias="c"),q: str = Query("None",alias="q")):
    print(c,q,p)
    items = []
    page_size = 3
    skip = (p - 1) * page_size
    limit = page_size
    if q == "None" and c == "all":
        items = list(database.db.find().skip(skip).limit(limit))
    elif (q == "None" and c != "all") or (q == "" and c != "all"):
        items = list(database.db.find(
            {"category": c}
        ).skip(skip).limit(limit))
    elif (q != "None" and c == "all"):
        items = list(database.db.find(
            {"title": {"$regex": q, "$options": "i"}}
        ).skip(skip).limit(limit))
    elif q != "None" and c != "all":
        items = list(database.db.find(
            {"category": c,
             "title": {"$regex": q, "$options": "i"}
             }
        ).skip(skip).limit(limit))

  
    
    print(items)
    for item in items:
        item["_id"] = str(item["_id"])
    return templates.TemplateResponse("home.html", {"request": request,"Data":items})


@router.get("/items/")
async def get_items(p: int = Query(1, alias="p")):

    page_size = 1
    skip = (p - 1) * page_size
    limit = page_size
    items = list(database.db.find().skip(skip).limit(limit))
    for item in items:
        item["_id"] = str(item["_id"])  # Convert ObjectId to string for JSON serialization
    return items

















