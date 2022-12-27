from cards import Card
import pytest

@pytest.mark.skip(reason='this comparison not yet implemented!')
def test_less_than():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2