while True:
    username = input()
    if username == "End".casefold():
        print("End of While Loop")
        break
    print(f"The user name is {username}")
