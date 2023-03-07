# ### Exercise #2 <br>
# <p>Write an anonymous function that sorts this list by the last name...<br><b>Hint: Use the ".sort()" method and access the key"</b></p>

# `Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']`
names = ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield']


names.sort(key=lambda x: x.split()[-1])

print(names)



