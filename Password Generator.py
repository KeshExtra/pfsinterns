import pyperclip
import secrets

character_set = input("What are the characters that you would like to use to generate the password? e.g. abcdefgh1234?/! \n")
character_list = []
password = ""
for i in character_set:
    character_list.append(i)
character_list = list(set(character_list))
length = int(input("What is the length of the password?\n"))
for i in range(length):
    password+=secrets.choice(character_list)

print(password)
copy = input("Would you like to copy the password to the clipboard? (Y/N)\n")
copy = copy.upper()
print(copy)
while True:
    if copy == "Y":
        pyperclip.copy(password)
        print("Copied")
        break
    elif copy =="N":
        print("Not Copied")
        break
    else:
        print("Please pick Y for yes or N for no.")
        copy = input("Would you like to copy the password to the clipboard? (Y/N)\n")