import unittest

from src.common_friends import generate_friend_pairs

class TestCommonFriends(unittest.TestCase):
    def test_generate_friend_pairs(self):
        # User 1 with friends 2, 3, 4
        pairs = generate_friend_pairs(1, "Sidi", [2, 3, 4])
        expected = [
            ((1, 2), {2, 3, 4}),
            ((1, 3), {2, 3, 4}),
            ((1, 4), {2, 3, 4}),
        ]
        self.assertEqual(sorted(pairs), sorted(expected))

    def test_intersection(self):
        # Simulate intersection logic
        set1 = {2, 3, 4}
        set2 = {1, 3, 4}
        common = set1 & set2
        self.assertEqual(common, {3, 4})

if __name__ == "__main__":
    unittest.main()
