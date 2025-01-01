import src.util as util
from main import gui_mode
import src.clac_methods as M



# Matrix addition
def matrixAddition():

    mat1, mat2 = util.getMatrixData()
    POM1, POM2 = util.getMatrixProperties(mat1, mat2)

    # Check if orders are the same before adding
    if util.checkMatrixOrder(POM1, POM2):
        #add the matrix
        matSum = M.add(matrix1=mat1, matrix2=mat2)
        if not gui_mode:  # TODO: add gui option later
            print("The SUM of your matrices is:- \n")
            M.__printMatrix__(matrix_2b_print=matSum)
    else:
        if not gui_mode:
            util.orderNotSameErrorMessage()

# Matrix substraction
def matrixSubstraction():
    mat1, mat2 = util.getMatrixData()
    POM1, POM2 = util.getMatrixProperties(mat1, mat2)

    # Check if orders are the same before adding
    if util.checkMatrixOrder(POM1, POM2):
        #substract the matrix
        matDifference = M.subtract(matrix1=mat1, matrix2=mat2)
        if not gui_mode:  # TODO: add gui option later
            print("The DIFFERENCE of your matrices is:- \n")
        M.__printMatrix__(matrix_2b_print=matDifference)
    else:
        if not gui_mode:
            util.orderNotSameErrorMessage()




def matrixScalarMultiplication():

    print(f"Matrix:-\n")
    rows = int(input("Enter the no. of rows:- "))
    cols = int(input("Enter the no. columns:- "))
    print()

    Mat = M.__formMatrix__(rows, cols)
    # print(matrix1)
    M.__printMatrix__(Mat)
    print()

    multiplyInt = int(
        input("Enter the integer you want to multiply with your matrix:- ")
    )

    scalarMat = M.scalar_multiply(integer=multiplyInt, matrix=Mat)
    M.__printMatrix__(scalarMat)

def matrixFindTranspose():
    print(f"Matrix:-\n")
    rows = int(input("Enter the no. of rows:- "))
    cols = int(input("Enter the no. columns:- "))
    print()

    Mat = M.__formMatrix__(rows, cols)
    # print(matrix1)
    M.__printMatrix__(Mat)
    print()

    transpose = M.__getTranspose__(matrix=Mat)
    M.__printMatrix__(transpose)

def matrixMultiplication():

    print("Sorry! The option is Out Of Order")


    """
            print('\n\t\t\t\t\t\t\tMAKE YOUR MATRICES')

            counterVar1 = 1  # counter value for while loop and matrix message

            while counterVar1 <= 2:

                print(f'Matrix {counterVar1}:-\n')
                rows = int(input('Enter the no. of rows:- '))
                cols = int(input('Enter the no. columns:- '))
                print()

                if counterVar1 == 1:

                    mat1 = M.__formMatrix__(rows, cols)
                    # print(matrix1)
                    M.__printMatrix__(mat1)
                    print()

                elif counterVar1 == 2:
                    mat2 = M.__formMatrix__(rows, cols)
                    # print(matrix2)
                    M.__printMatrix__(mat2)
                    print()

                counterVar1 += 1

            POM1 = M.__getProperties__(matrix=mat1)
            POM2 = M.__getProperties__(matrix=mat2)

            if POM1['cols'] == POM2['rows']:

                matProduct = M.multiply(matrix1=mat1, matrix2=mat2)
                print('The PRODUCT of your matrices is:- \n')
                M.__printMatrix__(matrix_2b_print=matProduct)

            else:
                cprint(text='PropertyError: The column of matrix1 != row of matrix2',
                       color='red',
                       attrs=['bold'])
                print('\nThe column/row of Matrix1 must be == row/column of Matrix2 respectively')
        """
