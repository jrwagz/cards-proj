import pytest

@pytest.fixture()
def the_answer():
    """Get the answer to the life, universe and everything"""
    return 42

@pytest.fixture(scope='module')
def sample_dict():
    print('before yield!')
    yield {
        'name': 'pytest_example',
        'type': 'fixture_function',
        'data': 'dictionary'
    }
    print('after yield!')

@pytest.fixture()
def sample_list():
    return [
        'bob',
        'joe',
        'cindy',
        'marlene',
        'sandy',
        'mandy'
    ]

@pytest.fixture()
def sample_tuple():
    return (42, 'answer', 'life', 'universe', 'everything')

def test_tuple(sample_tuple):
    assert len(sample_tuple) == 5

def test_tuple_2(sample_tuple):
    assert 'answer' in sample_tuple

def test_list(sample_list):
    assert len(sample_list) == 6

def test_list_2(sample_list):
    assert 'joe' in sample_list

def test_dict(sample_dict):
    assert len(sample_dict) == 3

def test_dict_2(sample_dict):
    assert 'dictionary' in sample_dict.values()

def test_dict_3(sample_dict):
    assert 'type' in sample_dict.keys()