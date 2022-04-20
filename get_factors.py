import sys
import math
import progressbar


if len(sys.argv) < 2:
    raise Exception("Need input")

num = int(sys.argv[1])
print("Getting to " + str(num))
primes = [2]
factors = dict()
c = 0

if num < 2:
    print("Number must be >= 2")
    quit()

widgets = [' [',
           progressbar.Timer(format='elapsed time: %(elapsed)s'),
           '] ',
           progressbar.PercentageLabelBar(), ' (',
           progressbar.ETA(), ') ',
           ]

bar = progressbar.ProgressBar(max_value=100,
                              widgets=widgets).start()

while True:
    if num % primes[c] == 0:
        num = num / primes[c]
        if primes[c] not in factors:
            factors[primes[c]] = 0
        factors[primes[c]] = factors[primes[c]] + 1
    else:
        c += 1
        x = primes[c-1] + 1
        n = 0
        while True:
            if x % primes[n] == 0:
                x += 1
                n = 0
            elif primes[n] > math.sqrt(x+1):
                break
            else:
                n += 1
                if n >= len(primes):
                    break
        primes.append(x)
        bar.update(min(100, x * x / num * 100))
    if (num < 100 and primes[c] > num):
        break
    if (num > 100 and primes[c] > math.sqrt(num)):
        factors[int(num)] = 1
        break
bar.finish()
output = ''
for i in factors:
    output += str(i) + '^' + str(factors[i]) + ' * '

output = output[:-3]
print("\n")
print(sys.argv[1] + ' = ' + output)

print(factors)
