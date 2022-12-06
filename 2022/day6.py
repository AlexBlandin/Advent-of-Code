from pathlib import Path

print(next(filter(None, map(lambda a, b, c, d, i: i if len({a, b, c, d})==4 else None, data := Path("day6.txt").read_text(), data[1:], data[2:], data[3:], range(4, len(data))))), next(filter(None, map(lambda a, b, c, d, e, f, g, h, j, k, l, m, n, o, i: i if len({a, b, c, d, e, f, g, h, j, k, l, m, n, o})==14 else None, data, data[1:], data[2:], data[3:], data[4:], data[5:], data[6:], data[7:], data[8:], data[9:], data[10:], data[11:], data[12:], data[13:], range(14, len(data))))))
