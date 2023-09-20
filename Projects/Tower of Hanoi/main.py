from logic import tower_of_hanoi

def run(num_disks):
    start = [disk for disk in range(num_disks, 0, -1)]
    target = []
    spare = []

    towers = {0: start, 2: target, 1: spare}

    tower_of_hanoi(num_disks, 0, 2, 1, towers)

if __name__ == "__main__":
    run(3)
