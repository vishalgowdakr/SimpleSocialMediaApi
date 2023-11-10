from fastapi import  Response, status, HTTPException, Depends, APIRouter
from ..database import engine, get_db
from app.schemas import loginUser
from sqlalchemy.orm import Session
from .. import models, OAuth2 
from ..utils import verify_password

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/login",
    tags=["Auth"],
)

#method for user to login using a username and password
@router.post('/', status_code=status.HTTP_200_OK)
async def login_user(user: loginUser, db: Session = Depends(get_db)):
    user_ = db.query(models.User).filter(models.User.username == user.username).first()
    if user:
        if verify_password(user.password, user_.password):
            jwt_token = OAuth2.create_access_token(data={"username": user.username})
            return {'token': jwt_token, 'token_type': 'bearer',}
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Credentials")
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Credentials")


