student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items(): 
    
    pass

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score  
    pass 

# Keyword Method with iterrows()


# Create a dictionary in this format:
# {new_key:new_value for (index, row) in df.iterrows()}
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
answer = input("Enter a word: ").upper()
output_list = [ phonetic_dict[letter]  for letter in answer]
print(output_list)


