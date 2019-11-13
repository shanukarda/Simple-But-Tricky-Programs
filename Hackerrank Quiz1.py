'''Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given scores. 
Store them in a list and find the score of the runner-up.'''

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a = max(arr)
    i=0
    while i<n:
        if a == max(arr):
            arr.remove(max(arr))
        i+=1
    print(max(arr))