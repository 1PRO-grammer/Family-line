family1 = {
    "surname" : "Halim",
    "father": {
        "name": "Sujono",
        "year": 1935
    },
    "mother": {
        "name": "Ika",
        "year": 1940
    },
    "child1": {
        "name": "Andrew",
        "year": 1970
    },
    "child2": {
        "name": "Lina",
        "year": 1975
    }
}

family2 = {
    "surname" : "Wijaya",
    "father": {
        "name": "Kent",
        "year": 1940
    },
    "mother": {
        "name": "Kayla",
        "year": 1945
    },
    "child1": {
        "name": "Sharen",
        "year": 1975
    }
}

family3 = {
    "surname" : "Halim",
    "father": dict(family1["child1"]),
    "mother": dict(family2["child1"]),
    "child1": {
        "name": "Ansen",
        "year": 2005
        }
}
a = family1["surname"]
b = family1["father"]
c = family1["mother"]
d = family2["surname"]
e = family2["father"]
f = family2["mother"]
g = family3["surname"]
h = family3["father"]
i = family3["mother"]
j = family3["child1"]
k = "Male side:"
l = "Female side:"
m = "The New Family:"
n = "Father:"
o = "Mother:"
p = "Son/Daughter:"
q = "Surname:"
print(k)
print(q,a)
print(n,b,o,c)
print()
print(l)
print(q,d)
print(n,e,o,f)
print()
print(m)
print(q,g)
print(n,h,o,i)
print(p,j)
