# This program stores the full name for each month in a list,
# but prints their abbreviation to demonstrate abbreviating items
# from a list

print("\nThis program prints each month using list comprehension to print both the full name and the abbreviation: ")

# Each month in a list, lookup table
months_table = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# This line abbreviates the months_table from a list
# months_table_abbreviated is the full name of the month,
# up until the third character. "Month" (list item)
# in the list (months_table), up until the third character
# List comprehension explained by #Python IRC
# Where querying Google for "abbreviate items in a list"
# failed.
months_table_abbreviated = [month[:3] for month in months_table]

# print the months_table, joined into a string
print("\n", ', '.join(map(str, months_table)))

# print the abbreviated months_table, joined into a string
print("\n", ', '.join(map(str, months_table_abbreviated)), "\n")
