from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session


import models
import shemas
import OAuth2
import database
import utils

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login', response_model= shemas.Token)
def login(user_credintials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credintials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Credintials invalid')

    if not utils.verify(user_credintials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Credintials invalid')

    access_token = OAuth2.create_access_token(data={"user_id": user.id})

    return {"access_token" : access_token, "token_type": "bearer"}