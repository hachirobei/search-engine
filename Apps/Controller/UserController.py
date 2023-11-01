from Model.UserModel import UserModel
from Util.Security import get_password_hash, create_access_token, verify_password
from fastapi import HTTPException, status

class UserController:
    
    @staticmethod
    def register_user(username: str, password: str, role: str):
        if UserModel.get_user_by_username(username):
            raise HTTPException(status_code=400, detail="Username already registered")
        
        if role not in ['admin', 'user']:
            raise HTTPException(status_code=400, detail="Invalid role")

        hashed_password = get_password_hash(password)
        new_user = UserModel.create(username=username, hashed_password=hashed_password, role=role)
        return new_user
    
    @staticmethod
    def authenticate_user(username: str, password: str):
        user = UserModel.get_user_by_username(username)
        if not user:
            return False

        if not verify_password(password, user.hashed_password):
            return False

        return user
    
    @staticmethod
    def get_user_profile(username: str):
        user = UserModel.get_user_by_username(username)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
    @staticmethod
    def get_all_users():
        return UserModel.get_all_users()
    
    @staticmethod
    def delete_user(username: str):
        if not UserModel.delete(username):
            raise HTTPException(status_code=404, detail="User not found")
        return {"detail": "User deleted successfully"}