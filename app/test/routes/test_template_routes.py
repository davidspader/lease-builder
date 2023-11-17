from fastapi.testclient import TestClient
from fastapi import status
from app.db.models import Template as TemplateModel
from app.main import app

client = TestClient(app)

def test_add_category_route(db_session, authenticated_token):
    token = authenticated_token

    client.headers = token

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