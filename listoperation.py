if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        command, *line = input().split()
        if command == 'append':
            list.append(int(line[0]))
        elif command == 'remove':
            list.remove(int(line[0]))
        elif command == 'insert':
            list.insert(int(line[0]), int(line[1]))
        elif command == 'sort':
            list.sort()
        elif command == 'pop':
            list.pop()
        elif command == 'reverse':
            list.reverse()
        elif command == 'print':
            print(list)
