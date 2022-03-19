import pytest
import System
import Staff
import json

#Tests if the program can handle a wrong username
def test_change_grade(grading_system):
    user = 'akend3'
    username = 'goggins'
    password = 'augurrox'
    course = 'comp_sci'
    assignment = 'assignment1'
    grade = 3
    grading_system.login(username, password)
    grading_system.usr.change_grade(user, course, assignment, grade)
    with open('Data/users.json') as json_file:
        data = json.load(json_file)
    assert data[user]['courses'][course][assignment]['grade'] == grade


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem