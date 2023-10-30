from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()

# get method & endpoint for this index function
@app.get('/') 
def index():            # index function
    return {'message': 'Hello, world!'}

# path parameter example without type
# @app.get('/blog/{id}')
# def get_blog(id):
#     return {'message' : f'Blog with id {id}'}

# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message': 'All blogs provided!'}

# Query parameter example dynamic value
# @app.get('/blog/all')
# def get_all_blogs(page, page_size):
#     return {'message': f'All {page_size} blogs on page {page}'}

# Query parameter example default value
# @app.get('/blog/all')
# def get_all_blogs(page = 1, page_size = 10):
#     return {'message': f'All {page_size} blogs on page {page}'}

# Tag example
@app.get('/blog/all', 
         tags= ['blog'],
         summary= 'Retrive all blogs',
         description= 'This api call simmulates fetching all blogs',
         response_description= 'The list of available blogs'
         )
def get_all_blogs(page = 1, page_size: Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page}'}

@app.get('/blog/{id}/comments/{comment_id}', tags= ['blog', 'comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog

    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query paramenter
    - **username** optional query parameter
    """
    return {'message' : f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

# Query parameter example optional value
# @app.get('/blog/all')
# def get_all_blogs(page = 1, page_size: Optional[int] = None):
#     return {'message': f'All {page_size} blogs on page {page}'}

# Query & Path parameter together example
# @app.get('/blog/{id}/comments/{comment_id}')
# def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
#     return {'message' : f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

# Enum path parameter
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}', tags= ['blog'])
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}

# path parameter example with type
@app.get('/blog/{id}')
def get_blog(id: int):
    return {'message': f'Blog with id {id}'}

# status code example
# @app.get('/blog/{id}', status_code=status.HTTP_404_NOT_FOUND)
# def get_blog(id: int):
#     if id > 5:
#         return {'error' : f'Blog {id} not found!'}
#     else:
#         return {'message': f'Blog with id {id}'}

# status code response example
@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags= ['blog'])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error' : f'Blog {id} not found!'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}
    
