"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """RPA AS."""


if __name__ == "__main__":
    main(prog_name="RPA-Cookiecutter")  # pragma: no cover
