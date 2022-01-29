from __future__ import annotations
import itertools


class Solution:
    LOWERCASE = set("abcdefghijklmnopqrstuvwxyz")
    UPPERCASE = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    DIGIT = set("01234567089")
    def strongPasswordChecker(self, password: str) -> int:
        chars = set(password)

        needs_lowercase = not(chars & self.LOWERCASE)
        needs_uppercase = not(chars & self.UPPERCASE)
        needs_digit = not(chars & self.DIGIT)
        num_required_type_replaces = int(
            needs_lowercase + needs_uppercase + needs_digit
            )

        num_required_inserts = max(0, 6 - len(password))
        num_required_deletes = max(0, len(password) - 20)

        # For password = '11aaabB' we have groups = [2, 3, 1, 1]
        groups = [len(list(grp)) for _, grp in itertools.groupby(password)]

        def apply_best_delete():
            argmin, _ = min(
                enumerate(groups),
                # Ignore groups of length < 3 as long as others are available.
                key=lambda it: it[1] % 3 if it[1] >= 3 else 10 - it[1],
            )
            groups[argmin] -= 1

        for _ in range(num_required_deletes):
            apply_best_delete()

        num_required_group_replaces = sum(
            group // 3
            for group in groups
        )

        return (
            num_required_deletes
            + max(
                num_required_type_replaces,
                num_required_group_replaces,
                num_required_inserts,
            )
        )
