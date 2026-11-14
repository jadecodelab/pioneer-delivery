import unittest

from event_log_cleanup import maximum_removals


def is_subsequence_after_removal(source, pattern, removed_indices):
    removed = set(removed_indices)

    remaining = "".join(
        character
        for index, character in enumerate(source)
        if index not in removed
    )

    pattern_position = 0

    for character in remaining:
        if (
            pattern_position < len(pattern)
            and character == pattern[pattern_position]
        ):
            pattern_position += 1

    return pattern_position == len(pattern)


class TestEventLogCleanup(unittest.TestCase):

    def assert_valid_result(
        self,
        source,
        pattern,
        target_indices,
        expected_count
    ):
        removal_count, removed_indices = maximum_removals(
            source,
            pattern,
            target_indices
        )

        self.assertEqual(removal_count, expected_count)
        self.assertEqual(len(removed_indices), removal_count)
        self.assertEqual(len(set(removed_indices)), len(removed_indices))

        for index in removed_indices:
            self.assertIn(index, target_indices)

        self.assertTrue(
            is_subsequence_after_removal(
                source,
                pattern,
                removed_indices
            )
        )

    def test_example_1(self):
        self.assert_valid_result(
            "abbaa",
            "aba",
            [0, 1, 2],
            1
        )

    def test_example_2(self):
        self.assert_valid_result(
            "bcda",
            "d",
            [0, 3],
            2
        )

    def test_example_3_no_removals(self):
        self.assert_valid_result(
            "dda",
            "dda",
            [0, 1, 2],
            0
        )

    def test_example_4(self):
        self.assert_valid_result(
            "yeyeykyded",
            "yeyyd",
            [0, 2, 3, 4],
            2
        )

    def test_no_allowed_deletions(self):
        self.assert_valid_result(
            "abc",
            "abc",
            [],
            0
        )

    def test_repeated_characters(self):
        self.assert_valid_result(
            "aaab",
            "ab",
            [0, 1, 2],
            2
        )


if __name__ == "__main__":
    unittest.main()