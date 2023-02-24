from fastapi import FastAPI
from router1 import get_blog


app = FastAPI()
app.include_router(get_blog.router)

@app.get('/hello')
def index():
  return {'message': 'Hello world!'}