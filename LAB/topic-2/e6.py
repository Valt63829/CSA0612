# Question 2: Traffic Signal Priority Queue
# Bubble Sort to Maintain Vehicle Priority

# Priority: Ambulance > Bus > Car
priority = {
    "Ambulance": 3,
    "Bus": 2,
    "Car": 1
}


def bubble_sort_queue(queue):
    n = len(queue)

    # Sort in descending order of priority
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if priority[queue[j]] < priority[queue[j + 1]]:
                queue[j], queue[j + 1] = queue[j + 1], queue[j]
                swapped = True

        if not swapped:
            break


def add_vehicle(queue, vehicle):
    queue.append(vehicle)
    bubble_sort_queue(queue)
    print(f"After adding {vehicle}: {queue}")


# -------------------------
# Example
# -------------------------
traffic_queue = []

add_vehicle(traffic_queue, "Car")
add_vehicle(traffic_queue, "Bus")
add_vehicle(traffic_queue, "Car")
add_vehicle(traffic_queue, "Ambulance")
add_vehicle(traffic_queue, "Bus")

print("\nFinal Priority Queue:", traffic_queue)


# -------------------------
# Test Cases
# -------------------------
q = []
add_vehicle(q, "Car")
add_vehicle(q, "Ambulance")
add_vehicle(q, "Bus")

assert q == ["Ambulance", "Bus", "Car"]

q = []
add_vehicle(q, "Bus")
assert q == ["Bus"]

print("\nAll test cases passed!")