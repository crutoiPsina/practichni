years_list = [2010,2011,2012,2013,2014,2015]
print(years_list[3])
print(years_list[-1])

things =  ["mozzarella","cinderella","salmonella"]
things[1] = things[1].capitalize()
print(things)
things[0] = things[0].upper()
print(things)

things.pop(-1)
print(things)

surprise = ['Groucho', 'Chico', 'Harpo']
surprise[-1] = surprise[-1].lower()
print(surprise[-1][::-1].capitalize())

e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}
print(e2f)

print(e2f["walrus"])

f2e = {}
for english, french in e2f.items():
    f2e[french] = english

print(f2e)

print(f2e["chien"])

print(set(e2f.keys()))

life = {
    "animals": {
        "cats": ["Henri", "Grumpy", "Lucy"],
        "octopi": {},
        "emus": {}
    },
    "plants": {},
    "other": {}
}

print(life.keys())