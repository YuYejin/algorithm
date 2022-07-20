N, M = map(int, input().split())

team_mem, mem_team = {}, {}

for i in range(N):
    team_name, mem_num = input(), int(input())
    team_mem[team_name] = [] # team_mem 딕셔너리의 team_name key에 빈 리스트 value를 추가
    for j in range(mem_num):
        name = input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name

for i in range(M):
    name, q = input(), int(input())
    if q: # q가 1일 때 즉, 참일 때
        print(mem_team[name])
    else:
        for mem in sorted(team_mem[name]):
            print(mem)
