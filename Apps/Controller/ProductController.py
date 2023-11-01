from model.productModel import ProductModel
from fastapi import HTTPException

class ProductController:

    @staticmethod
    def search_products(query: str):
        products = ProductModel.search(query)
        if not products:
            raise HTTPException(status_code=404, detail="No products found for the given query")
        return products