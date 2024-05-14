import sys
import random

def read_requests(filename):
    with open(filename, 'r') as f:
        requests = [int(line.strip()) for line in f.readlines()]
    return requests

def generate_random_requests(filename, num_requests, max_cylinder):
    requests = [random.randint(0, max_cylinder) for _ in range(num_requests)]
    with open(filename, 'w') as f:
        for request in requests:
            f.write(f"{request}\n")

def fcfs(requests, initial_position):
    current_position = initial_position
    total_head_movement = 0
    for request in requests:
        total_head_movement += abs(request - current_position)
        current_position = request
    return total_head_movement

def scan(requests, initial_position, max_cylinder):
    total_head_movement = 0
    current_position = initial_position

    left = [r for r in requests if r <= current_position]
    right = [r for r in requests if r > current_position]

    # Moving towards the innermost cylinder first
    left.sort(reverse=True)
    for request in left:
        total_head_movement += abs(request - current_position)
        current_position = request

    # After reaching the innermost cylinder, moving towards the outermost cylinder
    for request in right:
        total_head_movement += abs(request - current_position)
        current_position = request

    return total_head_movement

def c_scan(requests, initial_position, max_cylinder):
    total_head_movement = 0
    current_position = initial_position

    right = [r for r in requests if r >= current_position]
    left = [r for r in requests if r < current_position]

    # Moving towards the outermost cylinder first
    for request in right:
        total_head_movement += abs(request - current_position)
        current_position = request

    # Jump to the beginning (simulate circular)
    if left:
        total_head_movement += abs(max_cylinder - current_position)  # Move to max
        total_head_movement += max_cylinder  # Move from max to 0
        current_position = 0

        for request in left:
            total_head_movement += abs(request - current_position)
            current_position = request

    return total_head_movement


def main():
    max_cylinder = 4999
    initial_position = random.randint(0, max_cylinder)
    request_file = "numbers.txt"

    # Generate random requests if the file does not exist
    try:
        requests = read_requests(request_file)
    except FileNotFoundError:
        print(f"{request_file} not found, generating random requests.")
        generate_random_requests(request_file, 1000, max_cylinder)
        requests = read_requests(request_file)

    print(f"Initial Position: {initial_position}")
    print("FCFS Total Head Movement:", fcfs(requests, initial_position))
    print("SCAN Total Head Movement:", scan(requests, initial_position, max_cylinder))
    print("C-SCAN Total Head Movement:", c_scan(requests, initial_position, max_cylinder))

    sorted_req = requests.sort()

    print(f"Initial Position: {initial_position}")
    print("FCFS Total Head Movement:", fcfs(requests, initial_position))
    print("SCAN Total Head Movement:", scan(requests, initial_position, max_cylinder))
    print("C-SCAN Total Head Movement:", c_scan(requests, initial_position, max_cylinder))



if __name__ == "__main__":
    main()

