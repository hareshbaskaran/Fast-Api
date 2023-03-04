from fastapi import APIRouter
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import models
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
routerr = APIRouter(
    tags=['authentication']
)
@router.post('/token')
def get_token(
    request: OAuth2PasswordRequestForm = Depends(),
    db : Session = Depends(get_db)
):
    user = db.query(models.DbUser).filter(
        models.DbArticle.user == request.username).first()
    if not user:
        raise
        )
    