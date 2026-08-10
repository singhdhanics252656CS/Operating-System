print("S113 Dhani Singh")
from collections import deque

processes = [
    ("P1", 0, 5),
    ("P2", 4, 2),
    ("P3", 5, 4)
]

quantum = 2


def round_robin(processes, quantum):
    time = 0
    queue = deque()
    remaining = {p[0]: p[2] for p in processes}
    completion = {}
    i = 0

    while len(completion) < len(processes):
        while i < len(processes) and processes[i][1] <= time:
            queue.append(processes[i][0])
            i += 1

        if not queue:
            time = processes[i][1]
            continue

        pid = queue.popleft()
        run = min(quantum, remaining[pid])
        time += run
        remaining[pid] -= run

        while i < len(processes) and processes[i][1] <= time:
            queue.append(processes[i][0])
            i += 1

        if remaining[pid] > 0:
            queue.append(pid)
        else:
            completion[pid] = time

    return completion


def fcfs(processes):
    time = 0
    completion = {}

    for pid, arrival, burst in processes:
        if time < arrival:
            time = arrival

        time += burst
        completion[pid] = time

    return completion


def display(title, processes, completion):
    total_tat = 0
    total_wt = 0

    print("\n" + title)
    print("-" * 75)
    print(f"{'Process':<10}{'Arrival':<12}{'Burst':<10}{'Completion':<15}{'Turnaround':<15}{'Waiting':<10}")
    print("-" * 75)

    for pid, arrival, burst in processes:
        tat = completion[pid] - arrival
        wt = tat - burst

        total_tat += tat
        total_wt += wt

        print(f"{pid:<10}{arrival:<12}{burst:<10}{completion[pid]:<15}{tat:<15}{wt:<10}")

    print("-" * 75)
    print(f"Average Turnaround Time: {total_tat / len(processes):.2f} ms")
    print(f"Average Waiting Time:    {total_wt / len(processes):.2f} ms")


rr_completion = round_robin(processes, quantum)
fcfs_completion = fcfs(processes)

display("ROUND ROBIN", processes, rr_completion)
display("FCFS", processes, fcfs_completion)
