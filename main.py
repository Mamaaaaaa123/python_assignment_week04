#2
# import calculator
# print(calculator.add(100, 100))
# print(calculator.substract(100, 100))
# print(calculator.multiply(100, 100))
# print(calculator.divide(100, 100))

#3
# import lambda_calculator
# print(lambda_calculator.add(100, 100))
# print(lambda_calculator.substract(100, 100))
# print(lambda_calculator.multiply(100, 100))
# print(lambda_calculator.divide(100, 100))

#4
# import string_operations
# print(string_operations.reverse_string("OHHH yeah"))
# print(string_operations.capitalize_string("OHHH yeah"))
# print(string_operations.lowercase_string("OHHH yeah"))
# print(string_operations.uppercase_string("OHHH yeah"))

#5
# import calculator
# print("Using calculator.py:")
# print("Addition:", calculator.add(10, 10))
# print("Subtraction:", calculator.substract(10, 10))
# print("Multiplication:", calculator.multiply(10, 10))
# print("Division:", calculator.divide(10, 10))

# import string_operations
# sample_string = "Ohhh yeah"
# print("\nUsing string_operations.py:")
# print("Original:", sample_string)
# print("Reversed:", string_operations.reverse_string(sample_string))
# print("Capitalized:", string_operations.capitalize_string(sample_string))
# print("Lowercase:", string_operations.lowercase_string(sample_string))
# print("Uppercase:", string_operations.uppercase_string(sample_string))

#6
# grades = [55, 70, 65, 40, 90, 85, 50, 77]
# passed_with_bonus = list(map(lambda x: x*1.05, filter(lambda x: x >= 60, grades)))
# print(passed_with_bonus)

#7
children = [ {"name": "Alice", "age": 2, "height": 95},
              {"name": "Bob", "age": 4, "height": 105},
              {"name": "Charlie", "age": 3, "height": 110},
              {"name": "David", "age": 5, "height": 102},
              {"name": "Eve", "age": 6, "height": 99} ]
eligible_children = (child for child in children if child["age"] >= 3 and child["height"] >= 100)
print(list(eligible_children))