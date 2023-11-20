from app.schemas.document_info import Document_info

def test_document_info_schema():
    document_info = Document_info(
        template_id='18XRdOWpOcoCebJhOOpZYGb733-BfIei_N-f58QhLQms',
        name='João pé de feijão',
        rg='12.674.156-6',
        cpf='292.629.784-05',
        address='Rua da Matriz 40, 389, Centro, Cedro-PE',
        cep='56130-970',
        phone='(87) 98450-2983',
        start_date='2024-10-27',
        end_date='2024-11-05',
        rental_value=5000.50,
        down_payment_value=1000.50,
        cleaning_fee=250.50
    )

    assert document_info.dict() == {
        'template_id': '18XRdOWpOcoCebJhOOpZYGb733-BfIei_N-f58QhLQms',
        'name': 'João pé de feijão',
        'rg': '12.674.156-6',
        'cpf': '292.629.784-05',
        'address': 'Rua da Matriz 40, 389, Centro, Cedro-PE',
        'cep': '56130-970',
        'phone': '(87) 98450-2983',
        'start_date': '2024-10-27',
        'end_date': '2024-11-05',
        'rental_value': 5000.50,
        'down_payment_value': 1000.50,
        'cleaning_fee': 250.50
    }