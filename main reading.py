# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    var_open_file = open(filename)
    var_read_file = var_open_file.read()
    
    return var_read_file


dictionary = {}

def count_words():
    text = read_file_content("./story.txt")
    split_text = text.split()

    for i in split_text:
        # This line of code adds 1 to any key value that already exist in the dictionary
        if i in dictionary:
            dictionary[i] += 1
        #this line of code equate any string in the split yext variable to 1 if it doesn't exist in the dictionary yet  
        else:
            dictionary[i] = 1            
    return dictionary

print(count_words())
