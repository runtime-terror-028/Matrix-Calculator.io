"""
1. This is a matrix calculator. Just solve your matrix problems in 3 easy steps:-

    optional step: Enter the formula in which you want to solve those matrix Q.s
    step 1: Enter the order of that matrix
    step 2: Enter the elements of that matrix
    step 3: Enter the operation you want to perform on that matrices

2. All the operations are there in the form of M in MatrixOperation class.
3. The code for that MatrixOperation class is there in a different python file and
    here that class is imported using static import.
"""

"""
Edit by runtime-terror-028

-- This is the entry point "main.py"
-- all the operation logic is tranfered to "src/matrix_operation.py"
"""

import argparse
import src.clac_methods as M
from termcolor import cprint
import src.matrix_operations as matrix_operations

# Decides if the program will start with GUI or CLI
gui_mode = False

# menu of operations available in the calc. for user
MENU = """
\t\tMENU\n
\t1. Addition
\t2. Subtraction
\t3. Multiplication (not working)
\t4. Scalar Multiplication
\t5. Find Transpose
\t6. Find Determinant\n
"""

# renders first when program starts
def drawLine(len=int()):
    print("-" * len, end="")
    print("")
    print("-" * len, end="")

# ask user for operation
def userChooseOperation():
    return input("Choose a Operation:- ").lower()

# decide if the program will run using gui or cli depending on user command argument
def isGuiEnabled():
    parser = argparse.ArgumentParser(description="Process command-line arguments.") 
    # Add --gui argument 
    parser.add_argument('--gui', action='store_true', help="Enable GUI mode")
    # Parse the arguments
    args = parser.parse_args()

    global gui_mode
    gui_mode = args.gui


def main():

    # there are multiple "if not" instead of one because when we want
    # to add a gui later we would only have to add else statment without much change here

    if not gui_mode:
        # draw some lines
        drawLine(len=50)
        # print menu
        print(MENU)

    # get operation type from user
    if not gui_mode:
        user_choice = userChooseOperation()

    if not gui_mode:
        print("\n\t\t\t\t\t\t\tMAKE YOUR MATRICES");

    if user_choice == "1" or user_choice == "addition":
        matrix_operations.matrixAddition()

    elif user_choice == "2" or user_choice == "subtraction":
        matrix_operations.matrixSubstraction()

    elif user_choice == "3" or user_choice == "multiplication":
        matrix_operations.matrixMultiplication()

    elif user_choice == "4" or user_choice == "scalar multiplication":
        matrix_operations.matrixScalarMultiplication()

    elif user_choice == "5" or user_choice == "Find Transpose" or user_choice == "Transpose":
        matrix_operations.matrixFindTranspose()
    
    else:
        if not gui_mode:
            cprint("OutOfMenuError: No such option in menu.", color="red", attrs=["bold"])



if __name__ == "__main__":
    isGuiEnabled()
    main()
