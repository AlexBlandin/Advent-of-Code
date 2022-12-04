from pathlib import Path

print(sum(map(lambda job: (job[0] <= job[2] <= job[1] and job[0] <= job[3] <= job[1]) or (job[2] <= job[0] <= job[3] and job[2] <= job[1] <= job[3]), jobs := list(map(lambda line: tuple(map(int, line.split(","))), Path("day4.txt").read_text().replace("-",",").splitlines())))), sum(map(lambda job: job[0] <= job[2] <= job[1] or job[0] <= job[3] <= job[1] or job[2] <= job[0] <= job[3] or job[2] <= job[1] <= job[3], jobs)))
