from subprocess import run
import sums


def test_sums_subprocess():
    result = run(["python3", "sums.py", "data.txt"], capture_output=True, text=True)
    assert result.stdout == "200.00\n"


def test_sums_import(capsys):
    sums.main()
    assert capsys.readouterr().out == "200.00\n"
