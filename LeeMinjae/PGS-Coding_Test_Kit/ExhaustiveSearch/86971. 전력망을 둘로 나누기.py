def solution(n, wires):
    answer = 0
    
    countList = []
    count = 0

    for w in wires:
        copy_wires = wires.copy()
        copy_wires.remove(w)
        print(copy_wires)
        # copy_wires.remove(comb)
        #setl = set([w[0]])
        #previous = set()
        #while (setl != previous) :
        #    previous = setl.copy()
        #    for wire in copy_wires.copy():
        #        if (setl & set(wire)):
        #            setl = setl | set(wire)
        #countList.append(abs((n - 2*len(setl))))
        #count = 0
        #copy_wires = wires.copy()

    #answer = min(countList)
    #return answer
