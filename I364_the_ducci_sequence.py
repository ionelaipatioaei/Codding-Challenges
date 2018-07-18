print("I364 The Ducci Sequence")

seq = input("Please use ',' to separate the numbers. \n").split(",")
steps = 2 # We need to add the initial and the final state as well

def ducci(seq):
    next_seq = []
    for i in range(0, len(seq)):
        if i == len(seq) - 1:
            next_seq.append(abs(int(seq[i]) - int(seq[0])))
            continue    
        next_seq.append(abs(int(seq[i]) - int(seq[i + 1])))
    return next_seq

while sum(ducci(seq)) != 0:
    seq = ducci(seq)
    print(seq)
    steps += 1

    if sum(ducci(seq)) <= len(seq):
        break

print(ducci(seq))
print("Steps:", steps)
