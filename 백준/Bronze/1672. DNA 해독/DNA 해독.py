from collections import deque

N = int(input())
dna = deque(input())
dna_dict = {'A': {'A': 'A', 'G': 'C', 'C': 'A', 'T': 'G'},
            'G': {'A': 'C', 'G': 'G', 'C': 'T', 'T': 'A'},
            'C': {'A': 'A', 'G': 'T', 'C': 'C', 'T': 'G'},
            'T': {'A': 'G', 'G': 'A', 'C': 'G', 'T': 'T'}}

while len(dna) > 1:
    end1 = dna.pop()
    end2 = dna.pop()
    dna.append(dna_dict[end2][end1])

print(dna[0])