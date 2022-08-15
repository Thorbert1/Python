text = str(input("This is a user input. Say anything! "))

print("This is what you said: " + text)
print("There are " + str(len(text.strip())) + " characters and " + str(len(text.split(" "))) + " words in it")
