import click
from spotify import sp


@click.command()
def pause():
    click.echo(f"pausing")
