def separator():
    print("------")


text = "TodaY is A suNny Day"
# -1 takes the last char in the text, 0 gets the 1st
symbol = text[-1]
print(symbol)
separator()  # sep 1

for letter in text:
    if letter == "s":
        break
    print(letter, end="")
print()
separator()  # sep 2

new_text = ""
for letter in text:
    if letter.isupper():
        new_text += letter
print(new_text)
