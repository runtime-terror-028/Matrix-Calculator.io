import tkinter as tk
from functools import partial
from src.calc_methods import determinant, scalar_multiply, transpose, add_matrices, subtract_matrices, multiply_matrices

class GuiCalculater:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")
        self.main_menu()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Matrix Calculator", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Choose an operation:").pack()
        operations = ["addition", "subtraction", "multiplication", "scalar multiplication", "transpose", "determinant"]
        for op in operations:
            btn = tk.Button(self.root, text=op.capitalize(), command=partial(self.get_matrix_dimensions, op))
            btn.pack(pady=5)

    def get_matrix_dimensions(self, operation):
        self.clear_screen()
        if operation == "scalar multiplication":
            tk.Label(self.root, text="Enter dimensions for the matrix:").pack()
        elif operation == "determinant":
            tk.Label(self.root, text="Enter dimensions for the square matrix:").pack()
        else:
            tk.Label(self.root, text=f"Enter dimensions for the matrices ({operation}):").pack()

        row_label = tk.Label(self.root, text="Rows: ")
        row_label.pack()
        self.rows_entry = tk.Entry(self.root, width=5)
        self.rows_entry.pack()

        col_label = tk.Label(self.root, text="Columns: ")
        col_label.pack()
        self.cols_entry = tk.Entry(self.root, width=5)
        self.cols_entry.pack()

        submit_btn = tk.Button(self.root, text="Submit", command=lambda: self.input_matrices(operation))
        submit_btn.pack()

    def create_matrix_entry(self, rows, cols, label_text):
        tk.Label(self.root, text=label_text).pack()
        entries = []
        for i in range(rows):
            row_entries = []
            row_frame = tk.Frame(self.root)
            row_frame.pack()
            for j in range(cols):
                entry = tk.Entry(row_frame, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            entries.append(row_entries)
        return entries

    def input_matrices(self, operation):
        rows = int(self.rows_entry.get())
        cols = int(self.cols_entry.get())
        self.clear_screen()

        if operation == "scalar multiplication":
            self.matrix1 = self.create_matrix_entry(rows, cols, "Enter values for the matrix:")
            tk.Label(self.root, text="Enter scalar value:").pack()
            self.scalar_entry = tk.Entry(self.root, width=5)
            self.scalar_entry.pack()
        elif operation == "determinant":
            if rows != cols:
                tk.Label(self.root, text="Matrix must be square for determinant!").pack()
                tk.Button(self.root, text="Back", command=self.main_menu).pack()
                return
            self.matrix1 = self.create_matrix_entry(rows, cols, "Enter values for the matrix:")
        elif operation == "transpose":
            self.matrix1 = self.create_matrix_entry(rows, cols, "Enter values for the matrix:")
        else:
            self.matrix1 = self.create_matrix_entry(rows, cols, "Enter values for the first matrix:")
            self.matrix2 = self.create_matrix_entry(rows, cols, "Enter values for the second matrix:")

        calc_btn = tk.Button(self.root, text="Calculate", command=lambda: self.calculate_result(operation, rows, cols))
        calc_btn.pack()

    def calculate_result(self, operation, rows, cols):
        mat1_values = [[float(entry.get()) for entry in row] for row in self.matrix1]
        if operation in ["addition", "subtraction", "multiplication"]:
            mat2_values = [[float(entry.get()) for entry in row] for row in self.matrix2]
        else:
            mat2_values = None

        if operation == "scalar multiplication":
            scalar = float(self.scalar_entry.get())
            result = scalar_multiply(mat1_values, scalar)
        elif operation == "transpose":
            result = transpose(mat1_values)
        elif operation == "determinant":
            result = determinant(mat1_values)
        else:
            if operation == "addition":
                result = add_matrices(mat1_values, mat2_values)
            elif operation == "subtraction":
                result = subtract_matrices(mat1_values, mat2_values)
            elif operation == "multiplication":
                result = multiply_matrices(mat1_values, mat2_values)

        self.show_result(result, operation)

    def show_result(self, result, operation):
        self.clear_screen()
        tk.Label(self.root, text="Result:").pack()
        if operation == "determinant":
            tk.Label(self.root, text=f"Determinant: {result}").pack()
        else:
            for row in result:
                tk.Label(self.root, text="  ".join(map(str, row))).pack()

        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = GuiCalculater(root)
    root.mainloop()
