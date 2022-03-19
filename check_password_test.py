import pytest
import System


def test_check_password(grading_system):
    username = 'akend3'
    password =  '123454321'
    assert grading_system.check_password(username,password) == True
    username = 'akend3'
    password = ''
    assert grading_system.check_password(username,password) == False
    username = 'akend3'
    password = '#$^&#&$^(@$'
    assert grading_system.check_password(username,password) == False
    username = 'akend3'
    password = '                   '
    assert grading_system.check_password(username,password) == False
    username = 'akend3'
    password = '8235498y2895y982y398rf893889y298hf398h293hfhseiuhf2789yeehfiuah78y923yf29fhdaihf32y9fy9sahdf92yh93yhf9ohud9ayf928ye98fh2983h9f'
    assert grading_system.check_password(username,password) == False



@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem