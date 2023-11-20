from app.schemas.base import CustomBaseModel

class Document_info(CustomBaseModel):
    template_id: str
    name: str
    rg: str
    cpf: str
    address:str
    cep: str
    phone: str
    start_date: str
    end_date: str
    rental_value: float
    down_payment_value: float
    cleaning_fee: float