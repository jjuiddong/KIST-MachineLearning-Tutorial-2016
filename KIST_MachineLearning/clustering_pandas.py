import numpy as np
import pandas as pd


def main():
    do_exercise()


def do_exercise():
    # 1

    # 2
    aapl_bars = pd.read_csv("./AAPL.csv")

    # 3
    date_index = aapl_bars.pop('Date')
    aapl_bars.index = pd.to_datetime(date_index)

    # 4
    twoseries_dict = {'Open': aapl_bars.Open, 'Close': aapl_bars.Close, 'Volume': aapl_bars.Volume}
    df = pd.DataFrame(twoseries_dict)

    #5
    print(df[:]['2003-04' : '1989'])
    return df


if __name__ == "__main__":
    main()
