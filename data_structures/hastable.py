'''
About:

A Hash table (HT) is a data structure that provides a mapping from keys to values using a technique called hashing.






'''



def myHashfunc(Name,Age,Sex):
    sum = 0
    for char in Name:
        sum = sum+ord(char)
    return (sum + Age + ord(Sex) )

print(myHashfunc('Asjad', 31,'M'))

print(myHashfunc('crhis', 91,'F'))







# A hash function $H(x)$ is a function that maps a key ' $x$ ' to a whole number in a fixed range.