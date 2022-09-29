lst = [None] * 100

def insert(data, index):
    if lst[index] is None:
        lst[index] = data
    if data < lst[index]:
        insert(data, 2*index+1)
    if data > lst[index]:
        insert(data, 2*index+2)

def min_value(index):
    while lst[2*index+1] != None:
        index = 2*index+1
    return index
    
def delete(data, index):
    if lst[index] != None:
        if lst[index] == data:
            if lst[2*index+1] == None and lst[2*index+2] == None:
                lst[index] = None
            if lst[2*index+1] == None and lst[2*index+2] != None: 
                lst[index] = lst[2*index+2]
                delete(lst[2*index+2], 2*index+2)
            if lst[2*index+2] == None and lst[2*index+1] != None: 
                lst[index] = lst[2*index+1]
                delete(lst[2*index+1], 2*index+1)
            if lst[2*index+1] != None and lst[2*index+2] != None: 
                min_val = min_value(2*index+2)
                lst[index] = lst[min_val]
                lst[min_val] = None
        elif data < lst[index]:
            delete(data, 2*index+1)
        elif data > lst[index]:
            delete(data, 2*index+2) 

def level_order_traversal():
    level = 0
    while True:
        ll = pow(2, level) - 1
        hl = 2 * ll
        level_nodes = []
        for i in range(ll, hl + 1):
            level_nodes.append(lst[i])
        if all(item == None for item in level_nodes):
            break
        print("Nodes at Level", level, ":", level_nodes)
        level += 1

insert(4, 0)       
insert(2, 0)
insert(6, 0)
insert(1, 0)
insert(3, 0)
insert(5, 0)
insert(7, 0)
print("====Tree Before Deletion====")
level_order_traversal()
delete(7, 0)
print("====Tree After Deletion====")
level_order_traversal()