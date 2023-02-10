import numpy as np

def print_id(student_id):
    print("Student ID =", student_id)

def calculate_sum(array):
    return array.sum()

if __name__ == "__main__":
    print_id("6513364")
    calculate_sum(np.array([1,2,3]))