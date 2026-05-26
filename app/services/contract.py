from sqlalchemy.orm import Session
from app.repositories.contract import get_contracts_list
from app.schemas.contract import ContractFilter, ContractFilterResponse, ContractResponse, ContractSortField, SortOrder

def get_contracts(payload: ContractFilter, skip: int, limit: int, sort_by: ContractSortField, sort_order: SortOrder, db: Session) -> ContractFilterResponse:
    data = payload.model_dump(exclude_none=True)
    contracts = get_contracts_list(data, skip, limit, sort_by, sort_order, db)
    return ContractFilterResponse(skip = skip, limit = limit, sort_by = sort_by, sort_order = sort_order, contracts = contracts)


