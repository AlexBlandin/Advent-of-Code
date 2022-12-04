from pathlib import Path

print(sum(map(lambda job: (job[0][0] <= job[1][0] <= job[0][1] and job[0][0] <= job[1][1] <= job[0][1]) or (job[1][0] <= job[0][0] <= job[1][1] and job[1][0] <= job[0][1] <= job[1][1]), jobs := list(map(lambda line: tuple((map(lambda job: tuple(map(int, job)), line))), list(map(lambda l: list(map(lambda j: j.split("-"), l.split(","))), Path("day4.txt").read_text().splitlines())))))), sum(map(lambda job: job[0][0] <= job[1][0] <= job[0][1] or job[0][0] <= job[1][1] <= job[0][1] or job[1][0] <= job[0][0] <= job[1][1] or job[1][0] <= job[0][1] <= job[1][1], jobs)))
