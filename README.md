# bitcalc

bitcalc is a command-line tool for converting an amount between
different Bitcoin units and fiat currencies.

## Installation

Current installation method requires setuptools.
This should install to the users local path in home directory.

```
 git clone https://github.com/matthewbotti/bitcalc
 
 cd bitcalc

 python3 setup.py install --user
```

## Usage

bitcalc takes three arguments with the first being a 
numerical amount to be converted, the starting unit type, 
and the end unit type. The `-r` or `--raw_output` option
can be used to display output value without commas or
unit codes.

``` 
 bitcalc START_AMT START_UNIT END_UNIT
 bitcalc -r START_AMT START_UNIT END_UNIT
```

Availabe Bitcoin units for conversion: BTC, mBTC, uBTC, sat, msat

Availabe Fiat units for conversion: USD

*NOTE: units are case-insensitve*

### Example Usage

```
 bitcalc 0.000125 btc sat
 12,500.0 sat

 bitcalc 55000 sat usd
 5.10 USD 

 bitcalc 20 usd btc
 0.0022 BTC

 bitcalc -r 6.15 btc usd
 64931.11
```

## TODO:

* Add error message when can't retrieve price api
* Handle formatting for exponentail notation output 
* Add support for multiple fiat currencies

