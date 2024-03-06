from cartepizzeria import CartePizzeria

def test_is_empty(mocker):
    mocker.patch('CartePizzeria.is_empty', return_value=100)
 
    expected_value = 100
    assert CartePizzeria.is_empty() == expected_value