from fastapi import APIRouter, Depends, HTTPException, status
from Util.Security import get_password_hash, create_access_token
from dependencies.token import authenticate_user, OAuth2PasswordRequestForm
from Model.UserModel import UserModel

router = APIRouter()

@router.post("/login/", response_model=dict)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register/")
def register_user(username: str, password: str, role: str):
    if role not in ['admin', 'user']:
        raise HTTPException(status_code=400, detail="Invalid role")
    
    hashed_password = get_password_hash(password)
    new_user = UserModel.create(username=username, hashed_password=hashed_password, role=role)
    return new_user