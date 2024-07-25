# 1. Open the file
# 2. Read the contents
# 3. Print the contents
# Add a new function that takes the txt from the book as a string and returns the # of words in the string
# Add a print() then run code to make sure it does as expected, expecting 77986
# Add a new function that takes the text from a book and counts the amount of letters inside after converting to all lower case
# I seem to be repeating the same code and should probably convert it into a function. However, I'm not sure how I would do so at this point in time so I'm going to keep going as I have so far
# Created read_content() to do just as the function name says

# This is my first time using the with function and I'm still trying to comprehend and understand it fully but to my current understanding it's similar to a for loop or while function
# It takes the entirety of the path passed to it, in this case, "books/frankenstein.txt" and assigns it to f. Then using a new variable I assign as the entire text where it reads it once
# Then ends the operation by using .read() on the text of the book.
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        
# To achieve the count of words, I retyped code (yes going to fix in future when I get better understanding), in which is reads the entire text of the book as a string.
# Then it splits the long string into a new list using the split.() and having it split on white space (spaces) Then printing the resulting list's length by putting it into len()
def word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))

# Here I'm retyping code again(I know I need to fix this). I'm taking the entirety of the text from the given book, reading it and converting it all to lowercase
# From there, I declared a new variable named count and set it to 0 since I'm just adding. Then did a small for loop with an if statement to check if what I pass in for the 
# function parameter matches what is being checked at the time for the loop. If it is, then add 1 to the count variable and once the loop is completed, to print the final result of count to console
def letter_count(letter):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        txt_lowered = file_contents.lower()
        count = 0
        for i in txt_lowered:
            if i == letter:
                count += 1
        print(count)

# Here I'm trying to create a way to reduce the amount of code I have repeating itself currently                
def read_content(file_path):
    with open(file_path) as f:
        return f.read()
        
if __name__ == "__main__":
    main()
    word_count()
    # Would like to create a way to take an input from the user and set that as what we're asking to be ran in the letter_count() function
    # So it would ideally look more like letter_count(user_letter_choice). Might need to create a failsafe in case the user tries over 1 character.
    letter_count("i")