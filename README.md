# bitcalc

bitcalc is a command-line tool for converting an amount between
different Bitcoin units and fiat currencies.

## Usage

bitcalc takes three arguments with the first being a 
numerical amount to be converted, the starting unit type, 
and the end unit type.

``` 
 bitcalc START_AMT START_UNIT END_UNIT
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
```

## TODO:

* Handle formatting for exponentail notation output 
* Add support for multiple fiat currencies
* Add support for multiple end unit output

