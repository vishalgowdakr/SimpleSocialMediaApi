from fastapi import  Response, status, HTTPException, Depends, APIRouter
from ..database import engine, get_db
from app.schemas import Posts, GetPost
from sqlalchemy.orm import Session
from .. import models 
from ..OAuth2 import verify_token 

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
    dependencies=[Depends(verify_token)],
)

@router.get('/', response_model=list[GetPost])
async def get_all_posts(db: Session = Depends(get_db) ):
    posts = db.query(models.Post).all()
    return posts

@router.get('/{id}', response_model=GetPost)
async def get_post_by_id(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if post:
        return post
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No post found with the specified id")
    
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=GetPost)
async def create_post(post: Posts, db: Session = Depends(get_db)):
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.put('/{id}', response_model=GetPost)
async def update_post(id: int, newpost: Posts, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() != None:
        updated_post = post.update(newpost.model_dump(), synchronize_session=False)
        db.commit()    
        return  post.first()

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() != None:
        post.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No post found with the specified id")
