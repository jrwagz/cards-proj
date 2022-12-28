import pytest
from packaging.version import parse
import cards


@pytest.mark.xfail(
    parse(cards.__version__).major < 2,
    reason='> comparison is not supported in 1.x.x'
)
def test_less_than():
    c1 = cards.Card("a task")
    c2 = cards.Card("b task")
    assert c1 < c2

# @pytest.mark.xfail(reason='XPASS demo', strict=False)
# def test_xpass():
#     c1 = cards.Card("a task")
#     c2 = cards.Card("a task")
#     assert c1 == c2

# @pytest.mark.xfail(reason='strict demo')
# def test_xpass_strict():
#     c1 = cards.Card("a task")
#     c2 = cards.Card("a task")
#     assert c1 == c2
