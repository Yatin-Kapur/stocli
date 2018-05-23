# Candle
Command line tool to show candlestick-esque tickers for stocks

## Installation
```
$ cd /usr/local/bin
$ curl https://raw.githubusercontent.com/Yatin-Kapur/stocli/master/candle > candle
$ chmod +x candle
```

## Running

Displaying all charts from shortlist
```
$ candle
```

Displaying particular symbol (ex. aapl)
```
$ candle -s aapl
```

Specifying data granularity (default at 300 seconds)
```
$ candle -s aapl -i 60
```

Adding to shortlist
```
$ candle -a aapl
```

Deleting from shortlist
```
$ candle -d aapl
```

Clearing entire shortlist
```
$ candle -c
```

Data from googlefinance

## TODO:
* add x axis
