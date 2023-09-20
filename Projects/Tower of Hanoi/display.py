def display_towers(towers):
    max_height = max(len(towers[0]), len(towers[1]), len(towers[2]))
    for i in range(max_height, 0, -1):
        for j in range(3):
            if len(towers[j]) >= i:
                print(f" {towers[j][i-1]} ", end=" ")
            else:
                print("   ", end=" ")
        print("")
    print("___ ___ ___")
    print(" 1   2   3 ")
    print()
