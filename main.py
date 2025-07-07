import math

a, b, c = 1, 1, 0
working_triples = []
unique_triples = []

for i in range(100):
    while c<100:
        c = math.sqrt(a**2 + b**2)
        if c.is_integer() and c<100:
            working_triples.append((a, b, int(c)))
        a += 1
    a = 1
    b += 1
    c = 0

for triple in working_triples:
    triple = sorted(triple)
    if triple not in unique_triples:
        unique_triples.append(triple)
print(unique_triples)
print(f'Total amount is {len(unique_triples)}')









