guess_me = 7
if guess_me < 7:
    print("too low")
elif guess_me > 7:
    print("too high")
else:
    print("just right")
    
start = 1
while True:
    if start < guess_me:
        print("too low")
    elif start == guess_me:
        print("found it")
        break
    else :
        print("oops")
        break
    start += 1
    
j = [3,2,1,0]
for i in j:
    print(i)
    
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

squares = {x: x**2 for x in range(10)}
print(squares)

odd = {x for x in range(10) if x % 2 == 0}
print(odd)

gen = ('Got ' + str(x) for x in range(10))

for item in gen:
    print(item)

def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())

def get_odds():
    for x in range(10):
        if x % 2 == 0:
            yield x

count = 0
for num in get_odds():
    count += 1
    if count == 3:
        print(num)
        break

def test(func):
    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper

@test
def say_hi():
    print('Hello')

say_hi()

class OopsException(Exception):
    pass

try:
    raise OopsException
except OopsException:
    print('Caught an oops')

titles = ['Creature of Habit', 'Crewel Fate',]
plots = ['A nun turns into a monster', 'A haunted yarn shop']

movies = dict(zip(titles, plots))
print(movies)

