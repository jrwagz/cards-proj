import cards
import pytest
from cards import Card


@pytest.fixture(scope="session")
def tmp_db_path(tmp_path_factory):
    """Path to temporary database"""
    return tmp_path_factory.mktemp("cards_db")


@pytest.fixture(scope="session")
def session_cards_db(tmp_db_path):
    """CardsDB"""
    db_ = cards.CardsDB(tmp_db_path)
    yield db_
    db_.close()


@pytest.fixture(scope="function")
def cards_db(session_cards_db):
    """Empty CardsDB"""
    db = session_cards_db
    db.delete_all()
    return db

@pytest.fixture(scope="session")
def example_three_cards():
    return [
        Card("foo"),
        Card("bar", owner="me"),
        Card("baz", owner="you", state="in prog"),
    ]

@pytest.fixture(scope="function")
def cards_db_three_cards(cards_db, example_three_cards):
    """CardsDB with 3 cards"""
    for c in example_three_cards:
        cards_db.add_card(c)
    return cards_db
