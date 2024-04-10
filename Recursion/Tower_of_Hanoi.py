def tower_of_hanoi(n, s, d, a):
    # Base case: If there's only one disk, move it directly from source to destination.
    if n == 1:
        return 1
    
    # Recursive case:
    # 1. Move n-1 disks from source to auxiliary peg.
    # 2. Move the nth disk from source to destination.
    # 3. Move the n-1 disks from auxiliary to destination.
    # The function returns the total number of moves required to solve the puzzle.
    return tower_of_hanoi(n-1, s, a, d) + 1 + tower_of_hanoi(n-1, a, d, s)

# Example usage: Move 4 disks from peg 's' to peg 'd', using peg 'a' as auxiliary.
print(tower_of_hanoi(4, 's', 'd', 'a'))


# Time Complexity

    # The time complexity of the Tower of Hanoi algorithm is determined by the number of moves required to
    # solve the puzzle. Each move is a constant time operation, and the total number of moves is 2^n - 1, 
    # where n is the number of disks. This is because each move of a disk involves moving n-1 disks to an 
    # auxiliary peg, moving the disk itself, and then moving the n-1 disks from the auxiliary peg to the 
    # destination peg. This process is repeated recursively for each disk, leading to a total of 2^n - 1 
    # moves. Therefore, the time complexity is O(2^n).

# Space Complexity

    # The space complexity of the Tower of Hanoi algorithm is determined by the maximum depth of the 
    # recursion tree, which is n. This is because the algorithm makes two recursive calls for each disk, 
    # and the depth of the recursion tree is equal to the number of disks. Each recursive call adds a level
    #  to the recursion tree, and the maximum depth is reached when all disks are moved to the auxiliary peg. Therefore, the space complexity is O(n) 3.

# In summary, the Tower of Hanoi algorithm has a time complexity of O(2^n) due to the exponential number of 
# moves required to solve the puzzle, and a space complexity of O(n) due to the depth of the recursion tree.
