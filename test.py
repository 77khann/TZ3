import datetime
import unittest


from main import (
    minimum,
    maximum,
    multiplication,
    sum_
)


def get_large_lst():
    return [
        i for i in range(100000000)
    ]


class MyTestCase(unittest.TestCase):
    def test_minimum(self):
        with open('spawn.txt', 'r') as f:
            arr = [int(el) for el in f.readline().split()]
        self.assertEqual(minimum(arr), 1)
        self.assertGreaterEqual('' , '')

        
    def test_maximum(self):
        with open('spawn.txt', 'r') as f:
            arr = [int(el) for el in f.readline().split()]
        self.assertEqual(maximum(arr), 9)

        
    def test_sum(self):
        with open('spawn.txt', 'r') as f:
            arr = [int(el) for el in f.readline().split()]
        self.assertEqual(sum_(arr), 10)

        
    def test_multiplication(self):
        with open('spawn.txt', 'r') as f:
            arr = [int(el) for el in f.readline().split()]
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
        with open('spawn.txt', 'r') as f:
            arr = [int(el) for el in f.readline().split()]
        result = min(sum_(arr), multiplication(arr))
        self.assertEquals(result, sum_(arr)) #в задании не сказано прописать для него время, но если надо, то напишите мне я быстро переделаю)

if __name__ == '__main__':
    unittest.main()
