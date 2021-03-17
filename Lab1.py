memory = [10, 20, 15, 30]  # this is the size of the memory partitions
program = [5, 30, 10, 40]  # this is the size of the program



def FirstFit(memory, program):
    allocation = [-1]*len(program)   #allocation refers to the index in which that specific program is stored in
    mem = memory.copy()
    for i in range(len(program)):
        for j in range(len(mem)):
            if mem[j]>=program[i]:
                allocation[i] = j    # store the index of the memory in which that program is stored in
                mem[j]-= program[i]
                break
    return allocation, mem   # in this case mem refers to the remaining memory in the partition

print(FirstFit(memory, program))

def BestFit(memory, program):
    allocation = [-1]*len(program)      # allocation refers to the index in which that specific program is stored in
    mem = memory.copy()
    for i in range(len(program)):
        leastIndex = -1                 # initialize least index as -1 to indicate start of search along memory partitions
        for j in range(len(mem)):
            if(mem[j] >= program[i]):
                if leastIndex == -1:    # indicates that this is the first search along memory partitions and hence we set the least index as such
                    leastIndex = j
                elif mem[leastIndex] > mem[j]:    # find the least value which is closest to the program size, and if found change the least index as such
                    leastIndex = j
        if leastIndex != -1:            # if we have found a least index allocate it in the partition 
            allocation[i] = leastIndex
            mem[leastIndex] -= program[i]
    return allocation, mem

print(BestFit(memory, program))