import numpy as np
from math import sqrt
from sklearn.preprocessing import normalize
import json


def Pearson(data1, data2):
    data = np.array([data1, data2])
    nd = normalize(data)
    len = nd[0].size

    Sxy, Sx, Sy, Sx2, Sy2 = 0.0, 0.0, 0.0, 0.0, 0.0

    for i in range(len):
        Sxy += nd[0][i] * nd[1][i]
        Sx += nd[0][i]
        Sy += nd[1][i]
        Sx2 += nd[0][i] * nd[0][i]
        Sy2 += nd[1][i] * nd[1][i]

    try:
        p = (len * Sxy - Sx * Sy + 0.0) / (sqrt(len*Sx2 - Sx*Sx) * sqrt(len*Sy2 - Sy*Sy))
    except ZeroDivisionError:
        p = 0.0
    finally:
        return p


def readPrice(filepath):
    data = []
    with open(filepath, 'rb') as f:
        prices = json.load(f)
        for p in prices:
            data.append(p[0])
    return data


def readCommit(filepath):
    data = []
    with open(filepath, 'rb') as f:
        commits = json.load(f)
        for c in commits:
            data += c['days']
    return data[-276:]


def allPearson():
    results = {}
    # BTC
    prices = readPrice('./data/BTCUSDT')
    commits = readCommit('./data/BTCgithub')
    p = Pearson(prices, commits)
    results['BTC'] = [prices, commits, p]

    # EOS
    prices = readPrice('./data/EOSUSDT')
    commits = readCommit('./data/EOSgithub')
    p = Pearson(prices, commits)
    results['EOS'] = [prices, commits, p]

    # ETH
    prices = readPrice('./data/ETHUSDT')
    commits = readCommit('./data/ETHgithub')
    p = Pearson(prices, commits)
    results['ETH'] = [prices, commits, p]

    return results


if __name__ == '__main__':
    # call allPearson
    results = allPearson()
    print(results['BTC'][2])
    print(results['EOS'][2])
    print(results['ETH'][2])
