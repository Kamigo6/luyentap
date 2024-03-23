def calculate_priority(item_type):
    if item_type.islower():
        return ord(item_type) - ord('a') + 1
    else:
        return ord(item_type) - ord('A') + 27

def find_badge_item_types(rucksack_groups):
    badge_item_types = []
    for group in rucksack_groups:
        item_counts = {}
        for rucksack in group:
            for item_type in set(rucksack):
                item_counts[item_type] = item_counts.get(item_type, 0) + 1
        common_item_type = [item_type for item_type, count in item_counts.items() if count == 3]
        badge_item_types.append(common_item_type[0])
    return badge_item_types

def sum_of_priorities(badge_item_types):
    total_priority = 0
    for item_type in badge_item_types:
        total_priority += calculate_priority(item_type)
    return total_priority

def main():
    # Read rucksack contents from file
    file_path = "input-01.txt" 
    with open(file_path, 'r') as file:
        rucksack_contents = [line.strip() for line in file]

    # Group rucksack contents into sets of three
    rucksack_groups = [rucksack_contents[i:i+3] for i in range(0, len(rucksack_contents), 3)]

    # Find badge item types for each group
    badge_item_types = find_badge_item_types(rucksack_groups)

    # Calculate sum of priorities for badge item types
    total_priority = sum_of_priorities(badge_item_types)
    print(total_priority)

if __name__ == "__main__":
    main()
