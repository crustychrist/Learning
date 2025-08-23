
import string


# Creating a dictionary with letters associating to length.
list_alphabet = list(string.ascii_lowercase)
list_numbers = list(range(0,26))
dict_alphaNum = dict(zip(list_alphabet, list_numbers))

# input and algo
input = ["adc","wzy","abc"]
lst = []
lst.extend(input)
print(lst)