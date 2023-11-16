import pytest
from app.schemas.template import Template

def test_template_schema():
    template = Template(
        id='18XRdOWpOcoCebJhOOpZYGb733-BfIei_N-f58QhLQms',
        description='template description'
    )

    assert template.dict() == {
        'id': '18XRdOWpOcoCebJhOOpZYGb733-BfIei_N-f58QhLQms',
        'description': 'template description'
    }

def test_tempalte_schema_invalid_description():
    with pytest.raises(ValueError):
        Template(
            id='18XRdOWpOcoCebJhOOpZYGb733-BfIei_N-f58QhLQms',
            description=''
        )