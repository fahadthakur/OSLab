def calculateResourcesNeed(resources_need, maximum_resources, allocated_resources, num_processes, num_resources):
    # Calculating the resource needed for each process
    for i in range(num_processes):
        for j in range(num_resources):
            # Need of instance = maxm instance -
            # allocated instance
            resources_need[i][j] = maximum_resources[i][j] - allocated_resources[i][j]

def systemSafe(processes, available_resources, maximum_resources, allocated_resources):
    # checking if the system is in a safe state
    num_processes = processes
    num_resources = len(available_resources)
    resources_need = []
    for i in range(num_processes):
        l = []
        for j in range(num_resources):
            l.append(0)
        resources_need.append(l)    # initialising the resource needed array

    # Function to calculate need matrix
    # calculating the resource needed for each process to complete its execution
    calculateResourcesNeed(resources_need, maximum_resources, allocated_resources, num_processes, num_resources)

    # To Mark the processes as finish
    process_finish = [0] * num_processes  # 0 means that process is not finished,  1 means that process is finished

    # To store safe sequence 
    safeSeq = [0] * num_processes

    # Make a copy of available resources 
    total_resources = available_resources.copy()

    count = 0
    while (count < num_processes):  # while all processes are not finished executing
        found = False
        for p in range(num_processes):
            # First check if a process is finished, if not then we try to see if the total_resources[] will satisfy the need of that process
            if (process_finish[p] == 0):
                print("Currently going over unfinished process: " + str(p))
                # Check if for all resources 
                # of current process need is less
                # than total_resources[]
                for j in range(num_resources):
                    if (resources_need[p][j] > total_resources[j]):
                        print("Resources needed by process "+ str(p) + " is greater than available resource for that job\n"
                                                                       "--------------------------------------------------\n")
                        break

                # If all needs of the process were satisfied.
                if (j == num_resources - 1):
                    print("All of the needs of process "+ str(p) + " are being satisfied.")
                    # deallocate the resources from the current process and add it to the available resources
                    print("Deallocating resources from process " + str(p) + " and adding to the available resources.")
                    for k in range(num_resources):
                        total_resources[k] += allocated_resources[p][k]
                        # Add this process to safe sequence.
                    print("Current available resources : " + str(total_resources))
                    print("Adding process " + str(p) + " to the safe sequence\n"
                                                       "--------------------------------------------------\n")
                    safeSeq[count] = p
                    count += 1

                    # Mark this p as finished 
                    process_finish[p] = 1

                    found = True


        # If we could not find a next process 
        # in safe sequence. 
        if (found == False):
            print("System is not in safe state")
            return False

    # If system is in safe state then 
    # safe sequence will be as below 
    print("System is in safe state.",
          "\nSafe sequence is: " + str(safeSeq))

    return True


# Driver code
if __name__ == "__main__":

    processes = int(input("Number of processes : "))
    resources = int(input("Number of resources : "))
    available_resources = [int(i) for i in input ("Current Available resources : ").split()]
    print("\nResources allocated for each process")
    allocated_resources = [[int(i) for i in input(f"process {j}: ").split()] for j in range(processes)]

    print("\nMaximum resources for each process")
    maximum_resources = [[int(i) for i in input(f"process {j} : ").split()] for j in range(processes)]

    systemSafe(processes, available_resources, maximum_resources, allocated_resources)

    # debug
    # processes = 4
    # resources = 3
    # current_available_resource = [2, 3, 3]

    #allocated_resources = [[0, 1, 0], [2, 0, 0],
    #          [3, 0, 2], [2, 1, 1]]
    
    # maximum_resources = [[7, 5, 3], [3, 2, 2],
    #         [9, 0, 2], [2, 2, 2]]

    # Check system is in safe state or not