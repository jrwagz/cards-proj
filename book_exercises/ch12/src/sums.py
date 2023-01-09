# sums.py
# add the numbers in `data.txt`
import typer
from typing import Optional

app = typer.Typer()


@app.command()
def main(filename: str):
    sum = 0.0

    with open(filename, "r") as file:
        for line in file:
            number = float(line)
            sum += number

    print(f"{sum:.2f}")


if __name__ == "__main__":
    app()
