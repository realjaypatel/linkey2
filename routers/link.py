from starlette import status
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, HTTPException, Path, Request, status, Form,FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from datetime import datetime

import json
import database
templates = Jinja2Templates(directory="templates")
import requests
import time

router = APIRouter(
    prefix='/add',
    tags=['home']
)

@router.get('/', status_code=status.HTTP_200_OK)
async def return_home(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})

@router.post("/submit_comment")
async def submit_form(name: str = Form(...), comment: str = Form(...), rating: str = Form(...),post_id: str = Form(...)):
    timestamp = datetime.now().isoformat()
    comment_data = {
        "name": name,
        "comment": comment,
        "rating":rating,
        "post_id":post_id,
        "timestamp": timestamp
    }

    database.comment_db.insert_one(comment_data)
    old_comment_number = database.db.find_one({"unique_id":int(post_id) })['comments']
    print("--------------------------------------------------------------------------old",old_comment_number)
    if not old_comment_number:
        old_comment_number = 0
    database.db.update_one(
    {"unique_id": int(post_id)},
    {"$set": {"comments": old_comment_number+1}}
    )

    return RedirectResponse(url=f'/view/{post_id}', status_code=302)

@router.post("/submit")
async def submit_form(title: str = Form(...), link: str = Form(...), category: str = Form(...),size:str = Form(...),desc:str = Form(...),username:str = Form(...),img:str = Form(...)):

    timestamp = datetime.now().isoformat()
    last_entry = database.db.find_one(sort=[("unique_id", -1)])
    unique_id = last_entry["unique_id"] + 1 if last_entry else 1
    user_data = {
        "title": title,
        "link": link,
        "size":size,
        "desc":desc,
        "category": category,
        "img":img,
        "username":username,
        "unique_id": unique_id,
        "timestamp": timestamp,
        "comments": 0
    }

    database.db.insert_one(user_data)
    return RedirectResponse(url=f'/view/{unique_id}', status_code=302)

@router.get("/users")
async def get_users():
    users = list(database.db.find({}, {"_id": 0}))  # Exclude the MongoDB ID from the results
    return users