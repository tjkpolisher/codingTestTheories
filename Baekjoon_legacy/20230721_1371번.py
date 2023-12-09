import sys

sentences = list(sys.stdin.readlines())
sentence = []
for i in range(len(sentences)):
    sentence.extend(list(sentences[i].rstrip('\n').replace(" " , "")))
characters = list(set(sentence))
counts = []
for alphabet in characters:
    counts.append(sentence.count(alphabet))
max_count = max(counts)
maximum = sorted([characters[i] for i in range(len(characters)) if counts[i] == max_count])
print(''.join(maximum))