from sqlalchemy import or_, select
from typing import List

from sqlalchemy.orm import Session


from app.models.contract import Contract
from app.schemas.contract import ContractFilter, ContractResponse

def get_contracts(payload: ContractFilter, skip: int, limit: int, db: Session) -> List[ContractResponse]:
    data = payload.model_dump(exclude_none=True)
    filter_contracts = select(Contract)
    for k, i in data.items():
        column = getattr(Contract, k, None)

        if column is not None:
            filter_contracts = filter_contracts.where(column==i)

    query = filter_contracts.offset(skip).limit(limit)
    contracts = db.execute(query).scalars().all()
    return contracts


