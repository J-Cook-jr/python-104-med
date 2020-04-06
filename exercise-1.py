# This program creates a function that will translate a string using "Leet Speak" translation.

# Step 1. Define a function that takes one argument.
def leet(text):
    
    #Step 3. Create a function body using the for loop to get the characters that will replace the specified string characters with the leet characters.
    getchar = lambda c: chars[c] if c in chars else c
    chars = {"a":"4", "e":"3", "g":"6", "i":"1", "o":"0", "s":"5", "t":"7"}
    return ''.join(getchar(c) for c in text)

#Step 2. Redefine the function and replace the argument with the string you want to translate.
print(leet("Leet speak converter."))
print(leet("Converted to leet speak!"))