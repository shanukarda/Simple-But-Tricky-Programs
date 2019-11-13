if __name__ == '__main__':
    total_mks = {}
    for i in range(int(input())):
        x = input().split()
        st_name,marks = x[0], x[1:]
        marks = map(float,marks)
        marks = sum(marks)/3
        total_mks[st_name]=marks
    d = input()
    print("{0:.2f}".format(total_mks[d]))