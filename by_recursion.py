def search(li:list, x : int):
    middle_term = len(li)//2
    if len(li) == 1 and li[0] != x:
        print('no results')
    elif li[middle_term] < x:
        search(li[middle_term:], x)
    elif li[middle_term] > x:
        search(li[:middle_term], x)
    elif li[middle_term] == x:
        print('found')


a = [1,2,3,4,5,6,7,8,9]
while True:
    b = int(input('no '))
    search(a,b )
