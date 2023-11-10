from fastapi import  Response, status, HTTPException, Depends, APIRouter
from app.schemas import  createUser, getUser, loginUser
from sqlalchemy.orm import Session
from .. import models 
from ..database import engine, get_db
from ..utils import get_password_hash
from ..OAuth2 import verify_token

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

#users
@router.put('/', response_model=getUser, status_code=status.HTTP_201_CREATED)
async def create_user(user: createUser, db: Session = Depends(get_db)):
    user.password = get_password_hash(user.password)
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.get('/{id}', response_model=getUser)
def get_user(id: int, db: Session = Depends(get_db),isLoggedIn: bool =  Depends(verify_token)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user found with the specified id")
    
