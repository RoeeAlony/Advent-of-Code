"""
Advent of Code 2024 - Day 5: Print Queue
Processes page ordering rules and validates update sequences.
"""

from collections import defaultdict
from pathlib import Path
from typing import List, Set, Dict


class PrintQueueValidator:
    """A class to validate print queue ordering based on page dependencies."""

    def __init__(self) -> None:
        # Key: page number, Value: set of pages that must come before this page
        self._ordering_rules: Dict[int, Set[int]] = defaultdict(set)

    def parse_input(self, file_path: str) -> tuple[List[str], List[str]]:
        """Parse input file into rules and updates sections."""
        input_file = Path(__file__).parent / file_path

        with input_file.open('r', encoding='utf-8') as file:
            content = file.read().strip()

        if not content:
            raise ValueError("Input file is empty")

        sections = content.split('\n\n')
        if len(sections) != 2:
            raise ValueError("Expected two sections separated by empty line")

        rules_section, updates_section = sections
        return rules_section.splitlines(), updates_section.splitlines()

    def process_rules(self, rules_data: List[str]) -> None:
        """Process page ordering rules into dependency mapping."""
        for rule in rules_data:
            if '|' not in rule:
                continue

            try:
                left, right = map(int, rule.split('|'))
                self._ordering_rules[right].add(left)
            except ValueError as e:
                raise ValueError(f"Invalid rule format: {rule}") from e

    def is_valid_update(self, pages: List[int]) -> bool:
        """Check if an update sequence follows all ordering rules."""
        if not pages:
            return True

        seen_pages: Set[int] = set()
        pages_set = set(pages)

        for page in pages:
            # Check if this page has ordering requirements
            required_pages = self._ordering_rules.get(page, set())

            # Check if any required page that exists in this update hasn't been seen yet
            missing_dependencies = required_pages & pages_set - seen_pages
            if missing_dependencies:
                return False

            seen_pages.add(page)

        return True

    def get_middle_page(self, pages: List[int]) -> int:
        """Get the middle page from a list of pages."""
        return 0 if not pages else pages[len(pages) // 2]

    def process_updates(self, updates_data: List[str]) -> int:
        """Process all updates and return sum of middle pages from valid updates."""
        valid_updates = []

        for update in updates_data:
            if not update.strip():
                continue

            try:
                pages = [int(page.strip()) for page in update.split(',')]
                if self.is_valid_update(pages):
                    valid_updates.append(pages)
            except ValueError as e:
                print(f"Warning: Skipping invalid update '{update}': {e}")
                continue

        return sum(self.get_middle_page(update) for update in valid_updates)

    def solve(self, input_file: str) -> int:
        """Main solving method that coordinates the entire process."""
        try:
            rules_data, updates_data = self.parse_input(input_file)
            self.process_rules(rules_data)
            return self.process_updates(updates_data)
        except Exception as e:
            print(f"Error solving puzzle: {e}")
            raise


def main() -> None:
    """Main function to run the print queue validator."""
    validator = PrintQueueValidator()

    try:
        result = validator.solve('input.txt')
        print(f"Sum of middle pages from valid updates: {result}")
    except Exception as e:
        print(f"Failed to solve: {e}")
        return


if __name__ == "__main__":
    main()
