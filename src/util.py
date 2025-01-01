import src.clac_methods as M
from main import gui_mode
from termcolor import cprint

#gets matrix dimention from user
def getMatrixDimention(counter):
    print(f"Matrix {counter}:-\n")
    rows = int(input("Enter the no. of rows:- "))
    cols = int(input("Enter the no. columns:- "))
    print()
    return rows, cols

#gets both matrix data from user
def getMatrixData():
    counterVar1 = 1  # counter value for while loop and matrix message

    while counterVar1 <= 2:
        rows, cols = getMatrixDimention(counterVar1)

        if counterVar1 == 1:
            mat1 = M.__formMatrix__(rows, cols)
            M.__printMatrix__(mat1)
            if not gui_mode:
                print()
        elif counterVar1 == 2:
            mat2 = M.__formMatrix__(rows, cols)
            M.__printMatrix__(mat2)
            if not gui_mode:
                print()

        counterVar1 += 1
    
    return mat1, mat2

# Check if the order are the same
def checkMatrixOrder(pom1, pom2):
    return True if pom1["order"] == pom2["order"] else False

# Error message saying order is not same
def orderNotSameErrorMessage():
    cprint(
    text="PropertyError: The order of Matrix1 and Matrix2 are not the same!!",
    color="red",
    attrs=["bold"],
    )
    print("\nThe order of both matrices must be the same to perform addition.")


# Get properties of matrices
def getMatrixProperties(mat1, mat2):
    POM1 = M.__getProperties__(matrix=mat1)
    POM2 = M.__getProperties__(matrix=mat2)
    return POM1, POM2
