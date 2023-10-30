import pandas as pd


def filterNa(seriesA: pd.Series, seriesB: pd.Series):
    bad = ~(seriesA.isnull() | seriesB.isnull ())
    n1 = seriesA[bad]
    n2 = seriesB[bad]
    return (n1, n2)

def visualizeTheData(seriesA: pd.Series, seriesB: pd.Series):
    (n1,n2) = filterNa(seriesA, seriesB)

    print(pd.DataFrame({
        'user 1': n1,
        'user 2': n2
    }).to_string())