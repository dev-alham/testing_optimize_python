import time
import random

newZipcodes = []
oldZipcodes = [random.randint(0,9) for i in range(1000000)]
start = time.time()

# Testing 1
# test time 1 : 0.18178129196166992
# test time 2 : 0.1913149356842041
# test time 3 : 0.17455267906188965

for zipcode in oldZipcodes:
    if zipcode % 2 == 0:
        newZipcodes.append(True)
    else:
        newZipcodes.append(False)


# Testing 2
# test time 1 : 0.1257925033569336
# test time 2 : 0.12566399574279785
# test time 3 : 0.12596559524536133

newZipcodes = list(map(lambda x: True if x % 2 == 0 else False, oldZipcodes))


# Testing 3
# test time 1 : 0.08676838874816895
# test time 2 : 0.08578205108642578
# test time 3 : 0.0867767333984375

newZipcodes += [True if x % 2 == 0 else False for x in oldZipcodes]


# Testing 4
# test time 1 : 0.08912825584411621
# test time 2 : 0.08630728721618652
# test time 3 : 0.08382368087768555

newZipcodes = [True if x % 2 == 0 else False for x in oldZipcodes]

# Testing 5
# test time 1 : 0.07587456703186035
# test time 2 : 0.07381391525268555
# test time 3 : 0.0733492374420166

newZipcodes = [True if x % 2 is 0 else False for x in oldZipcodes]

end = time.time()
print(end - start)

# cunclusion :
# Testing 5 is Faster compared to others
