from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from Util.Security import verify_password, create_access_token, ALGORITHM, SECRET_KEY
from Model.UserModel import UserModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def authenticate_user(username: str, password: str):
    user = UserModel.get_user_by_username(username)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = UserModel.get_user_by_username(username)
    if user is None:
        raise credentials_exception
    return user