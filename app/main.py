from fastapi import FastAPI, Response, status, HTTPException, Depends
from app.schemas import Posts
from random import randint
from sqlalchemy.orm import Session
from . import models as models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/posts')
async def get_all_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {'posts': posts}



@app.get('/posts/{id}')
async def get_post_by_id(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if post:
        return {'post': post}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No post found with the specified id")
    
@app.post('/posts', status_code=status.HTTP_201_CREATED)
async def create_post(post: Posts, db: Session = Depends(get_db)):
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"new post": new_post}

@app.put('/posts/{id}')
async def update_post(id: int, newpost: Posts, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() != None:
        updated_post = post.update(newpost.model_dump(), synchronize_session=False)
        db.commit()    
        return  {'post': post.first()}

@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() != None:
        post.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No post found with the specified id")
    
