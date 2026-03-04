# Standard library
import locale
from loguru import logger
from datetime import datetime

# Third party imports (need to be added to pyproject.toml)
import click


@click.command()
@click.option(
    "--name",
    default="Yufo",
    help="The person to greet.",
)
def hello(name: str) -> None:
    """Say hello to NAME."""
    locale.setlocale(locale.LC_TIME, "en_US.utf8")
    now = datetime.now()
    weekday = now.strftime("%A")
    day = now.day
    month = now.strftime("%B")
    year = now.year
    click.echo(f"Hello {name}! Today, we are {weekday} {day} {month} {year}.")
    logger.info("✅ Hello executed.")

if __name__ == "__main__":
    hello()
