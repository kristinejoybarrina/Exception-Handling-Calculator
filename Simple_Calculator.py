# Kristine Joy P. Barrina #BSCPE 1-5
# Creating a simple calculator program that uses exception handling to show error inputs.

# PSEUDOCODE

# Create a working simple calculator function that will serve as the basis only for creating functions inside tkinter

#    Ask the user what operation he/she would like to use
print ("Select an operation. Type number only. \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")

operation_input = int(input("Select operator: "))
    
# Let the user input the first input
first_input = int(input("Enter first input: "))

# Let the user input the second input
second_input = int(input("Enter second input: "))

# Add if-else for each operation
if operation_input == 1:
    sum = (first_input + second_input)
    print (sum)
    
else:
    ("okay")

    # Display error message if the user entered a string
    # Display an error message if the user inputs a zero in 2nd input
    # Display output considering the operation that the user chose
    # Ask the user if he/she wants to try again
    
# Based on the created simple calculator program, create a GUI using tkinter
# Define a function called First_Window
# Add labels and buttons to First_Window
# Define functions for each operator
# Add labels, button, and text box to each function
# Ask user for 1st input
# Ask user for 2nd input
# Apply the operation to the inputs
# Display output
# Display error message