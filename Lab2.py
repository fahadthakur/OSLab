from queue import Queue

def FIFOPage(pages, capacity):
    memSet = set()
    PageQueue = Queue()

    pageMiss = 0
    for i in range(len(pages)):
        print('Currently going over page ' + str(pages[i]))
        if len(memSet) < capacity:
            print('Memory set is not full and is less than capacity. Current size of Memory allocation ' +str(len(memSet))+' and total capacity is ' + str(capacity))
            if pages[i] not in memSet:
                print('Current page '+str(pages[i]) +' not in memory set. Incrementing page miss by 1 and adding current page to the memory set')
                memSet.add(pages[i])
                pageMiss += 1
                PageQueue.put(pages[i])
                print('Page which is top of queue is ' + str(PageQueue.queue[0]))
            else:
                print('Current page '+str(pages[i])+' is in the memory set.')

        else:
            print('Memory set is at full capacity ' + str(len(memSet)))
            if pages[i] not in memSet:
                TopQueue = PageQueue.queue[0]
                PageQueue.get()
                memSet.remove(TopQueue)
                print('Current page ' + str(pages[i]) + ' not in memory set. Incrementing page miss by 1 and adding current page to the memory set')
                print('Currently removed top element is ' + str(TopQueue))
                print('Memory set capacity currently at '+str(len(memSet)))
                memSet.add(pages[i])
                PageQueue.put(pages[i])
                print('Page which is top of queue is ' + str(PageQueue.queue[0]))
                pageMiss += 1
            else:
                print('Current page ' + str(pages[i]) + ' is in the memory set.')

        print('')

    return pageMiss

if __name__ == '__main__':
    pages = [7, 0, 1, 2, 0, 3, 0,
             4, 2, 3, 0, 3, 2]
    capacity = 4
    miss = FIFOPage(pages, capacity)
    print('Total number of miss is ' + str(miss))
    print('Miss ratio '+ str(miss/len(pages)))