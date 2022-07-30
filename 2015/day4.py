from hashlib import md5

secret = "bgvyzdsv"
five, six = 0, 0
for i in range(10**9):
  if md5(bytes(f"bgvyzdsv{i}", "utf8")).hexdigest()[:5] == "00000":
    five = i
    break
for i in range(10**9):
  if md5(bytes(f"bgvyzdsv{i}", "utf8")).hexdigest()[:6] == "000000":
    six = i
    break

print(five, six)
