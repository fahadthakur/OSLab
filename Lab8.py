class Directory():
    def __init__(self, parentNode, name):
        self.parentNode = parentNode
        self.name = name
        self.subdir = []
        self.subdirectory_count = 0
        self.countSet = False;

    ## function to return name of dir/file
    def getName(self):         
        return str(self.name)
    
    ## function to add dir/file
    def add(self, dir):        
        self.subdir.append(dir)

    ## function to set the number of subdirectories/files for a particular directory
    def set_subdirectory_count(self, count):   
        self.subdirectory_count = count
        self.countSet = True

    ## function to return the parent node of the directory
    def getParent(self):       
        return self.parentNode

    ## function to print the entire file directory
    def print_heirarchy(self, heirarchy_level):  
        for i in range (heirarchy_level):
            print('-|', end='')
        print(self.getName())
        if(len(self.subdir) != 0):
            for dir in self.subdir:
                dir.print_heirarchy(heirarchy_level+1)
            


def fileOrganization():
   name = input('Enter name of dir/file (under *): ')
   root = Directory(None, name)
   currentNode = root

   
   while True:
       ## checks if we have already set the number of subdirectories/files for a particular directory
       if(currentNode.countSet == False): 
            number = int(input('Enter number of subdirectories/files under '+currentNode.getName()+' : '))
            currentNode.set_subdirectory_count(number)

       ## check to see if the subdir list length is != the subdirectory count for the directory
       if(len(currentNode.subdir) != currentNode.subdirectory_count): 
            option = int(input('Enter 1 (dir), 2 (file) under '+currentNode.getName()+' : '))
            name = input('Enter name for subdir/file under '+currentNode.getName()+' : ')
            if(option == 1):
                name += '.dir'
            else:
                name += '.file'
            dir = Directory(currentNode,name)
            currentNode.add(dir)
            currentNode = dir

       # if it is equal, then move the current node directory up by 1 level
       else: 
           currentNode = currentNode.getParent()     

       ## checks if the root node directory satisfies its subdirectory count 
       if(currentNode == root and len(root.subdir) == root.subdirectory_count):
           print('Exit')
           root.print_heirarchy(1)
           break
        
       print('')
       
fileOrganization()