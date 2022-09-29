lst = [None] * 100

def insert(data, index):
    if lst[index] is None:
        lst[index] = data
    if data < lst[index]:
        insert(data, 2*index+1)
    if data > lst[index]:
        insert(data, 2*index+2)

def level_width():
    level = 0
    while True:
        ll = pow(2, level) - 1
        hl = 2 * ll
        level_nodes = []
        for i in range(ll, hl + 1):
            level_nodes.append(lst[i])
        if all(item == None for item in level_nodes):
            break
        print("Width of Level", level, ":", len(level_nodes))
        level += 1

insert(4, 0)       
insert(2, 0)
insert(6, 0)
insert(1, 0)
insert(3, 0)
insert(5, 0)
insert(7, 0)

level_width()