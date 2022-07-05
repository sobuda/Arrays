def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    # star = ['*']*N*2
    # print(star)
    for i in range(N, -1, -1):
        if i < N and i != 0:
            print()
        for j in range(2 * N):
            # print(i,j)
            if i < N:
                if j >= i and j < (2 * N) - i:
                    print(' ', end='')
                else:
                    print('*', end='')
            else:
                print('*', end='')

    for i in range(N):
        print()
        for j in range(2 * N):
            # if i == 0 :
            # print(i,j,end='')
            if i < N:
                if j > i and j < (2 * N) - i - 1:
                    print(' ', end='')
                else:
                    print('*', end='')
            else:
                print('*', end='')

    return 0


if __name__ == '__main__':
    main()