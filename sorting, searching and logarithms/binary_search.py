
def binary_search(numbers,target):

    left = 0
    right = len(numbers)-1

    while left <= right:
        middle = left + (right-left)//2
        #middle =  (right+left)//2 variant
        if (numbers[middle]==target):
            return target
        
        elif (numbers[middle]<target):

            left = middle + 1

        elif(numbers[middle]>target):
            right = middle - 1

    return "number not found"

print(binary_search([1,2,3,4,5,6,7,8,9,10,33,44,555],44))