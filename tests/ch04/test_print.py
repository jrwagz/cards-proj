import pytest

def test_normal():
    print("\nprint normal")

@pytest.mark.xfail
def test_fail():
    print("\nprint in failing test")
    assert False

def test_disabled(capsys):
    with capsys.disabled():
        print('\ncapsys disabled print')