from fastapi import APIRouter, Depends
from controller.productController import ProductController
from dependencies.token import get_current_user

router = APIRouter()

@router.get("/search/")
def search_products(query: str, current_user=Depends(get_current_user)):
    return ProductController.search_products(query)