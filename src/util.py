import argparse

# decide if the program will run using gui or cli depending on user command argument
def isGuiEnabled():
    parser = argparse.ArgumentParser(description="Process command-line arguments.") 
    # Add --gui argument 
    parser.add_argument('--gui', action='store_true', help="Enable GUI mode")
    # Parse the arguments
    args = parser.parse_args()
    
    gui_mode = args.gui
    return gui_mode