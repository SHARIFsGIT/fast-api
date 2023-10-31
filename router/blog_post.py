from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix= '/blog',
    tags= ['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version
        }

# Query parameter
@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, 
                   id: int, 
                   comment_id: int = Query(None, 
                                           title= 'ID of the comment', 
                                           description= 'Some description for comment_id',
                                           alias= 'commentId',
                                           deprecated= True
                                        ),
# Body parameter
                    content: str = Body(..., min_length= 10, max_length= 15, regex= '^[a-z\s]*$') # ... or Ellipsis
                ):
    return{ 
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        'content': content
    }