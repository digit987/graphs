visited = []
def dfs(start):
    global visited
    visited += start
    for value in graph[start]:
        if value not in visited:
            dfs(value)

graph = {
    'a' : ['b', 'c', 'd'],
    'b' : ['d', 'e'],
    'c' : ['e'],
    'd' : ['a'],
    'e' : ['f'],
    'f' : ['c']
}
dfs('a')
print(visited)
