from fastapi import FastAPI
from enum import Enum
from typing import Optional

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

# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message': 'All blogs provided!'}

# Quarry parameter example dynamic value
# @app.get('/blog/all')
# def get_all_blogs(page, page_size):
#     return {'message': f'All {page_size} blogs on page {page}'}

# Quarry parameter example default value
# @app.get('/blog/all')
# def get_all_blogs(page = 1, page_size = 10):
#     return {'message': f'All {page_size} blogs on page {page}'}

# Quarry parameter example optional value
@app.get('/blog/all')
def get_all_blogs(page = 1, page_size: Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page}'}

# Quarry & Path parameter together example
@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message' : f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

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
