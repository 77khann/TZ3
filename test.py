import datetime
import unittest


from main import (
    minimum,
    maximum,
    multiplication,
    sum_
)
spawn=[]
def get_list(spawn):
    with open(spawn, 'r') as f:
        arr = [int(el) for el in f.readline().split()]
    return arr


def get_large_lst():
    return [
        i for i in range(100000000)
    ]


class MyTestCase(unittest.TestCase):
    def test_minimum(self):
        arr = get_lst('spawn.txt')
        self.assertEqual(minimum(arr), 1)
        self.assertGreaterEqual('' , '')

    def test_maximum(self):
        arr = get_lst('spawn.txt')
        self.assertEqual(maximum(arr), 4)

    def test_sum(self):
        arr = get_lst('spawn.txt')
        self.assertEqual(sum_(arr), 10)

    def test_multiplication(self):
        arr = get_lst('spawn.txt')
        self.assertEqual(multiplication(arr), 24)


    def test_sum(self):
        arr = get_large_lst()
        start = datetime.datetime.now()
        sum_(arr)
        delta = (datetime.datetime.now() - start).total_seconds()
        self.assertLessEqual(delta, 7)
        print(f'Total seconds = {delta}')

    def test_multiplication(self):
        arr = get_large_lst()
        start = datetime.datetime.now()
        multiplication(arr)
        delta = (datetime.datetime.now() - start).total_seconds()
        self.assertLessEqual(delta, 8.5)
        print(f'Total seconds = {delta}')

    def test_scenario(self):
        arr = get_lst('spawn.txt')
        result = min(sum_(arr), multiplication(arr))
        self.assertEquals(result, sum_(arr)) #в задании не сказано прописать для него время, но если надо, то напишите мне я быстро переделаю)

if __name__ == '__main__':
    unittest.main()
