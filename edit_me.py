

def monotonic(lst):

    if not list:
        return True

    non_increasing = True
    non_decreasing = True

    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            non_increasing = False
        if lst[i] < lst[i-1]:
            non_decreasing = False
        if lst[i] == lst[i-1]:
            pass
    
    if non_increasing == False and non_decreasing == False:
        non_decreasing = True
        non_increasing = True
    return ((non_increasing and non_decreasing) or (not(non_increasing) and not(non_decreasing)))
            

# False = monotonic, True = not monotonic 

num = [1,2,3,4,5,6,7]# monotonic
num1= [1] #not list 
num2 = [1,2,3,4,4,5,6,7] # monotonic
num3 = [5,4,3,2,1] # monotonic
num4 = [5,4,3,4,5] # not monotonic 
num5 = [1,1,1,1,1,3,3,3,3,5,5,5,5,6,6,6,6]
print(monotonic(num))
print(monotonic(num1))
print(monotonic(num2))
print(monotonic(num3))
print(monotonic(num4))
print(monotonic(num5))

