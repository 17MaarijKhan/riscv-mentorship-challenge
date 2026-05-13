# Tower of Hanoi using Recursion
def tower_of_hanoi(n, source, target, auxiliary):
    # Base Case
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Recursive Step 1
    tower_of_hanoi(n - 1, source, auxiliary, target)
    # Move current disk
    print(f"Move disk {n} from {source} to {target}")
    # Recursive Step 2
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Number of disks
n = 3
# Function Call
tower_of_hanoi(n, 'A', 'C', 'B')
