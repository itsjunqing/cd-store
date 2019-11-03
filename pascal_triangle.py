# Define print_pascal() that takes in a list and a number as input
def print_pascal(alist, n):
    
    # Base case is when n = 0
    # when n is 0, it will append 1 to the empty list and prints out the list
    # the recursion will stop here
    if n == 0:
        alist.append(1)
        print(*alist)

    else:
        # Recursively call back the print_pascal() function with arguments of empty list and n-1
        
        print_pascal(alist, n-1)

        # When the print_pascal() has returned, create an empty list called 'line'
        line = []

        # Duplicating the alist to the 'line'
        # Eg: if alist = [1,2,1] it will append until line = [1,2,1]
        for j in alist:
            line.append(j)

        # Iterating every item in 'line' starting from index 1
        # Eg: if line = [1,2,1], so it will be "for i in range*1,3)"
        for i in range(1, len(line)):
            # Eg: for the first iteration: alist[1] = line[1] + line[1-1]
            # therefore, the value of alist at index1 will be replaced by sum of line[1] and line[0]
            # resulting in alist = [1,3,1]
            alist[i] = line[i] + line[i-1]

        # once the looping has completed, it will append the last number 1 and prints out the list accordingly
        alist.append(1)
        print(*alist)


alist = []
while True:
    # Asks user to enter a number
    n = int(input("Enter a number: "))

    # if the number given is negative, it will ask the user to re-enter again
    if n < 0:
        print("Please enter numbers from 0 onwards")
    else:
        break

print_pascal(alist, n)


