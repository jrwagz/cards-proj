import pytest
from cards import Card, InvalidCardId


pytestmark = pytest.mark.finish

@pytest.fixture(
    params=[
        'done',
        pytest.param('in prog',marks=pytest.mark.smoke),
        'todo'
        ]
)
def start_state_fixture(request):
    return request.param

@pytest.mark.smoke
class TestFinish:
    def test_finish_from_in_prog(self,cards_db):
        index = cards_db.add_card(Card("second edition",state='in prog'))
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == 'done'

    def test_finish_from_done(self,cards_db):
        index = cards_db.add_card(Card("write a book",state='done'))
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == 'done'

    def test_finish_from_todo(self,cards_db):
        index = cards_db.add_card(Card("create a course",state='todo'))
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == 'done'


@pytest.mark.parametrize(
    'start_state',
    [
        'done',
        pytest.param('in prog', marks=pytest.mark.smoke),
        'todo',
    ]
)
def test_finish_func(cards_db,start_state):
    initial_card = Card('irrelevant summary',state=start_state)
    index = cards_db.add_card(initial_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == 'done'

@pytest.mark.smoke
def test_finish_fix(cards_db,start_state_fixture):
    initial_card = Card('irrelevant summary',state=start_state_fixture)
    index = cards_db.add_card(initial_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == 'done'

@pytest.mark.smoke
@pytest.mark.exception
def test_finish_non_existent(cards_db):
    """
    Shouldn't be able to finish a non-existent card
    """
    index = 123 # any value here will be invalid since db is empty
    with pytest.raises(InvalidCardId):
        cards_db.finish(index)