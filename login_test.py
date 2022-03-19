import json
import pytest
import System

#Tests if the program can handle a wrong username
def test_login(grading_system):
    username = 'akend3'
    password =  '123454321'
    grading_system.login(username,password)
    with open('Data/users.json') as json_file:
        data = json.load(json_file)
    assert data[username]


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem