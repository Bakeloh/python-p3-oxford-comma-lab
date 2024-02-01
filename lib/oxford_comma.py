def oxford_comma(items):
    # return None
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return str(items[0])

    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"

    else:
        return f"{', '.join(map(str, items[:-1]))}, and {items[-1]}"


# This code defines a Python function 
# called oxford_comma that takes a single 
# argument items`, which is expected to be a 
# list of strings. The function returns a string that 
# contains a list of the items with appropriate punctuation, 
# following the "Oxford comma" convention.

# Here's a breakdown of what the code does:

# The function first checks the length of the items list using the len function.
# If the length is 0, the function returns an empty string.
# If the length is 1, the function returns the first (and only) item in the list as a string.
# If the length is 2, the function returns a string that concatenates the first
# and second items with the word "and" in between.
# If the length is greater than 2, the function returns a string that concatenates 
# all the items in the list except for the last one, separated by commas, followed by the word "and" and the last item.
# To accomplish this, the function uses several Python features:

# The join method of strings, which concatenates a list of strings with a specified delimiter.
# The map function, which applies a given function to each item in 
# an iterable and returns a new iterable with the results.
# String formatting, using f-strings to insert the items into the final string.
# Overall, the oxford_comma function provides a convenient way to 
# format lists of items with the Oxford comma, which can be useful in 
# many different contexts.The oxford_comma function is a Python function
# that takes a list of strings as input and returns a formatted string. 
# The function follows the "Oxford comma" convention, which is a style 
# rule that dictates the use of a comma before the word "and" in a 
# list of three or more items, except for the final item.

# The function starts by checking the length of the input list items. 
# If the list is empty, the function returns an empty string. If the 
# list contains only one item, the function returns that item as a string. 
# If the list contains exactly two items, the function returns a string 
# that combines the two items with the word "and" in between.

# If the list contains three or more items, the function uses the join 
# method of strings to concatenate all the items in the list except for 
# the last one, separated by commas. It then returns a string that combines 
# this comma-separated list with the word "and" and the last item.

# The function uses the map function to apply the str function to each item 
# in the list, converting them all to strings. It then uses the join method 
# of a string to concatenate these strings with commas in between.

# The function uses f-strings to insert the items into the final string. 
# F-strings are a feature of Python 3.6 and later that allow you to embed 
# expressions inside string literals, using curly braces {}. The expressions
# will be replaced with their values when the string is evaluated.

# Here's an example of how you might use the oxford_comma function:

# python
# Copy code
# fruits = ["apple", "banana", "cherry"]
# print(oxford_comma(fruits))  # Output: "apple, banana, and cherry"
# In this example, the oxford_comma function is called with a list 
# of strings representing different fruits. The function returns 
# a string that combines the fruit names with the Oxford comma 
# convention, resulting in the output "apple, banana, and cherry".
# The oxford_comma function is a Python function that takes a list 
# of strings as input and returns a formatted string. The function 
# follows the "Oxford comma" convention, which is a style rule that 
# dictates the use of a comma before the word "and" in a 
# list of three or more items, except for the final item.

# The function starts by checking the length of the input 
# list items. If the list is empty, the function returns an 
# empty string. If the list contains only one item, the function 
# returns that item as a string. If the list contains exactly two items, 
# the function returns a string that combines the two items with the word "and" in between.

# If the list contains three or more items, the function uses
# the join method of strings to concatenate all the items in the
# list except for the last one, separated by commas. It then 
# returns a string that combines this comma-separated list with the word "and" and the last item.