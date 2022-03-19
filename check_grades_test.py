import pytest
import System

#Tests if the program can handle a wrong username
def test_check_grades(grading_system):
    username = 'akend3'
    password = '123454321'
    course = 'comp_sci'

    grading_system.login(username, password)
    assert grading_system.usr.check_grades(course) == [['assignment1', 99],['assignment2', 66]]


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem