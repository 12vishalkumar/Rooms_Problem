# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
rooms = map(int, input().split())
s_rooms = sorted(rooms)
for i in range(len(s_rooms)):
    if(i != len(s_rooms)-1):
        if(s_rooms[i] != s_rooms[i-1] and s_rooms[i] != s_rooms[i+1]):
            print(s_rooms[i])
            break
    else:
        print(s_rooms[i])