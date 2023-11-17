import pytest
from passlib.context import CryptContext
from app.db.connection import Session
from app.db.models import User as UserModel
from app.db.models import Template as TemplateModel

cryptContext = CryptContext(schemes=['sha256_crypt'])

@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()

@pytest.fixture()
def user_on_db(db_session):
    user = UserModel(
        username='username',
        password=cryptContext.hash('pass#')
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    yield user

    db_session.delete(user)
    db_session.commit()

@pytest.fixture()
def templates_on_db(db_session):
    templates = [
        TemplateModel(id='18XRdOWpOcoCebJhOOpZYGb733-BfIei_N-f58QhLQms', description='template description 1'),
        TemplateModel(id='18XRdOWpOcoCebJhOOpZYGb733-BfIei_N-f68QhLQms', description='template description 2'),
        TemplateModel(id='18XRdOWpOcoCebJhOOpZYGb733-BfIei_N-f78QhLQms', description='template description 3'),
        TemplateModel(id='18XRdOWpOcoCebJhOOpZYGb733-BfIei_N-f88QhLQms', description='template description 4')
    ]

    for template in templates:
        db_session.add(template)
    db_session.commit()

    for template in templates:
        db_session.refresh(template)

    yield templates

    for template in templates:
        db_session.delete(template)
    db_session.commit()