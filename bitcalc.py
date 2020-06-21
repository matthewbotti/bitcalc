import requests
import click

UNIT_CHOICES=['BTC', 'mBTC', 'uBTC', 'SAT', 'mSAT']

# Fetch current Bitcoin price from Coindesk api
def btc_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    price_data = response.json()

    return price_data['bpi']['USD']['rate_float']


@click.command()
@click.argument('amount', type=float)
@click.argument('start_unit', type=click.Choice(UNIT_CHOICES, case_sensitive=False))
@click.argument('end_unit', type=click.Choice(UNIT_CHOICES, case_sensitive=False))
def cli(amount, start_unit, end_unit):
    """Convert amount between different Bitcoin unit types"""

    click.echo('Hello Sathoshi!')
    click.echo(f'{amount} {start_unit} {end_unit}')
