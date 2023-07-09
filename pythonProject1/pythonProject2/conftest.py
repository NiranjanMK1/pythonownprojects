import pytest

@pytest.fixture
def my_input():
    first_input = 55
    return first_input
# @pytest.fixture(scope='session')
# def myfixutre():
#     print("This is conftest fixture")