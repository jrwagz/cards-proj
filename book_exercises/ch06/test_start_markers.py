import pytest
from cards import Card, InvalidCardId

@pytest.mark.smoke
def test_start(cards_db):
    """
    Start changes state from 'todo' to 'in prog'
    """
    index = cards_db.add_card(Card("foo",state='todo'))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == 'in prog'

@pytest.mark.exception
def test_start_non_existent(cards_db):
    """
    Shouldn't be able to start a non-existent card
    """
    index = 123 # any value here will be invalid since db is empty
    with pytest.raises(InvalidCardId):
        cards_db.start(index)
