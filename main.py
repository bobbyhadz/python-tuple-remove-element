# Remove an element from a tuple in Python

my_tuple = ('bobby', 'hadz', 'com', 'abc')

new_tuple = tuple(
    item for item in my_tuple if item != 'bobby'
)

# 👇️ ('hadz', 'com', 'abc')
print(new_tuple)