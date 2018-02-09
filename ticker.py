import numpy as np
import argparse
import datetime
import urllib.request


def get_data(symbol):
    url = "http://finance.google.com/finance/getprices?q={0}".format(symbol)
    url += "&i=300&p=1d&f=o,h,l,c"
    csv = urllib.request.urlopen(url).readlines()

    # removing title headers and adding it to dataframe
    csv = np.asarray(csv[7:])
    data = []
    for entry in csv:
        add = entry.decode('utf8').split(',')
        data.append(add)

    for entry in data:
        for i in range(len(entry)):
            entry[i] = float(entry[i])
    return data


def get_y(data):
    top = 0
    bottom = 999999999
    for i in data:
        if i[1] < bottom:
            bottom = i[1]
        if i[2] < bottom:
            bottom = i[2]
        if i[1] > top:
            top = i[1]
        if i[2] > top:
            top = i[2]

    return top, bottom


def plot_it(symbol):
    data = get_data(symbol)
    top, bottom = get_y(data)
    yaxis = np.linspace(top, bottom, 30)
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CEND = '\033[0m'
    # close high low open
    for entry in yaxis:
        outstring = '' + str(round(entry, 1)) + ' '
        for price in data:
            if price[0] > price[3]:
                c = CGREEN + 'o' + CEND
                top = price[0]
                bot = price[3]
            else:
                c = CRED + 'o' + CEND
                top = price[3]
                bot = price[0]

            if entry > price[1]:
                outstring += ' '
            elif price[1] <= entry:
                outstring += '|'
            elif entry <= top and entry >= bot:
                outstring += c
            elif price[2] <= entry:
                outstring += '|'
            else:
                outstring += " "
        print(outstring)


def main():
    parser = argparse.ArgumentParser(description='input symbol')
    parser.add_argument('-s', help='use to input the symbol for ticker')

    args = vars(parser.parse_args())
    symbol = args['s'].upper()
    CYELLOW = '\33[33m'
    CEND = '\033[0m'
    now = datetime.datetime.now()
    print(CYELLOW + symbol + CEND + " for " + now.strftime("%Y-%m-%d"))
    plot_it(symbol)


if __name__ == "__main__":
    main()
