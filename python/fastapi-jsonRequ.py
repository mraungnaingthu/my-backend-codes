from fastapi import FastAPI, HTTPException, Request
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI()

class Database:
    def __init__(self):
        self.db = []

    def add_post(self, blog_post: dict):
        self.db.append(blog_post)

    def get_post(self):
        return self.db

db = Database()

class BlogPost(BaseModel):
    title: str
    content: Optional[str] = None

@app.post("/create_blog")
async def create_blog_post(blog_post: BlogPost):
    db.add_post(blog_post.dict())
    return {"message": "Blog post created successfully"}

@app.get("/retrive_blog")
async def get_blog_posts():
    return db.get_post()