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
    # I would like to create a way for this to be changed by the user after having a list of available books presented to them later on
    file_path = "books/frankenstein.txt"
    # Utilizing the function I created for reading the content repeatedly, I'm feeding it whatever is inside the variable file_path so it can find the book to run so it can read it then return back to text
    text = read_content(file_path)
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    
    # Need to call the word_count()
    total_words = word_count(text)
    # Let the user know how many words are inside of the book (which hopefully will have more books to choose from later)
    print(f"There are a total of {total_words} found inside of this book!")
    
    # Need to call letter count and let user decide which letters to pick as well as letting them know the amount of times that letter was used.
    for letter in alphabet_lower:
        num_occurences = letter_count(text, letter)
        print(f"The letter: {letter} was found: {num_occurences} times within the book!")
        
    # Once again, I would like to be able to have the books as a list the user sees and can choose from then I can say {book_name} instead of just book
    # I am getting the letter(s) from the user to put into the letter count function
    user_letter = input("Please choose a letter(s) to see how many times they appear within the book! ")
    if len(user_letter) == 1 and user_letter.isalpha() and user_letter.islower():
        count = letter_count(text, user_letter)
        # I feel like I'm repeating myself here and I'll see two prints?
        print(f"The letter you've chosen: {user_letter} was found inside of the book {count} times!")
    else:
        print("Please, use only a single lowercase letter at a time!")
        
        
# To achieve the count of words, I retyped code (yes going to fix in future when I get better understanding), in which is reads the entire text of the book as a string.
# Then it splits the long string into a new list using the split.() and having it split on white space (spaces) Then printing the resulting list's length by putting it into len()
# Along with creating read_content() I forgot to remove old code which was just repeating the function, so I'm trying to now clean it up by removing and using the function
def word_count(text):
    words = text.split()
    return len(words)
    
    # with open("books/frankenstein.txt") as f:
    #     file_contents = f.read()
    #     words = file_contents.split()
    #     print(len(words))

# Here I'm retyping code again(I know I need to fix this). I'm taking the entirety of the text from the given book, reading it and converting it all to lowercase
# From there, I declared a new variable named count and set it to 0 since I'm just adding. Then did a small for loop with an if statement to check if what I pass in for the 
# function parameter matches what is being checked at the time for the loop. If it is, then add 1 to the count variable and once the loop is completed, to print the final result of count to console
def letter_count(text, letter):
        text_lowered = text.lower()
        count = 0
        for i in text_lowered:
            if i == letter:
                count += 1
        return count

# Here I'm trying to create a way to reduce the amount of code I have repeating itself currently                
def read_content(file_path):
    with open(file_path) as f:
        return f.read()
        
if __name__ == "__main__":
    main()
    # word_count()
    # # Would like to create a way to take an input from the user and set that as what we're asking to be ran in the letter_count() function
    # # So it would ideally look more like letter_count(user_letter_choice). Might need to create a failsafe in case the user tries over 1 character.
    # letter_count("i")
    
