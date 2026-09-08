"""
Advent of Code 2024 - Day 5: Print Queue
Processes page ordering rules and validates update sequences.
"""

# Global variables
is_phase2 = False
total_sum = 0
# Key: page number, Value: list of pages that must come before this page
ordering_rules: dict[int, list[int]] = {}


def main():
    """Main function to process input and coordinate the two phases."""
    global is_phase2, total_sum

    with open('input.txt', 'r') as file:
        data = file.read().strip().split('\n')

    # Split input into two phases: rules and updates
    empty_line_index = data.index('')
    rules_data = data[:empty_line_index]
    updates_data = data[empty_line_index + 1:]

    # Process ordering rules first
    process_rules(rules_data)

    # Process updates and calculate sum
    total_sum = process_updates(updates_data)

    print(f"Sum of middle pages from valid updates: {total_sum}")


def process_rules(rules_data: list[str]) -> None:
    """Process the page ordering rules."""
    global ordering_rules

    for rule in rules_data:
        if '|' in rule:
            left, right = map(int, rule.split('|'))
            if right not in ordering_rules:
                ordering_rules[right] = []
            ordering_rules[right].append(left)


def process_updates(updates_data: list[str]) -> int:
    """Process the page updates and return sum of middle pages from valid updates."""
    sum_middle_pages = 0

    for update in updates_data:
        if not update.strip():
            continue

        pages = list(map(int, update.split(',')))

        if is_valid_update(pages):
            middle_index = len(pages) // 2
            sum_middle_pages += pages[middle_index]

    return sum_middle_pages


def is_valid_update(pages: list[int]) -> bool:
    """Check if an update follows the ordering rules."""
    seen_pages: set[int] = set()

    for page in pages:
        # Check if this page has any ordering requirements
        if page in ordering_rules:
            required_pages = ordering_rules[page]
            # All required pages must have been seen before this page
            for required_page in required_pages:
                if required_page in pages and required_page not in seen_pages:
                    return False

        seen_pages.add(page)

    return True


if __name__ == "__main__":
    main()
