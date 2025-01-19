from starlette import status
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, HTTPException, Path, Request, status
import json
import database
import requests as rq
templates = Jinja2Templates(directory="templates")


router = APIRouter(
    prefix='/explore',
    tags=['explore']
)




@router.get('/', status_code=status.HTTP_200_OK)
async def return_home(request: Request,search):
    data = rq.get('https://excel2api.vercel.app/api/1BSOoMb-j3ALwi56lgSW8x7q17iNGSbuq1gpi9vV_ZOQ')
    data = data.json()
    if not search:        
        return templates.TemplateResponse("search.html", {"request": request,"data":data})
    else:
        search_result = []
        for value in data:
            if search.lower() in value['Title'].lower():
                search_result.append(value)
        return templates.TemplateResponse("search.html", {"request": request,"data":search_result})

    

@router.get('/categories/{category}', status_code=status.HTTP_200_OK)
async def return_home(request: Request,category):
    data = rq.get('https://excel2api.vercel.app/api/1BSOoMb-j3ALwi56lgSW8x7q17iNGSbuq1gpi9vV_ZOQ')
    data = data.json()
    if not category:
        return templates.TemplateResponse("search.html", {"request": request,"data":data})
    else:
        search_result = []
        for value in data:
            if category.lower() in value['Category'].lower():
                search_result.append(value)
        return templates.TemplateResponse("search.html", {"request": request,"data":search_result})

