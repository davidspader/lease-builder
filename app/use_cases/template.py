from sqlalchemy.orm import Session
from app.db.models import Template as TemplateModel
from app.schemas.template import Template

class TemplateUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_template(self, template: Template):
        template_model = TemplateModel(**template.dict())
        self.db_session.add(template_model)
        self.db_session.commit()