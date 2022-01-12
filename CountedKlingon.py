# terbilang utk bahasa Klingon (versi ringkas)

def terbilang(n):
    if n < 0:
        raise ValueError
    if n < 10:
        return [
            'pagh', "wa'", "cha'", "wej",
            'loS', 'vagh', 'jav', 'Soch',
            'chorgh', 'Hut',
        ][n]
    digit = len(str(n))
    divider = pow(10, digit - 1)
    head = n // divider
    tail = n % divider
    suffix = {
        2: 'maH',
        3: 'vatlh',
        4: 'SaD',
        5: 'netlh',
        6: 'bIp',
        7: "'uy'",
    }.get(digit, None)
    if suffix is None:
        raise ValueError
    return terbilang(head) + suffix + (
        f' {terbilang(tail)}' if tail else ''
    )

print(terbilang(753))