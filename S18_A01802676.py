# Análisis de temperaturas x semana
temp  = [20,30,26,21,23,32,25]

promedio= sum (temp)/ len(temp)
print( promedio)

for item in temp :
    if item >= promedio:
        print(item,"is above average")
    
    else:
        print(item,"is belove avarage")

#Students exercises
students=["Maria,Pablo,Pato,Romina,Regina,Pedro"],
st_grades=[90,60,80,95,75,88,92]

print((sum (st_grades)/ len(st_grades)), "is the avarage")

FailSudent=0

for grade in st_grades:
    if grade < 70:
        FailStudent= FailStudent + 1

    else:
        PassStudent=  PassStudent +1
    
print(PassStudent,"students passed" )
print(FailStudent,"students Fail" )

    
