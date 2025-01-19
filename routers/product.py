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
        user_data = database.db.find_one({"unique_id": int(unique_id)})
        print(user_data)
        if user_data:
            return templates.TemplateResponse("product.html", {"request": request,"data":user_data})

            return user_data
        else:
            raise HTTPException(status_code=404, detail="Data not found")
    except:
        return 'as'


