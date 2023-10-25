from fastapi import FastAPI

app = FastAPI()

@app.get()
async def get_all_todos():
    return {"message": "Hello there"}