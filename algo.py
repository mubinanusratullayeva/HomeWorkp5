# task-1

class Simple_sample:
    def __init__(self, massiv: list, n: int):
        self.arr = massiv
        self.numb_val = n

    def algo1(self):
        return sum(self.arr[:self.numb_val])

task_1 = Simple_sample([5,6,-4], 3)

# print(task_1.algo1())



# task-2

class Numbery_route:
    def algo2(self, n):
        sum_num = 0
        while n > 0:
            sum_num += n % 10
            n //= 10
        return sum_num

    def algo2_1(self, n):
        if n < 10:
            return n
        else:
            return self.algo2_1(self.algo2(n))

task_2 = Numbery_route()
# print(task_2.algo2_1(15), task_2.algo2_1(999))



# task-3

def ekub(a, b):

  max_num = max(a, b)
  min_num = min(a, b)

  while min_num != 0:
    q = max_num % min_num
    max_num = min_num
    min_num = q
  return max_num

print(ekub(124, 36))