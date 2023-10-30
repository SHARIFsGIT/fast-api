from fastapi import FastAPI
from router import blog_get
from router import blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

# get method & endpoint for this index function
@app.get('/') 
# index function
def index():            
    return {'message': 'Hello, world!'}

