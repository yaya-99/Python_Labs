sentence = input( "Enter a sentence : ")
i= 0
cap, small, dig, Sp = 0, 0, 0, 0
while i < len(sentence):
    if sentence[i] >= 'A' and sentence[i] <= 'Z':
        cap+=1
    elif ord(sentence[i]) >= 48 and ord(sentence[i]) <= 57:
        dig +=1
    elif ord(sentence[i]) >= 97 and ord(sentence[i]) <= 122:
        small += 1
    else:
        Sp += 1
    i+= 1

print( "Capital Count :",cap)
print("Small : ", small)
print("Digit : ", dig)
print("Special : ", Sp)
