from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.responses import PlainTextResponse
from fastapi import status
from exception import StoryException
from router import blog_get
from router import blog_post
from db import models 
from db.database import engine
from router import user
from router import article

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

# get method & endpoint for this index function
@app.get('/') 
# index function
def index():            
    return {'message': 'Hello, world!'}

# Custom exception handling
@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exception: StoryException):
    return JSONResponse(
        status_code=418,
        content= {'detail': exception.name}
    )

# Custom handler
@app.exception_handler(HTTPException)
def custom_handler(request: Request, exception: StoryException):
    return PlainTextResponse(str(exception), status_code=status.HTTP_400_BAD_REQUEST)

models.Base.metadata.create_all(engine)