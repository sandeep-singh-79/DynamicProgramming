def fibDPTabulation(position):
    if position <= 1: return 1
    table = list()
    table = [0 for i in range(0, position+1)]
    table[1] = 1
    
    length = len(table)
    for i in range(2, length):
        table[i] = table[i-2] + table[i-1]
    
    return table[position]