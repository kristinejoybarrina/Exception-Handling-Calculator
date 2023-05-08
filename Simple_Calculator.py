# Kristine Joy P. Barrina #BSCPE 1-5
# Creating a simple calculator program that uses exception handling to show error inputs.

# PSEUDOCODE

# Create a working simple calculator function that will serve as the basis only for creating functions inside tkinter
from tkinter import *

# Initialize Variables
user_loop_response = "y"

while user_loop_response == "y":
    
    try:

    #    Ask the user what operation he/she would like to use
        print ("Select an operation. Type number only. \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")

        operation_input = int(input("Select operator: "))
            
        # Let the user input the first input
        first_input = int(input("Enter first input: "))

        # Let the user input the second input
        second_input = int(input("Enter second input: "))

        # Addition operation
        if operation_input == 1:
            sum = (first_input + second_input)
            
        #   Display output considering the operation that the user chose
            print (sum)
            
        # Subtraction operation
        elif operation_input == 2:
            difference = (first_input - second_input)
            print (difference)
            
        # Multiplication operation
        elif operation_input == 3:
            product = (first_input * second_input)
            print (product)

        else:
            quotient = (first_input / second_input)
            print (quotient)
            
        # Ask the user if he/she wants to try again
        user_loop_response = str(input("Do you want to try again? y/n: ")).lower()

    # Display error message if the user entered a string
    except ValueError:
        user_loop_response = "y"
        print ("Enter an integer!")


    # Display an error message if the user inputs a zero in 2nd input

    except ZeroDivisionError:
        user_loop_response = "y"
        print ("The second input must not be equal to zero! Please try again.")
        
print ("Thank you")

# Based on the created simple calculator program, create a GUI using tkinter

# Define a function called First_Window
def First_Window():
    
    # Define function and create window for addition operation 
    def Addition():
        addition_window = Tk()
        addition_window.title("Addition")
        addition_window.geometry("450x200")
        addition_window.config(bg="gray")
        
        # Create label for first input
        first_input_label = Label(addition_window, text="First input:", fg="black", bg="gray", font=("Arial", 12, "bold"))
        first_input_label.grid(row=1, column=5, pady=15)
        
        # Create label for second input
        second_input_label = Label(addition_window, text="Second input:", fg="black", bg="gray", font=("Arial", 12, "bold"))
        second_input_label.grid(row=2, column=5, pady=15)
        
        # Create textbox for first input
        first_input_textbox = Entry(addition_window, fg="black", font=("Arial", 12, "bold"))
        first_input_textbox.grid(row=1, column=20)
        
        # Create textbox for second input
        second_input_textbox = Entry(addition_window, fg="black", font=("Arial", 12, "bold"))
        second_input_textbox.grid(row=2, column=20)
        
        # Define function to apply addition operation
        def sum():
            
            # Use try-catch to show error inputs
            try:
                
                total = (int(first_input_textbox.get()) + int(second_input_textbox.get()))
                empty_label.config(fg="black", text="Total: " + str(total))
                
            except ValueError:
                empty_label.config(text="Please enter an integer!", fg="red") 
        
        # Create calculate button
        calculate_button = Button(addition_window, command=sum, text="Calculate", fg="black", font=("Arial", 12, "bold"))
        calculate_button.grid(row=5, column=20, sticky=W)
        
        # Create empty label to show total 
        empty_label = Label(addition_window, fg="black", bg="gray", font=("Arial", 12, "bold"))
        empty_label.grid(row=15, column=20, sticky=W)
        
        # Create back button
        back_button = Button(addition_window, text="Back", bg="red", fg="white", command=addition_window.destroy)
        back_button.grid(row=5, column=50, sticky=W)
        
        addition_window.mainloop()
        
    # Define function and create window for addition operation 
    def Subtraction():
        subtraction_window = Tk()
        subtraction_window.title("Subtraction")
        subtraction_window.geometry("450x200")
        subtraction_window.config(bg="gray")
        
        # Create label for first input
        first_input_label = Label(subtraction_window, text="First input:", fg="black", bg="gray", font=("Arial", 12, "bold"))
        first_input_label.grid(row=1, column=5, pady=15)
        
        # Create label for second input
        second_input_label = Label(subtraction_window, text="Second input:", fg="black", bg="gray", font=("Arial", 12, "bold"))
        second_input_label.grid(row=2, column=5, pady=15)
        
        # Create textbox for first input
        first_input_textbox = Entry(subtraction_window, fg="black", font=("Arial", 12, "bold"))
        first_input_textbox.grid(row=1, column=20)
        
        # Create textbox for second input
        second_input_textbox = Entry(subtraction_window, fg="black", font=("Arial", 12, "bold"))
        second_input_textbox.grid(row=2, column=20)
        
        # Define function to apply addition operation
        def difference():
            
            # Use try-catch to show error inputs
            try:
                
                total = (int(first_input_textbox.get()) - int(second_input_textbox.get()))
                empty_label.config(fg="black", text="Total: " + str(total))
                
            except ValueError:
                empty_label.config(text="Please enter an integer!", fg="red") 
        
        # Create calculate button
        calculate_button = Button(subtraction_window, command=difference, text="Calculate", fg="black", font=("Arial", 12, "bold"))
        calculate_button.grid(row=5, column=20, sticky=W)
        
        # Create empty label to show total 
        empty_label = Label(subtraction_window, fg="black", bg="gray", font=("Arial", 12, "bold"))
        empty_label.grid(row=15, column=20, sticky=W)
        
        # Create back button
        back_button = Button(subtraction_window, text="Back", bg="red", fg="white", command=subtraction_window.destroy)
        back_button.grid(row=5, column=50, sticky=W)
        
        subtraction_window.mainloop()

    # Create a window

    root = Tk()
    root.geometry("450x200")
    root.configure(bg="gray")
    root.title("Calculator")

    # Create label for direction
    direction_label = Label(root, text="Select an operation", bg="gray", fg="black", font=("Arial", 16, "bold"))
    direction_label.pack()

    # Create close button
    close_button = Button(root, text="Close", bg="red", fg="white", command=root.destroy)
    close_button.pack(side="bottom")

    # Create addition operation button
    addition_button = Button(root, text="Addition", bg="black", fg="white", command=Addition)
    addition_button.pack()
    
    # Create addition operation button
    addition_button = Button(root, text="Subtraction", bg="black", fg="white", command=Subtraction)
    addition_button.pack()


    root.mainloop()

First_Window()