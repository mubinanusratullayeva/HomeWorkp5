# task-1
# Azimjonning qo'ylari'

from roboContest import n

class SHeep_ears:
    def countears_of_sheep(self, legs):
        try:
            if legs > 0:
                return int((legs / 4) * 2)
            else:
                return -1
        except Exception as e:
            return e

es = SHeep_ears()

# print(es.countears_of_sheep(n))