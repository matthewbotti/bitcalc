import requests
import click


# Fetch current Bitcoin price from Coindesk api
def get_btc_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    price_data = response.json()
    return price_data['bpi']['USD']['rate_float']


@click.command()
def cli():
    """Displays current price of Bitcoin."""

    btc_price = get_btc_price()

    click.echo('Hello Sathoshi!')
    click.echo(f'Current BTC Price: ${btc_price:,.2f}')
