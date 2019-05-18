import time
import random

start = time.time()
data = [random.randint(0,9) for i in range(1000000)]

# Testing 1
# test time 1 : 1.63297438621521
# test time 2 : 1.6104836463928223
# test time 3 : 1.594841718673706

result1 = []
for sub in data:
    if sub not in result1:
        result1.append(sub)


# Testing 2
# test time 1 : 1.5616710186004639
# test time 2 : 1.5611648559570312
# test time 3 : 1.563831090927124

result2 = []
values = set()
for sub in data:
    if sub not in values:
        values.add(sub)
        result2.append(sub)


# Testing 3
# test time 1 : 1.490015983581543
# test time 2 : 1.485351800918579
# test time 3 : 1.4811670780181885

result3 = list(set(data))

end = time.time()
print(end - start)

# cunclusion :
# Testing 3 is Faster compared to others

