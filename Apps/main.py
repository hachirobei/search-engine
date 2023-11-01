from fastapi import FastAPI
from Routes.Api import ProductRoutes, UserRoutes, AuthRoutes

app = FastAPI()

app.include_router(ProductRoutes.router, prefix="/api/products", tags=["products"])
app.include_router(UserRoutes.router, prefix="/api/users", tags=["users"])
app.include_router(AuthRoutes.router, prefix="/api/auth", tags=["authentication"])