from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# get method & endpoint for this index function
@app.get('/') 
# index function
def index():
    return {'message': 'Hello, world!'}

# path parameter example without type
# @app.get('/blog/{id}')
# def get_blog(id):
#     return {"message": f"Blog with id {id}"}

@app.get('/blog/all')
def get_all_blogs():
    return {'message': 'All blogs provided!'}

# Enum path parameter
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}

# path parameter example with type
@app.get('/blog/{id}')
def get_blog(id: int):
    return {'message': f'Blog with id {id}'}

