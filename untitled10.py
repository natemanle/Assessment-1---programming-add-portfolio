#function to determine if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0: #uses mod to divide the number by 2, if it doesnt reach 0 its odd
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

# main function
def main():
    # ask the user for a number
    num = int(input("Enter a number: "))
    
    # pass the number to the function and get the result
    result = check_even_odd(num)
    
    # print the result message
    print(result)

#run the main function
if __name__ == "__main__":
    main()

