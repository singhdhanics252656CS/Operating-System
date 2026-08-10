print("S113 Dhani Singh")
from collections import deque


def fcfs(processes):
    time = 0
    results = []
    context_switches = 0
    previous = None

    for p in processes:
        pid = p["pid"]
        arrival = p["arrival"]
        burst = p["burst"]

        if time < arrival:
            time = arrival

        start = time
        completion = time + burst
        turnaround = completion - arrival
        response = start - arrival

        if previous is not None and previous != pid:
            context_switches += 1

        previous = pid
        time = completion

        results.append({
            "pid": pid,
            "completion": completion,
            "turnaround": turnaround,
            "response": response
        })

    return results, context_switches


def round_robin(processes, quantum):
    processes = sorted(processes, key=lambda x: x["arrival"])

    n = len(processes)
    remaining = {p["pid"]: p["burst"] for p in processes}
    first_start = {p["pid"]: None for p in processes}
    completion = {}

    ready_queue = deque()

    time = 0
    index = 0
    context_switches = 0
    previous = None

    while len(completion) < n:

        while index < n and processes[index]["arrival"] <= time:
            ready_queue.append(processes[index]["pid"])
            index += 1

        if not ready_queue:
            if index < n:
                time = processes[index]["arrival"]
                continue

        pid = ready_queue.popleft()

        if previous is not None and previous != pid:
            context_switches += 1

        if first_start[pid] is None:
            first_start[pid] = time

        previous = pid

        run_time = min(quantum, remaining[pid])
        time += run_time
        remaining[pid] -= run_time

        while index < n and processes[index]["arrival"] <= time:
            ready_queue.append(processes[index]["pid"])
            index += 1

        if remaining[pid] == 0:
            completion[pid] = time
        else:
            ready_queue.append(pid)

    results = []

    for p in processes:
        pid = p["pid"]
        turnaround = completion[pid] - p["arrival"]
        response = first_start[pid] - p["arrival"]

        results.append({
            "pid": pid,
            "completion": completion[pid],
            "turnaround": turnaround,
            "response": response
        })

    return results, context_switches


def display_results(name, results, context_switches):
    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    print(
        f"{'PID':<8}"
        f"{'Completion':<15}"
        f"{'Turnaround':<15}"
        f"{'Response':<15}"
    )

    total_turnaround = 0
    total_response = 0

    for r in results:
        print(
            f"{r['pid']:<8}"
            f"{r['completion']:<15}"
            f"{r['turnaround']:<15}"
            f"{r['response']:<15}"
        )

        total_turnaround += r["turnaround"]
        total_response += r["response"]

    n = len(results)

    print("-" * 60)
    print(f"Average Turnaround Time : {total_turnaround / n:.2f}")
    print(f"Average Response Time   : {total_response / n:.2f}")
    print(f"Context Switches        : {context_switches}")


def main():
    processes = [
        {"pid": "P1", "arrival": 0, "burst": 8},
        {"pid": "P2", "arrival": 1, "burst": 4},
        {"pid": "P3", "arrival": 2, "burst": 9},
        {"pid": "P4", "arrival": 3, "burst": 5},
    ]

    quantum = 3

    fcfs_results, fcfs_switches = fcfs(processes)
    rr_results, rr_switches = round_robin(processes, quantum)

    display_results("FCFS Scheduling", fcfs_results, fcfs_switches)
    display_results("Round Robin Scheduling", rr_results, rr_switches)

    fcfs_avg_tat = sum(
        r["turnaround"] for r in fcfs_results
    ) / len(fcfs_results)

    rr_avg_tat = sum(
        r["turnaround"] for r in rr_results
    ) / len(rr_results)

    fcfs_avg_response = sum(
        r["response"] for r in fcfs_results
    ) / len(fcfs_results)

    rr_avg_response = sum(
        r["response"] for r in rr_results
    ) / len(rr_results)

    print("\n" + "=" * 60)
    print("FCFS vs Round Robin")
    print("=" * 60)

    print(f"{'Metric':<25}{'FCFS':<15}{'Round Robin':<15}")
    print("-" * 55)

    print(
        f"{'Avg Turnaround Time':<25}"
        f"{fcfs_avg_tat:<15.2f}"
        f"{rr_avg_tat:<15.2f}"
    )

    print(
        f"{'Avg Response Time':<25}"
        f"{fcfs_avg_response:<15.2f}"
        f"{rr_avg_response:<15.2f}"
    )

    print(
        f"{'Context Switches':<25}"
        f"{fcfs_switches:<15}"
        f"{rr_switches:<15}"
    )


if __name__ == "__main__":
    main()
