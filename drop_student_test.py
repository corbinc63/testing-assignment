import pytest
import System
import json

#Tests if the program can handle a wrong username
def test_drop_student(grading_system):
    username = 'goggins'
    password = 'augurrox'
    course = 'comp_sci'
    student = 'akend3'
    grading_system.login(username, password)
    grading_system.usr.drop_student(student, course)
    with open('Data/users.json') as json_file:
        data = json.load(json_file)
    assert course not in data[student]['courses']


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem