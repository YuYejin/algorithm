# total = list(input().split())
# m_lst = total[:2]
# t_lst = total[2:]

ML, MR, TL, TR = ('SPR'.index(i) for i in input().split())

if ML == MR and (ML+2)%3 in [TL, TR]: #TK가 이기는 패
    print("TK")
elif TL == TR and (TL+2)%3 in [ML, MR]: #MS가 이기는 패
    print("MS")
else:
    print('?')