from fastapi import FastAPI
from models import Posts
from random import randint

app = FastAPI()

posts = []

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
        return {"message": "No latest post"}

@app.get('/posts')
async def get_all_posts():
    return {"posts": posts}



@app.get('/posts/{id}')
async def get_post_by_id(id: int):
    post = find_post_by_id(id)
    if post:
        return post
    else:
        return {"message": "No post found with the specified id"}

@app.post('/posts')
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
        return {"message": "No post found with the specified id"}

@app.delete('/posts/{id}')
async def delete_post(id: int):
    post = find_post_by_id(id)
    if post :
        posts.remove(post)
        return {"id": id}
    else:
        return {"message": "No post found with the specified id"}
    
