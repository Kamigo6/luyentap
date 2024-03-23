def calculate_priority(item_type):
    if item_type.islower():
        return ord(item_type) - ord('a') + 1
    else:
        return ord(item_type) - ord('A') + 27

def sum_of_priorities(rucksack_contents):
    total_priority = 0
    for rucksack in rucksack_contents:
        first_compartment = rucksack[:len(rucksack)//2]
        second_compartment = rucksack[len(rucksack)//2:]

        common_items = set(first_compartment) & set(second_compartment)

        for item_type in common_items:
            total_priority += calculate_priority(item_type)

    return total_priority

def main():
    # Read rucksack contents from file
    # Update with file path
    file_path = "input-01.txt" 
    with open(file_path, 'r') as file:
        rucksack_contents = [line.strip() for line in file]

    total_priority = sum_of_priorities(rucksack_contents)
    print(total_priority)


if __name__ == "__main__":
    main()
