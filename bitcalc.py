import requests
import click

UNIT_CHOICES = ['BTC', 'mBTC', 'uBTC', 'SAT', 'mSAT']
UNITS = {'BTC':1, 'mBTC':0.001, 'uBTC':0.000001, 'SAT':0.00000001, 'mSAT':0.00000000001}

# Fetch current Bitcoin price from Coindesk api
def btc_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    price_data = response.json()

    return price_data['bpi']['USD']['rate_float']


@click.command()
@click.argument('start_amt', type=float)
@click.argument('start_unit', type=click.Choice(UNIT_CHOICES, case_sensitive=False))
@click.argument('end_unit', type=click.Choice(UNIT_CHOICES, case_sensitive=False))
def cli(start_amt, start_unit, end_unit):
    """Convert start_amt between different Bitcoin unit types"""

    end_amt = (UNITS[start_unit] / UNITS[end_unit]) * start_amt

    click.echo(f'{end_amt:,} {end_unit}')    
