# numb = input('enter a positive number: ')
n = int(input('enter a number: '))


#Koshi

class Koshi:
    def __init__(self, a: int, b: int):
        self.arifmet = (a + b) / 2
        self.geomet = (a * b) ** 0.5

    def evaluate(self):
        if self.arifmet > self.geomet:
            return '>'
        elif self.arifmet < self.geomet:
            return '<'
        else:
            return '='

koshi = Koshi(10, 2)

# print(koshi.evaluate())




#Gugurt donalari

class Match:
    matches = {
        '0': 6,
        '1': 2,
        '2': 5,
        '3': 5,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 3,
        '8': 7,
        '9': 6
    }

    def find_len_match(self, x:str):
        foo = 0
        for i in x:
            if i in self.matches.keys():
                foo += self.matches[i]
        return foo

match = Match()

# print(match.find_len_match(numb))



#Isfandiyor algebrasi

def f(x):
    return x**5 + 8*(x**4) - 5*(x**3) + 3*(x**2) + x - 12

print(f(n))