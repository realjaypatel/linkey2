from starlette import status
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, HTTPException, Path, Request, status
import json
import database
import requests as rs
import ast
templates = Jinja2Templates(directory="templates")


router = APIRouter(
    prefix='/view',
    tags=['product']
)

data = {
    
}




@router.get('/{unique_id}', status_code=status.HTTP_200_OK)
async def return_home(unique_id,request: Request):
    print(unique_id)
    try:    
        post_data = database.db.find_one({"unique_id": int(unique_id)})
        print(post_data)
        if post_data:
            user_comment = list(database.comment_db.find({'post_id': unique_id}))
            print('user comm', user_comment)
            return templates.TemplateResponse("product.html", {"request": request,"data":post_data,"comments":user_comment})

            return post_data
        else:
            raise HTTPException(status_code=404, detail="Data not found")
    except:
        return 'as'


