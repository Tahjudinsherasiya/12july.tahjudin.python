
"""Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
300}, o {'item': 'item1', 'amount': 750}]
"""

my_list = [{'item': 'item1', 'amount': 400},
           {'item': 'item2', 'amount': 300},
           {'item': 'item1', 'amount': 750}]

new_list = []
for d in my_list:
    new_list.append(tuple(d.values()))
combined_dict = {}
for t in new_list:
    if t[0] in combined_dict:
        combined_dict[t[0]] += t[1]
    else:
        combined_dict[t[0]] = t[1]
print(combined_dict)