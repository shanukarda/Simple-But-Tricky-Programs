'''Given the names and grades for each student in a Physics class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the same grade, order their names alphabetically and
print each name on a new line.
'''

if __name__ == '__main__':
    arr = []
    sc = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr += [[name,score]]
        sc += [score]
    for i,j in sorted(arr):
        if j==sorted(list(set(sc)))[1]:
            print(i)