file = open("example.txt", "w")

try:
    file.write("Hello, 2025!\n")
    file.write("Bye, 2024!\n")
finally:
    file.close()

with open("example_2.txt", "w") as file:
    file.write("Hello, 2025!\n")
    file.write("Bye, 2024!\n")


