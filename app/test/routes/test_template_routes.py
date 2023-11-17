from fastapi.testclient import TestClient
from fastapi import status
from app.db.models import Template as TemplateModel
from app.main import app

client = TestClient(app)

def test_add_template_route(db_session, authenticated_token):
    client.headers = authenticated_token

    body = {
        "id": "18XRdOWpOcoCebJhOOpZYGb733-BfIei_N-f58QhLQms",
        "description": "template description"
    }

    response = client.post('/template/add', json=body)

    assert response.status_code == status.HTTP_201_CREATED

    templates = db_session.query(TemplateModel).all()

    assert len(templates) == 1
    
    db_session.delete(templates[0])
    db_session.commit()

def test_list_templates_route(templates_on_db, authenticated_token):
    client.headers = authenticated_token

    response = client.get('/template/list')

    assert response.status_code == status.HTTP_200_OK

    templates = response.json()

    assert len(templates) == 4
    assert templates[0] == {
        "id": templates_on_db[0].id,
        "description": templates_on_db[0].description
    }