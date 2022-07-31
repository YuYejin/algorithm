S, tmp = input(), ""

ck = False # 괄호 안에 있는지 체크
ans = ""

for i in S:
    if i == ' ':
        if not ck:
            ans += tmp[::-1] + " "
            tmp=""
        else:
            ans += " "
    elif i == '<':
        ck = True
        ans += tmp[::-1] + "<"
        tmp=""
    elif i == '>':
        ck = False
        ans += ">"
    else:
        if ck:
            ans += i
        else:
            tmp += i

ans += tmp[::-1]

print(ans)