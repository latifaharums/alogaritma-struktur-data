# terbilang utk bahasa Klingon (versi panjang)

def terbilang(n):
    if n < 0:
        raise ValueError
    if n < 10:
        return [
            'pagh', "wa'", "cha'", "wej",
            'loS', 'vagh', 'jav', 'Soch',
            'chorgh', 'Hut',
        ][n]
    if n < 100:
        head = n // 10
        tail = n % 10
        return terbilang(head) + 'maH' + (
            f' {terbilang(tail)}' if tail else ''
        )
    if n < 1000:
        head = n // 100
        tail = n % 100
        return terbilang(head) + 'vatlh' + (
            f' {terbilang(tail)}' if tail else ''
        )
    if n < 10000:
        head = n // 1000
        tail = n % 1000
        return terbilang(head) + 'SaD' + (
            f' {terbilang(tail)}' if tail else ''
        )
    if n < 100000:
        head = n // 10000
        tail = n % 10000
        return terbilang(head) + 'netlh' + (
            f' {terbilang(tail)}' if tail else ''
        )
    if n < 1000000:
        head = n // 100000
        tail = n % 100000
        return terbilang(head) + 'bIp' + (
            f' {terbilang(tail)}' if tail else ''
        )
    if n < 10000000:
        head = n // 1000000
        tail = n % 1000000
        return terbilang(head) + "'uy'" + (
            f' {terbilang(tail)}' if tail else ''
        )
    raise ValueError

print(terbilang(753))