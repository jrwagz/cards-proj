from pathlib import Path
import os


def home_dir():
    if 'TEST_HOME_DIR' in os.environ:
        return os.environ['TEST_HOME_DIR']
    else:
        return str(Path.home())


if __name__ == "__main__":
    print(home_dir())
