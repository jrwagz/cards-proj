"""
Test Cases
* `list` from an empty database
* `list` from a non-empty database
"""
from cards import Card


def test_list_no_cards(cards_db):
    """Empty db, empty list"""
    assert cards_db.list_cards() == []


def test_list_several_cards(cards_db,example_three_cards):
    """
    Given a variety of cards, make sure they get returned.
    """

    for c in example_three_cards:
        cards_db.add_card(c)

    the_list = cards_db.list_cards()

    assert len(the_list) == len(example_three_cards)
    for c in example_three_cards:
        assert c in the_list

def test_list_with_owner(cards_db_three_cards):
    """
    Test providing an owner parameter to the list function
    """

    the_list = cards_db_three_cards.list_cards(owner="me")
    assert len(the_list) == 1

def test_list_with_owner_non_existent(cards_db_three_cards):
    """
    Test providing a non-existent owner parameter to the list function
    """

    the_list = cards_db_three_cards.list_cards(owner="fake")
    assert len(the_list) == 0

def test_list_with_state(cards_db_three_cards):
    """
    Test providing an state parameter to the list function
    """

    the_list = cards_db_three_cards.list_cards(state="in prog")
    assert len(the_list) == 1

def test_list_with_state_non_existent(cards_db_three_cards):
    """
    Test providing a non-existent state parameter to the list function
    """

    the_list = cards_db_three_cards.list_cards(state="fake")
    assert len(the_list) == 0

def test_list_with_owner_and_state(cards_db_three_cards):
    """
    Test providing owner and state parameter to the list function
    """

    the_list = cards_db_three_cards.list_cards(owner="you", state="in prog")
    assert len(the_list) == 1

def test_list_with_owner_and_state_non_existent(cards_db_three_cards):
    """
    Test providing non-existent owner and state parameter to the list function
    """

    the_list = cards_db_three_cards.list_cards(owner="fake", state="fake_state")
    assert len(the_list) == 0