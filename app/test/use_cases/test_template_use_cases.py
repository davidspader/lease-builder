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