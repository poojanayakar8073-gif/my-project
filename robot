import random

# Create 4x4 grid with random dirty (1) or clean (0)
def create_room():
    return [[random.choice([0, 1]) for _ in range(4)] for _ in range(4)]

# Display the room
def display_room(room):
    for row in room:
        print(" ".join(["D" if cell == 1 else "C" for cell in row]))
    print()

# Clean the room
def clean_room(room):
    cleaned_positions = []
    total_dirty = 0
    cleaned_count = 0

    for i in range(4):
        for j in range(4):
            if room[i][j] == 1:  # Dirty
                total_dirty += 1
                room[i][j] = 0   # Clean it
                cleaned_positions.append((i, j))
                cleaned_count += 1

    return cleaned_positions, total_dirty, cleaned_count


# MAIN PROGRAM
room = create_room()

print("Room before cleaning:")
display_room(room)

cleaned_positions, total_dirty, cleaned_count = clean_room(room)

print("Room after cleaning:")
display_room(room)

print("Cleaned positions:")
for pos in cleaned_positions:
    print(pos)

# Performance calculation
if total_dirty == 0:
    performance = 100
else:
    performance = (cleaned_count / total_dirty) * 100

print(f"Performance: {performance:.2f}%")
