
from app.nested_script import nested_message

# def test_something_else():
#     assert True == True

def test_nested_message():
    assert nested_message() == "HELLO FROM A SCRIPT IN THE APP DIR"
