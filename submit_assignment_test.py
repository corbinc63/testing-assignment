import pytest
import System
import json

#Tests if the program can handle a wrong username
def test_submit_assignment(grading_system):
    username = 'akend3'
    password = '123454321'
    course = 'comp_sci'
    assignment_name = 'assignment2'
    submission = 'garbagio'
    submission_date = '2/9/20'
    grading_system.login(username, password)
    grading_system.usr.submit_assignment(course,assignment_name,submission,submission_date)
    with open('Data/users.json') as json_file:
        data = json.load(json_file)
    assert data[username]['courses'][course][assignment_name]['submission'] == submission and data[username]['courses'][course][assignment_name]['submission_date'] == submission_date


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem