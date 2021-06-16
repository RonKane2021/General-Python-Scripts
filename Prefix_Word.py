def ListToString(s):
    strl = " "
    return (strl.join(s))

word = "ABC00"
letters = []

for i in range (20):
    if i <10:
        new_word = word + str(0) + str(i)
        letters.append(new_word)
    else:
        new_word = word + str(i)
        letters.append(new_word)
        
new_letters = (ListToString(letters))
final = new_letters.replace(" ", ", ")

print (final)

# =============================================================================
# Output: 'ABC0000, ABC0001, ABC0002, ABC0003, ABC0004, ABC0005, ABC0006, ABC0007, ABC0008, ABC0009, ABC0010, ABC0011, ABC0012, ABC0013, ABC0014, ABC0015, ABC0016, ABC0017, ABC0018, ABC0019, ABC0020'
# =============================================================================
