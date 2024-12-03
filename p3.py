import re
p = r"mul\((\d+),(\d+)\)"
c = r"(do\(\)|don't\(\))"
u8 = re.findall(f"{p}|{c}", input())
val = True
ans = 0
for i in u8:
    if i[2]: val = i[2] == "do()"
    elif i[0] and i[1]: ans += int(i[0]) * int(i[1]) * val
Auto.submit(ans)


