import click
from spotify import sp


@click.command()
@click.argument("song")
def play(song):
    click.echo(f"playing {song}")
