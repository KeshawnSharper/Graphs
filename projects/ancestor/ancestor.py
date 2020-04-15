def earliest_ancestor(ancestors, starting_node):
    seeds = []
    roots = []
    for x in ancestors:
        if x[1] == starting_node:
            seeds.append(x[0])
        roots.append(x[1])
    for x in seeds:
        if x in roots:
            return earliest_ancestor(ancestors,x)
    if len(seeds) == 0:
        return -1 
    else:
        return seeds[0]
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors,3))
