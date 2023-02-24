from fastapi import FastAPI
from router1 import get_blog
from router1 import post_plog

app = FastAPI()
app.include_router(get_blog.router)
app.include_router(post_plog.router)
@app.get('/hello')
def index():
  return {'message': 'Hello world!'}