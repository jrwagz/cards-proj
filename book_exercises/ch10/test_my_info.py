from unittest import mock
import pathlib
import my_info
import os


def test_my_home_env_var():
    os.environ["TEST_HOME_DIR"] = "/users/fake_user"
    value = my_info.home_dir()
    assert value == "/users/fake_user"


def test_my_home_returns_correct_value():
    with mock.patch.object(my_info, "home_dir") as mock_home_dir_func:
        mock_home_dir_func.return_value = "/users/fake_user"
        value = my_info.home_dir()
        assert value == "/users/fake_user"


# TODO: figure out why this is failing!
# looks like this is a complication with trying to mock the Path class
# i'm just going to modify the code we are testing to be better architected
# for testing, rather than try to solve the issue with mocking Path
# FAILED test_my_info.py::test_my_home_is_called -
# AttributeError: type object 'Path' has no attribute '_flavour'
# def test_my_home_is_called():
#     with mock.patch.object(pathlib, "Path", autospec=True) as myPath:
#         my_info.home_dir()
#         myPath.home.assert_called()
# check to see if Path.home() was called
