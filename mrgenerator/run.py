import click

from mrgenerator.generator import Generator

app = Generator()


@click.group()
def cli():
    """
    Markdown Generator - Server Documentation

    """
    pass


@cli.command('start')
@click.option('--name', '--n', type=str, default='README.md', help="Name of the file to be generated")
@click.option('--path', '--p', type=str, default=None, help="Path of the file to be generated")
def start(name, path):
    """
    build readme.md.

    """
    app.start(name, path)


@cli.command('create')
def create():
    """
    create build file readme.json.

    """
    app.create()


if __name__ == '__main__':
    cli()
