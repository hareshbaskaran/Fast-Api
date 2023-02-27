from typing import Optional
from fastapi import FastAPI
from router1 import get_blog
from router1 import post_plog
from router1 import user
from router1 import article
from db.database import engine
from db import models
from router1 import product

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(get_blog.router)
app.include_router(post_plog.router)
app.include_router(product.router)


@app.get('/hello')
def index():
  return {'message': 'Hello world!'}

models.Base.metadata.create_all(engine)