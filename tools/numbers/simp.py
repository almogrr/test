# Assuming initial_calls list is declared in this module or imported
from tools.numbers.flag import check_simp_first_flag,check_simp_two
# Flag variable for controlling function behavior

initial_calls = []  # Placeholder for initial_calls list

# Function to check if an initial function from 'simp' module was called
def check_if_simp_first():
    global check_simp_first_flag
    simp_calls = [call for call in initial_calls if call.startswith('tools.numbers.simp')]
    if not simp_calls or (simp_calls[0].endswith('subtract') and simp_calls[0] != 'tools.numbers.simp.subtract'):
        raise RuntimeError("Please call an initial function from 'simp' module (add or subtract) before using functions from 'comp' module.")

def add(a, b):
    global check_simp_first_flag
    global check_simp_two
    if check_simp_first_flag:
        check_simp_first_flag = True  # Update the flag for the next operation
        check_simp_two = False
        return a + b
    else:
        raise RuntimeError("Error: Please call an initial function from 'simp' module (add or subtract) before using functions from 'comp' module.")

def subtract(a, b):
    global check_simp_first_flag
    global check_simp_two
    if check_simp_first_flag:
        check_simp_first_flag = True
        check_simp_two = False
        return a - b
    else:
        raise RuntimeError("Error: Please call an initial function from 'simp' module (add or subtract) before using functions from 'comp' module.")
