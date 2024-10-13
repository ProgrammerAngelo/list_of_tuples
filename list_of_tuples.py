#make a list for numbers
print("\nCombining list of names\n")
list_of_numbers = [1, 2, 3, 4, 5]
#make a list for names
lis_of_names = ["Gab", "Ris", "Ed", "Kit", "jes"]
#method for combining the names and names
combined_list = [(numbers, names) for numbers, names in zip(list_of_numbers, lis_of_names)]
#for displaying the result
print(combined_list)