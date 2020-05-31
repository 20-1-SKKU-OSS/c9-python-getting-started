#Method or sorting alphabetically
def sorter_alphabetically(item):
    return item['name']

#method of sorting by length
def sorter_by_length(item):
	return len(item['name'])

presenters = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Christopher', 'age': 47}
]

#Sort alphabetically
presenters.sort(key=sorter_alphabetically)
print(presenters)

#Sort by length of name(shortest to longest)
presenters.sort(key=sorter_by_length)
print(presenters)
