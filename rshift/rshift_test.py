import click
from toolz import curry
from rshift import Right


def first(ctx: dict) -> tuple:
    return True, "start first step"


@curry
def second(ctx: dict, new) -> tuple:
    return True, "start second step, --> add another parameter {new}".format(new=new)


def three(ctx: dict) -> tuple:
    if not ctx.get("second"):
        return False, "stop three step"
    return True, "start three step"


@click.command()
@click.option("--name", default="li", help="your name")
def hello_world(name):
    Right({"name": name}) >> first >> second(new="second") >> three


if __name__ == "__main__":
    hello_world()
