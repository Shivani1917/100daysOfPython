#  Program for Incrementing Numeric String

def incrementNumericString(input_str):
    if not input_str.isdigit():
        raise ValueError("Input must be a numeric string")

    num = int(input_str)

    num += n

    result_str = str(num)

    return result_str

input_str = input("Enter a numeric string: ")
n = int(input("Enter the increment number: "))
try:
    result_str = incrementNumericString(input_str)
    print("Incremented result:", result_str)
except ValueError as e:
    print("Error:", e)
