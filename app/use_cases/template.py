from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status
from app.db.models import Template as TemplateModel
from app.schemas.template import Template

class TemplateUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_template(self, template: Template):
        template_model = TemplateModel(**template.dict())
        self.db_session.add(template_model)
        self.db_session.commit()

    def list_templates(self):
        categories = self.db_session.query(TemplateModel).all()
        return categories
    
    def delete_template(self, id: str):
        template = self.db_session.query(TemplateModel).filter_by(id=id).first()

        if not template:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Template not found'
            )
        
        self.db_session.delete(template)
        self.db_session.commit()