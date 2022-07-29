"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Notify."""


if __name__ == "__main__":
    main(prog_name="notify")  # pragma: no cover
