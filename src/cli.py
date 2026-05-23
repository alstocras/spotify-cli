import click
from commands.play import play
from commands.pause import pause


@click.group()
def cli():
    pass


cli.add_command(play)
cli.add_command(pause)


if __name__ == "__main__":
    cli()
