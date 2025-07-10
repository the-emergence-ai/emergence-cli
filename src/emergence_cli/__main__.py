import click
from . import __version__

@click.group()
@click.version_option(__version__)
def cli():
    """Emergence command-line tool."""
    pass

if __name__ == "__main__":  # pragma: no cover
    cli()