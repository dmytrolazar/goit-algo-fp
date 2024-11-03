import random

random.seed(42)
n = 50000
results = [(random.randint(1, 6) + random.randint(1, 6)) for _ in range(n)]
print("Результати обрахунків ймовірностей методом Монте-Карло:")
print('\n'.join(['{:2}/12 — {:.2%}'.format(i, sum(1 for r in results if r == i) / n) for i in range(2, 13)]))
