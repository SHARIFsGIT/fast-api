from fastapi import APIRouter, status, Response
from typing import Optional
from enum import Enum

# all the get methods came from main.py
# all @app replaced with @route
# as prefix have '/blog' so all the '/blog' removed from all endpoints
# all the tags also removed
router = APIRouter(
    prefix= '/blog',
    tags= ['blog']
)

# path parameter example without type
# @router.get('/{id}')
# def get_blog(id):
#     return {'message' : f'Blog with id {id}'}

# @router.get('/all')
# def get_all_blogs():
#     return {'message': 'All blogs provided!'}

# Query parameter example dynamic value
# @router.get('/all')
# def get_all_blogs(page, page_size):
#     return {'message': f'All {page_size} blogs on page {page}'}

# Query parameter example default value
# @router.get('/all')
# def get_all_blogs(page = 1, page_size = 10):
#     return {'message': f'All {page_size} blogs on page {page}'}

# Tag example
@router.get('/all', 
         summary= 'Retrive all blogs',
         description= 'This api call simmulates fetching all blogs',
         response_description= 'The list of available blogs'
         )
def get_all_blogs(page = 1, page_size: Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page}'}

@router.get('/{id}/comments/{comment_id}', tags= ['comment'])
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
# @router.get('/all')
# def get_all_blogs(page = 1, page_size: Optional[int] = None):
#     return {'message': f'All {page_size} blogs on page {page}'}

# Query & Path parameter together example
# @router.get('/{id}/comments/{comment_id}')
# def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
#     return {'message' : f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

# Enum path parameter
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}

# path parameter example with type
# @router.get('/{id}')
# def get_blog(id: int):
#     return {'message': f'Blog with id {id}'}

# status code example
# @router.get('/{id}', status_code=status.HTTP_404_NOT_FOUND)
# def get_blog(id: int):
#     if id > 5:
#         return {'error' : f'Blog {id} not found!'}
#     else:
#         return {'message': f'Blog with id {id}'}

# status code response example
@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error' : f'Blog {id} not found!'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}
    
