from subprocess import run


def test_sums_subprocess():
    result = run(["python3", "sums.py", "data.txt"], capture_output=True, text=True)
    assert result.stdout == "200.00\n"
