#Binary Search Algorithm For Lists In Python
def search(li: list, x: int):
     #Takes list and Target as Parameter
    middle_term = len(li) // 2 
    #gets the middle term
    while True: 
    #running loop until the item is found or list doesnot contains the item
        if li[middle_term] == x:
            return True
        # if the item in the middle is the target
        elif li[middle_term] < x: 
            # if the middle item is smaller than target
            li = li[middle_term + 1 :]
            #list cuts in half from the middle term to last
            middle_term = middle_term // 2
            #new middle term of the list is assigned according to new list
        else:
            #if middle term is greater than the target
            li = li[: middle_term]
            #list cuts in half from last to middle term
            middle_term = middle_term // 2
            #new middle term of the list is assigned according to new list
        if len(li) == 1 and li[0] != x:
            #if no further list can be checked then checking last time if it contains the target
            return False
            #returns false and breaks the loop


#test cases
a = [1, 3, 5, 7, 8, 9, 10]
print(
search(a, 10),
search(a, 3),
search(a, 8),
search(a, 55))
