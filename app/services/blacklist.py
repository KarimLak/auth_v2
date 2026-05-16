from fastapi import Depends
from niquests import Session
from sqlalchemy import or_, select
from app.database import get_db
from app.models.blacklist import BlackList
from app.repositories.token import get_blacklist_token

def is_black_list_token(refresh_token: str, db : Session) -> bool:
    blacklisttoken = get_blacklist_token(refresh_token, db)
    if blacklisttoken:
        return True
    else:
        return False