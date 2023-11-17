import pytest
from fastapi.exceptions import HTTPException
from app.use_cases.template import TemplateUseCases
from app.db.models import Template as TemplateModel
from app.schemas.template import Template

def test_add_template_uc(db_session):
    uc = TemplateUseCases(db_session)

    template = Template(
        id='18XRdOWpOcoCebJhOOpZYGb733-BfIei_N-f58QhLQms',
        description='template description'
    )

    uc.add_template(template=template)

    templates_on_db = db_session.query(TemplateModel).all()

    assert len(templates_on_db) == 1
    assert templates_on_db[0].id == '18XRdOWpOcoCebJhOOpZYGb733-BfIei_N-f58QhLQms'
    assert templates_on_db[0].description == 'template description'

    db_session.delete(templates_on_db[0])
    db_session.commit()

def test_list_templates_uc(db_session, templates_on_db):
    uc = TemplateUseCases(db_session)

    templates = uc.list_templates()

    assert len(templates) == 4
    assert templates[0].id == templates_on_db[0].id
    assert templates[0].description == templates_on_db[0].description
    assert templates[1].id == templates_on_db[1].id
    assert templates[1].description == templates_on_db[1].description
    assert templates[2].id == templates_on_db[2].id
    assert templates[2].description == templates_on_db[2].description
    assert templates[3].id == templates_on_db[3].id
    assert templates[3].description == templates_on_db[3].description

def test_delete_template_uc(db_session):
    new_template = TemplateModel(id='18XRdOWpOcoCebJhOOpZYGb733-BfIei_N-f58QhLQms', description='template description')
    db_session.add(new_template)
    db_session.commit()

    uc = TemplateUseCases(db_session)
    uc.delete_template(id=new_template.id)

    templates = db_session.query(TemplateModel).first()
    assert templates is None

def test_delete_template_uc_non_exists(db_session):
    uc = TemplateUseCases(db_session)

    with pytest.raises(HTTPException):
        uc.delete_template(id='invalid id')