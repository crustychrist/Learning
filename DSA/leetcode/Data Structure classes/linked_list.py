
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class linkedList :
    def __init__(self):
        self.head = None
        
    def append_data(self,data):    
        new_node = Node(data)
        
        if self.head == None: # init case to assign head to first node
            self.head = new_node
            
        else:
            current_node = self.head
            
            while(current_node.next != None):
                current_node = current_node.next
                
            current_node.next = new_node
            
    def traverse(self):
        current_node = self.head
        
        while current_node.next != None:
            print(current_node.data)
            current_node = current_node.next
            
        if current_node.next == None: #printing edge case
            print(current_node.data)