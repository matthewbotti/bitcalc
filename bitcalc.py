import requests
import click

FIAT_CHOICES = ['USD']
UNITS = {'BTC':1, 'mBTC':0.001, 'uBTC':0.000001, 'sat':0.00000001, 'msat':0.00000000001}

# Fetch current Bitcoin price from Coindesk api
def get_btc_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    try:
        response.raise_for_status()
    except Exception as exc:
        print(f'Could not retreive Bitcoin price information:\n{exc}')        
        exit()
    price_data = response.json()

    return price_data['bpi']['USD']['rate_float']


@click.command()
@click.option('--raw_output', '-r', is_flag=True, help='Give output without commas or unit codes')
@click.argument('start_amt', type=float)
@click.argument('start_unit', type=click.Choice(list(UNITS.keys())+FIAT_CHOICES, case_sensitive=False))
@click.argument('end_unit', type=click.Choice(list(UNITS.keys())+FIAT_CHOICES, case_sensitive=False))
def cli(raw_output, start_amt, start_unit, end_unit):
    """Convert start_amt between different Bitcoin & fiat unit types"""

    # convert from a bitcoin unit to a fiat unit
    if end_unit in FIAT_CHOICES:
        end_amt = start_amt * UNITS[start_unit] * get_btc_price()    
        if raw_output:
            click.echo(end_amt)
        else:
            click.echo(f'{end_amt:,.2f} {end_unit}')

    # convert from a fiat unit to a bitcoin unit
    elif start_unit in FIAT_CHOICES:
        end_amt = start_amt / get_btc_price() / UNITS[end_unit] 
        if raw_output:
            click.echo(end_amt)
        else:
            click.echo(f'{end_amt:,.4f} {end_unit}')

    # convert from one bitcoin unit to another bitcoin unit
    else:
        end_amt = (UNITS[start_unit] / UNITS[end_unit]) * start_amt
        if raw_output:
            click.echo(end_amt)
        else:
            click.echo(f'{end_amt:,} {end_unit}')    


if __name__ == '__main__':
    cli()
