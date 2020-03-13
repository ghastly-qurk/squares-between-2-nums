#This is a comment
#Comments help you to understand my code

#Program to prints the squares of numbers
#between 1 and a user-specified number
#as a dictionary

#num ----> Stores a number

#Function to write num and all numbers before it as keys
#and their squares as values
def dictSquare(num):

    #Stores {num: num^2} for num and every number before it
    #using dictionary comprehension
    square_dict = {k: k**2 for k in range(1, num+1)}

    #Return the dictionary
    return square_dict

#Main function
def main():

    #Loop forever
    while True:

        #Tried first
        try:
            
            #Ask num input from user
            num = int(input('Please enter the last number: '))

            #If num is less than 1
            if num < 1:

                #Print a helpful message
                print('\nPlease enter an integer greater than or equal to 1\n')

                #Return to start of loop
                continue

        #Tried if previous block of code finds ValueError
        except ValueError:

            #Print a helpful message
            print('\nPlease enter an integer\n')

        #Executed if no errors were found
        else:

            #Break out of loop
            break

    #Print an empty line
    print('')

    #Print the dictionary
    print(dictSquare(num))
    
#If program is started as main process
#instead of being imported
if __name__ == '__main__':

    #Execute the main function
    main()
