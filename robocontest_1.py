# task-1
# Azimjonning qo'ylari'

# from roboContest import n

class SHeep_ears:
    def countears_of_sheep(self, legs):
        if legs % 4 == 0:
            return legs // 2
        else:
            return -1

es = SHeep_ears()

# print(es.countears_of_sheep(n))





# task-4
# Sovg'a

m=0
g = 1
gnomlarning_pullari = 0
while m < 7:
    m = int(input(f'{g}-gnomning puli qancha? '))
    gnomlarning_pullari += m
    g += 1

gift = int(input('sovg\'a narxini kiriting: '))

def solution(m, g):
    if m < 1000 and g < 1000:
        return g-m

print(solution(gnomlarning_pullari, gift))