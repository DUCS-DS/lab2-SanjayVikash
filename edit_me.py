

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
            return True
    
    if non_increasing == False and non_decreasing == False:
        non_decreasing = True
        non_decreasing = True
    return non_increasing and non_decreasing
            



num = [1,2,3,4,2,6,7] #monotonic
num1= [1] #not list 
num2 = [1,2,3,4,4,5,6,7] #not monotonic
num3 = [5,4,3,2,1] # monotonic
num4 = [5,4,3,4,5] # not monotonic 
print(monotonic(num))
print(monotonic(num1))
print(monotonic(num2))
print(monotonic(num3))
print(monotonic(num4))