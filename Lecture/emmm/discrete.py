pegs = {"source":[],"Target":[],"spare":[]}


def init_pegs(pegs):
    pegs["source"].append(1)
    pegs["source"].append(2)
    pegs["source"].append(3)


def print_pegs(pegs):
    for peg in pegs:
        print("peg"+peg+"holds: ")
        for disk in pegs[peg]:
            print(disk)

def move_pegs(src,dest):
    if len(pegs[src])<=0:
        print("Trying to move from an empty peg")
        return
    if pegs[src][0]>pegs[dest][0]:
        return
    pegs[dest].push(pegs[src][0])
    pegs[src].pop()


print(print_pegs(pegs))
init_pegs(pegs)