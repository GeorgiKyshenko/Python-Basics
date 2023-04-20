username = input()
user_password = input()
password_input = input()

while user_password != password_input:
    password_input = input()
print(f"Welcome {username}")
