lst = [None] * 100

def insert(data, index):
    if lst[index] is None:
        lst[index] = data
    if data < lst[index]:
        insert(data, 2*index+1)
    if data > lst[index]:
        insert(data, 2*index+2)

count_leaf_nodes = 0
def leaf_node_counter(index):
    global count_leaf_nodes
    if lst[0] is None:
        print("Empty Tree")
    elif lst[2*index+1] is None and lst[2*index+2] is None:
        count_leaf_nodes += 1
    else:
        leaf_node_counter(2*index+1)
        leaf_node_counter(2*index+2)

insert(4, 0)       
insert(2, 0)
insert(6, 0)
insert(1, 0)
insert(3, 0)
insert(5, 0)
insert(7, 0)

leaf_node_counter(0)
print("Number of leaf Nodes: ", count_leaf_nodes)