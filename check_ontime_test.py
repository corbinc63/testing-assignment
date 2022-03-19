import pytest
import System

#Tests if the program can handle a wrong username
def test_check_ontime(grading_system):
    username = 'akend3'
    password = '123454321'
    submission_date = '2/9/20'
    due_date = '2/10/20'
    grading_system.login(username, password)
    assert grading_system.usr.check_ontime(submission_date,due_date) == True

    submission_date = '2/10/20'
    due_date = '2/9/20'
    assert grading_system.usr.check_ontime(submission_date,due_date) == False




@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem