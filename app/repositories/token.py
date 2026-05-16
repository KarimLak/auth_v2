from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.models.blacklist import BlackList
from app.models.user import User

def get_blacklist_token(refresh_token: str, db: Session) -> BlackList:
    return db.execute(select(BlackList).where(BlackList.refresh_token == refresh_token)).scalars().one_or_none()

def add_blacklist_token(access_token: str, refresh_token: str, db: Session):
    blacklist = BlackList(access_token = access_token, refresh_token = refresh_token)
    db.add(blacklist)
    db.commit()
    db.refresh(blacklist)