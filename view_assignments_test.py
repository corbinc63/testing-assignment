import pytest
import System

#Tests if the program can handle a wrong username
def test_view_assignments(grading_system):
    username = 'akend3'
    password = '123454321'
    course = 'comp_sci'
    grading_system.login(username, password)
    assert grading_system.usr.view_assignments(course) == [['assignment1', '2/2/20'], ['assignment2', '2/10/20']]

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem