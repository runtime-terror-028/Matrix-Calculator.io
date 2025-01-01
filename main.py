"""
This is the entry point.
To use the GUI run the main.py with --gui flag
cli.py contains cli code
gui.py contains the Tkinter gui code
calc_methods.py contains the matrix operation functions
util.py contains the help functions
"""

import src.util as util

# Decides if the program will start with GUI or CLI
gui_mode = False

def main():

    # run with tkinter gui or cli
    if gui_mode:
        import tkinter as tk
        from src.gui import GuiCalculater

        root = tk.Tk()
        app = GuiCalculater(root)
        root.mainloop()
    else:
        from src.cli import matrix_cli
        matrix_cli()


if __name__ == "__main__":
    if util.isGuiEnabled(): gui_mode = True
    main()
