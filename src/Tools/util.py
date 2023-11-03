import pandas as pd

def filterNa(seriesA: pd.Series, seriesB: pd.Series):
    '''
    Take 2 serieses and return 2 serieses where both input had value in each index value
    '''
    bad = ~(seriesA.isnull() | seriesB.isnull ())
    n1 = seriesA[bad]
    n2 = seriesB[bad]
    return (n1, n2)

def visualizeTheData(seriesA: pd.Series, seriesB: pd.Series):
    '''
    Print 2 serieses with matching index values after filtering NaN
    '''
    (n1,n2) = filterNa(seriesA, seriesB)

    print(pd.DataFrame({
        'user 1': n1,
        'user 2': n2
    }).to_string())