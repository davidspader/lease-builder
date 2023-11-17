from typing import List
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.use_cases.template import TemplateUseCases
from app.schemas.template import Template
from app.routes.deps import get_db_session, auth

router = APIRouter(prefix='/template', tags=['Template'], dependencies=[Depends(auth)])

@router.post('/add', status_code=status.HTTP_201_CREATED, description='Add new template')
def add_template(
    template: Template,
    db_session: Session = Depends(get_db_session)
):
    uc = TemplateUseCases(db_session=db_session)
    uc.add_template(template=template)

    return Response(status_code=status.HTTP_201_CREATED)

@router.get('/list', response_model=List[Template], description='List all templates')
def list_templates(
    db_session: Session = Depends(get_db_session)
):
    uc = TemplateUseCases(db_session=db_session)
    response = uc.list_templates()
    return response

@router.delete('/delete/{id}', description='Delete template')
def delete_templates(
    id: str,
    db_session: Session = Depends(get_db_session)
):
    uc = TemplateUseCases(db_session=db_session)
    uc.delete_template(id=id)

    return Response(status_code=status.HTTP_200_OK)