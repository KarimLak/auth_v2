from fastapi import APIRouter
from auth_v2.app import limiter 

router = APIRouter(prefix='/profile')

@router.post('/')
@limiter.limit("10/minute")
def create_profile():
    return 1

@router.get('/')
@limiter.limit("10/minute")
def get_profile():
    return 1
