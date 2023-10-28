from fastapi import FastAPI

app = FastAPI()

# get method & endpoint for this index function
@app.get('/') 
# index function
def index():
    return {"message": "Hello, world!"}

# path parameter example without type
# @app.get('/blog/{id}')
# def get_blog(id):
#     return {"message": f"Blog with id {id}"}

@app.get('/blog/all')
def get_all_blogs():
    return {"message": "All blogs provided!"}

# path parameter example with type
@app.get('/blog/{id}')
def get_blog(id: int):
    return {"message": f"Blog with id {id}"}

