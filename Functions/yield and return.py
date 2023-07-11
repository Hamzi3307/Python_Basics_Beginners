# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time
def returnFunction():
    return 1
    return 2
    return 3

def yieldFunction():
	yield 1
	yield 2
	yield 3


# Driver code to check above generator function
def main():
    for value in yieldFunction():
	    print(value)

    #below will arise an error
    #for value in returnFunction():
    #    print(value)

if __name__ == '__main__': main()