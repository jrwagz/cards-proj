from typer.testing import CliRunner
import sums
import pytest

runner = CliRunner()


@pytest.mark.parametrize(
    ("filename", "expected"),
    [("tests/data.txt", "200.00\n")],
)
def test_files(filename, expected):
    result = runner.invoke(sums.app, [filename])
    assert result.stdout == expected


def test_no_argument():
    result = runner.invoke(sums.app)
    assert "Missing argument 'FILENAME'." in result.stdout
