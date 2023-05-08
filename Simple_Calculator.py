# Kristine Joy P. Barrina #BSCPE 1-5
# Creating a simple calculator program that uses exception handling to show error inputs.

# PSEUDOCODE

# Create simple calculator program using GUI tkinter

# import python module
from tkinter import *
import pyfiglet

# Create notice text that the program starts
notice_text = pyfiglet.figlet_format("Calculator", font="slant")
print("\033[1;31m" + notice_text)

# Define a function called First_Window
def first_window():
    
    # Define function and create window for addition operation 
    def addition():
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
                
                total = (float(first_input_textbox.get()) + float(second_input_textbox.get()))
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
        
    # Define function and create window for subtraction operation 
    def subtraction():
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
        
        # Define function to apply subtraction operation
        def difference():
            
            # Use try-catch to show error inputs
            try:
                
                total = (float(first_input_textbox.get()) - float(second_input_textbox.get()))
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
        
        
    # Define function and create window for multiplication operation 
    def multiplication():
        multiplication_window = Tk()
        multiplication_window.title("Multiplication")
        multiplication_window.geometry("450x200")
        multiplication_window.config(bg="gray")
        
        # Create label for first input
        first_input_label = Label(multiplication_window, text="First input:", fg="black", bg="gray", font=("Arial", 12, "bold"))
        first_input_label.grid(row=1, column=5, pady=15)
        
        # Create label for second input
        second_input_label = Label(multiplication_window, text="Second input:", fg="black", bg="gray", font=("Arial", 12, "bold"))
        second_input_label.grid(row=2, column=5, pady=15)
        
        # Create textbox for first input
        first_input_textbox = Entry(multiplication_window, fg="black", font=("Arial", 12, "bold"))
        first_input_textbox.grid(row=1, column=20)
        
        # Create textbox for second input
        second_input_textbox = Entry(multiplication_window, fg="black", font=("Arial", 12, "bold"))
        second_input_textbox.grid(row=2, column=20)
        
        # Define function to apply multiplication operation
        def product():
            
            # Use try-catch to show error inputs
            try:
                
                total = (float(first_input_textbox.get()) * float(second_input_textbox.get()))
                empty_label.config(fg="black", text="Total: " + str(total))
                
            except ValueError:
                empty_label.config(text="Please enter an integer!", fg="red") 
        
        # Create calculate button
        calculate_button = Button(multiplication_window, command=product, text="Calculate", fg="black", font=("Arial", 12, "bold"))
        calculate_button.grid(row=5, column=20, sticky=W)
        
        # Create empty label to show total 
        empty_label = Label(multiplication_window, fg="black", bg="gray", font=("Arial", 12, "bold"))
        empty_label.grid(row=15, column=20, sticky=W)
        
        # Create back button
        back_button = Button(multiplication_window, text="Back", bg="red", fg="white", command=multiplication_window.destroy)
        back_button.grid(row=5, column=50, sticky=W)
        
        multiplication_window.mainloop()

    # Define function and create window for division operation 
    def division():
        division_window = Tk()
        division_window.title("Division")
        division_window.geometry("450x200")
        division_window.config(bg="gray")
        
        # Create label for first input
        first_input_label = Label(division_window, text="First input:", fg="black", bg="gray", font=("Arial", 12, "bold"))
        first_input_label.grid(row=1, column=5, pady=15)
        
        # Create label for second input
        second_input_label = Label(division_window, text="Second input:", fg="black", bg="gray", font=("Arial", 12, "bold"))
        second_input_label.grid(row=2, column=5, pady=15)
        
        # Create textbox for first input
        first_input_textbox = Entry(division_window, fg="black", font=("Arial", 12, "bold"))
        first_input_textbox.grid(row=1, column=20)
        
        # Create textbox for second input
        second_input_textbox = Entry(division_window, fg="black", font=("Arial", 12, "bold"))
        second_input_textbox.grid(row=2, column=20)
        
        
        
        # Define function to apply division operation
        def quotient():
            
            # Use try-catch to show error inputs
            try:
                total = (float(first_input_textbox.get()) / float(second_input_textbox.get()))
                empty_label.config(fg="black", text="Total: " + str(total))
                
            except ValueError:
                empty_label.config(text="Please enter an integer!", fg="red") 
                
            except ZeroDivisionError:
                empty_label.config(text="Zero division error! \n Please try again.", fg="red") 
        
        # Create calculate button
        calculate_button = Button(division_window, command=quotient, text="Calculate", fg="black", font=("Arial", 12, "bold"))
        calculate_button.grid(row=5, column=20, sticky=W)
        
        # Create empty label to show total 
        empty_label = Label(division_window, fg="black", bg="gray", font=("Arial", 12, "bold"))
        empty_label.grid(row=15, column=20, sticky=W)
        
        # Create back button
        back_button = Button(division_window, text="Back", bg="red", fg="white", command=division_window.destroy)
        back_button.grid(row=5, column=50, sticky=W)
        
        division_window.mainloop()

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
    addition_button = Button(root, text="Addition", bg="black", fg="white", command=addition)
    addition_button.pack()
    
    # Create subtraction operation button
    subtraction_button = Button(root, text="Subtraction", bg="black", fg="white", command=subtraction)
    subtraction_button.pack()
    
    # Create multiplication operation button
    multiplication_button = Button(root, text="Multiplication", bg="black", fg="white", command=multiplication)
    multiplication_button.pack()

    # Create division operation button
    division_button = Button(root, text="Division", bg="black", fg="white", command=division)
    division_button.pack()

    root.mainloop()

first_window()