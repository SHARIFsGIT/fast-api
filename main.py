from fastapi import FastAPI

app = FastAPI()

# get method & endpoint for this index function
@app.get('/') 
# index function
def index():
    return "Hello, world!"