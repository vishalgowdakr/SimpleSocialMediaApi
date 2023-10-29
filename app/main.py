from fastapi import FastAPI, Response, status, HTTPException
from models import Posts
from random import randint
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

posts = []
while True:
    try:
        connection = psycopg2.connect(user='postgres', password='llvr1', host='192.168.139.161', port='5432', database='SimpleSocialMedia', cursor_factory=RealDictCursor )
        cursor = connection.cursor()
        print("Connected to the database")
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
        time.sleep(2)

def find_post_by_id(id):
    for post in posts:
        if post.id == id:
            return post

@app.get('/posts/latest')
async def get_latest_post():
    if len(posts) > 0:
        post = posts[len(posts)-1]
        return {"post": post}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No latest post")


@app.get('/posts')
async def get_all_posts():
    return {"posts": posts}



@app.get('/posts/{id}')
async def get_post_by_id(id: int):
    post = find_post_by_id(id)
    if post:
        return post
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No post found with the specified id")


@app.post('/posts', status_code=status.HTTP_201_CREATED)
async def create_post(post: Posts):
    post.id = randint(0,100000)
    posts.append(post)
    return {"new post": post}

@app.put('/posts/{id}')
async def update_post(id: int, newpost: Posts):
    post = find_post_by_id(id)
    if post :
        post.id = id
        post.title = newpost.title
        post.content = newpost.content
        post.published = newpost.published
        return {"post": post}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No post found with the specified id")

@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    post = find_post_by_id(id)
    if post :
        posts.remove(post)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No post found with the specified id")
    

