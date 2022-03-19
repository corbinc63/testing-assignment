import pytest
import System
import json

#Tests if the program can handle a wrong username
def test_create_assignment(grading_system):
    username = 'goggins'
    password = 'augurrox'
    course = 'comp_sci'
    assignment = 'assignment7'
    grading_system.login(username, password)
    grading_system.usr.create_assignment(assignment, "3/33/33", course)
    with open('Data/courses.json') as json_file:
        data = json.load(json_file)
    assert data[course]['assignments'][assignment]['due_date'] == "3/33/33"
    


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem