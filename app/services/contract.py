from typing import List

from sqlalchemy.orm import Session


from app.schemas.contract import ContractFilter, ContractResponse

def get_contracts(payload: ContractFilter, skip: int, limit: int, db: Session) -> List[ContractResponse]:
    return 1