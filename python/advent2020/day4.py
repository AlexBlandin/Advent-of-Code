from pathlib import Path

print(
  len(
    [
      p
      for p in [
        eval('{"' + s.replace("\n", ",").replace(" ", ",").replace(":", '":"').replace(",", '","').strip() + '"}')
        for s in Path("day4.txt").read_text().strip().split("\n\n")
      ]
      if (len(p) == 8 or (len(p) == 7 and "cid" not in p))
    ]
  ),
  len(
    [
      p
      for p in [
        eval('{"' + s.replace("\n", ",").replace(" ", ",").replace(":", '":"').replace(",", '","').strip() + '"}')
        for s in Path("day4.txt").read_text().strip().split("\n\n")
      ]
      if (len(p) == 8 or (len(p) == 7 and "cid" not in p))
      and (1920 <= int(p["byr"]) <= 2002)
      and (2010 <= int(p["iyr"]) <= 2020)
      and (2020 <= int(p["eyr"]) <= 2030)
      and (
        len(p["hgt"]) > 2
        and ((150 <= int(p["hgt"][:-2]) <= 193) if p["hgt"][-2:] == "cm" else (59 <= int(p["hgt"][:-2]) <= 76))
      )
      and (len(p["hcl"]) == 7 and p["hcl"][0] == "#" and int(p["hcl"][1:], 16))
      and (p["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"})
      and (len(p["pid"]) == 9 and int(p["pid"]))
    ]
  ),
)
