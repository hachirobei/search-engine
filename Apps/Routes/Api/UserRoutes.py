from fastapi import APIRouter, Depends, HTTPException, status
from Controller.UserController import UserController
from Dependencies.token import get_current_user, OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register/")
def register(username: str, password: str, role: str):
    return UserController.register_user(username, password, role)

@router.get("/profile/{username}")
def user_profile(username: str, current_user=Depends(get_current_user)):
    return UserController.get_user_profile(username)

@router.get("/users/")
def all_users(current_user=Depends(get_current_user(required_role='admin'))):
    return UserController.get_all_users()

@router.delete("/delete/{username}")
def delete_user(username: str, current_user=Depends(get_current_user(required_role='admin'))):
    return UserController.delete_user(username)