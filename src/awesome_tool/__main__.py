import sys
import click
from . import __version__
from .config import load_config
from .services import greet

@click.command()
@click.option("--name", default="World", help="Name to greet")
@click.version_option(version=__version__)
def main(name: str) -> None:
    """Entry‑point for the awesome_tool CLI.

    It loads configuration (if any) and prints a friendly greeting.
    """
    cfg = load_config()
    # cfg could be used to customise behaviour; kept simple here
    click.echo(greet(name))

if __name__ == "__main__":
    # Let click handle CLI parsing
    main()
