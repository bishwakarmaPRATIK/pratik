
#takes a secret word as input (without spaces).

secret = input("enter your secret word");
print(secret.replace(" ",""))



#the word using a custom cipher:


#rpelace all vowel with *

vowels = "aeiouAEIOU"
for vowel in vowels:
    secret = secret.replace(vowel,"*") 

print(secret)


#reverse the entire string 

print(secret[::-1])

#shift each letter 2 place a head in the alphabet (wrap around if needed, e.g.,y -> a, z-> b)





#finally, print the resulting encoded world.