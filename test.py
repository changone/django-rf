# coding: utf-8

import requests


class A():
    pass


class B(A):
    pass


class C(B):
    pass


def test():
    c = C()
    print(isinstance(c, A))


def testt():
    params = {
        "date_start": "2018-10-01",
        "date_end": "2018-10-15",
        "limit": 20,
        "log_name": "",
        "page": 1,
        "project_name": "",
        "max_slow_exe": [20, 50],
        "min_slow_exe": [0, 10],
        "avg_slow_query": [0, 20],
        "slow_query_amount": [10, 30],
        "total_query_amount": [10, 30],
        "slow_query_ratio": [10, 30],
        "sort_type": 1
    }

    res = requests.get(' http://127.0.0.1:8000/api/invoice_balance', params=params, headers={"accesstoken": "8207ufxy5biap48sl8fb5aoj3g6bhip8"})
    print(res)

def testpandas():
    import pandas as pd
    df = pd.DataFrame({'a': [1, 3, 5, 7, 4, 5, 6, 4, 7, 8, 9],
                       'b': [3, 5, 6, 2, 4, 6, 7, 8, 7, 8, 9]})


if __name__ == '__main__':
    testt()
