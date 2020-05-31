# key can act as the word
# value is like the definition

# phonebook - key: the phone num, value: the person that has that num

phonebook = {89317201: "edric", 999: "police", 995: "ambulance"}

#iterate through a dict
for key in phonebook:
    print(key)

del phonebook[995]
for key in phonebook:
    print(key)
# .items() - returns all keys and values
# .values() - returns all values
# .keys() returns all keys
# nothing - returns keys
# the pairs will not be in any order
