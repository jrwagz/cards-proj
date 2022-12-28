import pytest

def test_no_marker(cards_db):
    assert cards_db.count() == 0

@pytest.mark.num_cards
def test_marker_no_param(cards_db):
    assert cards_db.count() == 0

@pytest.mark.num_cards()
def test_marker_no_param_parens(cards_db):
    assert cards_db.count() == 0

@pytest.mark.num_cards(3)
def test_three_cards(cards_db):
    assert cards_db.count() == 3

    # just for fun, look at the cards created by Faker
    print()
    for c in cards_db.list_cards():
        print(c)

@pytest.mark.num_cards(100)
def test_marker(cards_db):
    assert cards_db.count() == 100