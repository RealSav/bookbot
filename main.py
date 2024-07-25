# 1. Open the file
# 2. Read the contents
# 3. Print the contents
# Add a new function that takes the txt from the book as a string and returns the # of words in the string
# Add a print() then run code to make sure it does as expected, expecting 77986

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        
def word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))
        
if __name__ == "__main__":
    main()
    word_count()