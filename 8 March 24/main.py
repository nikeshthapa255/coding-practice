def get_date_diff(d1: str, d2: str) -> int:
    import datetime
    d1 = datetime.datetime.strptime(d1, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(d2, '%Y-%m-%d')
    return abs((d1 - d2).days)

assert get_date_diff('2024-06-29', '2024-06-26') == 3
assert get_date_diff('2024-06-26', '2024-06-29') == 3
print(get_date_diff("2020-01-15", "2019-12-31"))


def odd_even(value: str)-> str:
    return ''.join(
        [
            ch.upper() if idx%2 == 0 else ch.lower() 
            for idx, ch  in enumerate(value)
            ]
            )

assert odd_even('nikesh') == 'NiKeSh'