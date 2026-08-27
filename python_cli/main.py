import typer
from typing import Optional

app = typer.Typer()

@app.command()
def hello(name:str):
	print(f"hello {name}")

@app.command()
def goodbye(name:str, formal: bool = False):
	if formal:
		print(f" Goodbye Ms. {name}. Have a good day")
	else:
		print(f"Bye {name}")

# def type_example(name: str, formal: bool = False, intro: Optional[str] = None):
  #  pass

# def main(name:str):
#	print(f"hello {name}")

if __name__ == "__main__":
	app()

