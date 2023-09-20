from display import display_towers

def tower_of_hanoi(number_of_disks, start_tower, target_tower, spare_tower, towers):
    if number_of_disks == 0:
        return

    tower_of_hanoi(number_of_disks-1, start_tower, spare_tower, target_tower, towers)
    
    display_towers(towers)
    print(f"Move disk {number_of_disks} from Tower {start_tower+1} to Tower {target_tower+1}\n")
    
    towers[target_tower].append(towers[start_tower].pop())
    
    display_towers(towers)

    tower_of_hanoi(number_of_disks-1, spare_tower, target_tower, start_tower, towers)
