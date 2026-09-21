print("S113 Dhani Singh")

import random


def calculate_movement(sequence, head):
    movement = 0
    current = head

    for request in sequence:
        movement += abs(request - current)
        current = request

    return movement


def fcfs(requests, head):
    sequence = requests.copy()
    movement = calculate_movement(sequence, head)
    return sequence, movement


def sstf(requests, head):
    pending = requests.copy()
    sequence = []
    current = head

    while pending:
        nearest = min(pending, key=lambda x: abs(x - current))
        sequence.append(nearest)
        pending.remove(nearest)
        current = nearest

    movement = calculate_movement(sequence, head)
    return sequence, movement


def cscan(requests, head, disk_size):
    left = sorted([x for x in requests if x < head])
    right = sorted([x for x in requests if x >= head])

    sequence = []
    movement = 0
    current = head

    for request in right:
        sequence.append(request)
        movement += abs(request - current)
        current = request

    if current != disk_size - 1:
        movement += abs((disk_size - 1) - current)
        current = disk_size - 1

    if left:
        movement += disk_size - 1
        current = 0

        for request in left:
            sequence.append(request)
            movement += abs(request - current)
            current = request

    return sequence, movement


def clook(requests, head):
    left = sorted([x for x in requests if x < head])
    right = sorted([x for x in requests if x >= head])

    sequence = []
    movement = 0
    current = head

    for request in right:
        sequence.append(request)
        movement += abs(request - current)
        current = request

    if left:
        movement += abs(current - left[0])
        current = left[0]
        sequence.append(current)

        for request in left[1:]:
            sequence.append(request)
            movement += abs(request - current)
            current = request

    return sequence, movement


def rss(requests, head):
    pending = requests.copy()
    sequence = []
    current = head

    while pending:
        request = random.choice(pending)
        pending.remove(request)
        sequence.append(request)
        current = request

    movement = calculate_movement(sequence, head)
    return sequence, movement


def disk_scheduling():
    print("\n========== DISK SCHEDULING ==========")

    requests = list(map(
        int,
        input("Enter disk request queue: ").split()
    ))

    head = int(input("Enter initial head position: "))
    disk_size = int(input("Enter disk size: "))

    print("\nFCFS")
    seq, movement = fcfs(requests, head)
    print("Sequence:", seq)
    print("Total Head Movement:", movement)

    print("\nSSTF")
    seq, movement = sstf(requests, head)
    print("Sequence:", seq)
    print("Total Head Movement:", movement)

    print("\nC-SCAN")
    seq, movement = cscan(requests, head, disk_size)
    print("Sequence:", seq)
    print("Total Head Movement:", movement)

    print("\nC-LOOK")
    seq, movement = clook(requests, head)
    print("Sequence:", seq)
    print("Total Head Movement:", movement)

    print("\nRSS")
    seq, movement = rss(requests, head)
    print("Sequence:", seq)
    print("Total Head Movement:", movement)


class File:
    def __init__(self, name, content, blocks):
        self.name = name
        self.content = content
        self.blocks = blocks


class SimpleFileSystem:
    def __init__(self, total_blocks=20):
        self.total_blocks = total_blocks
        self.free_blocks = list(range(total_blocks))
        self.directory = {}

    def create_file(self, name, content):
        if name in self.directory:
            print("Error: File already exists.")
            return

        required_blocks = max(1, len(content))

        if required_blocks > len(self.free_blocks):
            print("Error: Not enough free blocks.")
            return

        allocated = self.free_blocks[:required_blocks]
        self.free_blocks = self.free_blocks[required_blocks:]

        new_file = File(name, content, allocated)
        self.directory[name] = new_file

        print(f"File '{name}' created successfully.")
        print("Allocated blocks:", allocated)

    def read_file(self, name):
        if name not in self.directory:
            print("Error: File does not exist.")
            return

        file = self.directory[name]

        print("\nFile Name:", file.name)
        print("Content:", file.content)
        print("Blocks:", file.blocks)

    def delete_file(self, name):
        if name not in self.directory:
            print("Error: File does not exist.")
            return

        file = self.directory[name]

        self.free_blocks.extend(file.blocks)
        self.free_blocks.sort()

        del self.directory[name]

        print(f"File '{name}' deleted successfully.")

    def list_directory(self):
        print("\n========== DIRECTORY ==========")

        if not self.directory:
            print("Directory is empty.")
            return

        for name, file in self.directory.items():
            print(
                f"Name: {file.name} | "
                f"Size: {len(file.content)} | "
                f"Blocks: {file.blocks}"
            )

    def show_blocks(self):
        print("\n========== BLOCK STATUS ==========")

        used_blocks = set()

        for file in self.directory.values():
            used_blocks.update(file.blocks)

        for block in range(self.total_blocks):
            if block in used_blocks:
                print(f"Block {block}: USED")
            else:
                print(f"Block {block}: FREE")


def file_system_menu():
    fs = SimpleFileSystem(20)

    while True:
        print("\n========== SIMPLE FILE SYSTEM ==========")
        print("1. Create File")
        print("2. Read File")
        print("3. Delete File")
        print("4. List Directory")
        print("5. Show Block Status")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter file name: ")
            content = input("Enter file content: ")
            fs.create_file(name, content)

        elif choice == "2":
            name = input("Enter file name: ")
            fs.read_file(name)

        elif choice == "3":
            name = input("Enter file name: ")
            fs.delete_file(name)

        elif choice == "4":
            fs.list_directory()

        elif choice == "5":
            fs.show_blocks()

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n======================================")
        print("       OPERATING SYSTEM PROJECT")
        print("======================================")
        print("1. Disk Scheduling")
        print("2. Simple File System")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            disk_scheduling()

        elif choice == "2":
            file_system_menu()

        elif choice == "3":
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
