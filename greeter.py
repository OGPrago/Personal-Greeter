from pathlib import Path

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
hobby = str(input("Enter your favorite hobby: "))
message = f"Hello {name}. You're {age} years old. Your hobby is {hobby}."
print(message)

Path("greetings.txt").write_text(message + "\n", encoding="UTF-8")