from src.calc_methods import determinant, scalar_multiply, transpose, add_matrices, subtract_matrices, multiply_matrices
from termcolor import colored

def matrix_cli():
    print(colored("Matrix Calculator (CLI Mode)\n", color="blue", attrs=["bold"]))
    print("----------------------------\n")

    operations = {
        "1": "Addition",
        "2": "Subtraction",
        "3": "Multiplication",
        "4": "Scalar Multiplication",
        "5": "Transpose",
        "6": "Determinant"
    }

    for key, op in operations.items():
        print(f"{key}. {op}")

    while True:
        choice = input("\nChoose an operation: ").strip()
        if choice in operations:
            break
        else:
            print(colored("\nInvalid choice. Please try again.", color="red"))

    if choice in ["4", "5", "6"]:
        rows, cols = get_matrix_dimensions()
        while True:
            matrix = get_matrix_input(rows, cols)
            if matrix is not None:
                break
        if choice == "4":
            scalar = float(input("\nEnter scalar value: "))
            result = scalar_multiply(matrix, scalar)
        elif choice == "5":
            result = transpose(matrix)
        elif choice == "6":
            result = determinant(matrix)
    else:
        rows, cols = get_matrix_dimensions()
        print(colored("\nMatrix 1:", color="yellow"))
        while True:
            matrix1 = get_matrix_input(rows, cols)
            if matrix1 is not None:
                break
        print(colored("\nMatrix 2:", color="yellow"))
        while True:
            matrix2 = get_matrix_input(rows, cols)
            if matrix2 is not None:
                break
        if choice == "1":
            result = add_matrices(matrix1, matrix2)
        elif choice == "2":
            result = subtract_matrices(matrix1, matrix2)
        elif choice == "3":
            result = multiply_matrices(matrix1, matrix2)

    print(colored("\nResult: ", color="green"))
    if isinstance(result, list):
        for row in result:
            print("  ".join(map(str, row)))
    else:
        print(result)

def get_matrix_input(rows, cols):
    print(f"\nEnter values for a {rows}x{cols} matrix: ")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Row {i + 1}: ").split()))
                if len(row) != cols:
                    print(colored(f"Each row must have exactly {cols} values. Please try again.\n", color="red"))
                    print(colored(f"Example if column is 3: 2 31 4\n", color="yellow"))
                else:
                    break
            except ValueError:
                print(colored("Invalid input. Please enter numeric values.\n", color="red"))
        matrix.append(row)
    return matrix


def get_matrix_dimensions():
    while True:
        try:
            rows = int(input("\nEnter number of rows: "))
            cols = int(input("\nEnter number of columns: "))
            return rows, cols
        except ValueError:
            print(colored("Invalid input. Please enter integers for rows and columns.\n", color="red"))

if __name__ == "__main__":
    matrix_cli()
