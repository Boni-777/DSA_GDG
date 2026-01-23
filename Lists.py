if __name__ == '__main__':
    listt=[]
    N = int(input())
    for _ in range(N):
        command_line=input().split()
        command=command_line[0]
        if command=="insert":
            i=int(command_line[1])
            e=int(command_line[2])
            listt.insert(i,e)
        elif command=="print":
            print(listt)
        elif command=="remove":
            e=int(command_line[1])
            listt.remove(e)
        elif command=="append":
            e=int(command_line[1])
            listt.append(e)
        elif command=="sort":
            listt.sort()
        elif command=="pop":
            listt.pop()
        elif command=="reverse":
            listt.reverse()
