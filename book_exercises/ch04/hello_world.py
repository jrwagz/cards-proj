def hello():
    """Prints iconic Hello World! message to a file in the current directory"""
    with open("hello.txt","w") as f:
        f.write("Hello World!\n")

if __name__ == "__main__":
    hello()

def test_hello():
    """This example just uses whatever directory the test is called from
    that's a bad idea, since it's not automatically cleaned up between runs
    in order to create repeatable results"""
    hello()
    with open("hello.txt", 'r') as f:
        contents = f.read().rstrip()
        assert contents == "Hello World!"

def test_hello_tmp_path(monkeypatch, tmp_path):
    """Tests Hello function, using monkeypatch and tmp_path to create/cleanup a temp directory
    for the test on every run"""
    monkeypatch.chdir(tmp_path)
    print(f'\nCreating a file at: {tmp_path}')
    hello()
    with open("hello.txt", 'r') as f:
        contents = f.read().rstrip()
        assert contents == "Hello World!"