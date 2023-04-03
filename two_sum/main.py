def two_sum(nums: list[int], target: int):
    for i in range(len(nums)):
        for y in range(len(nums)):
            if y == 0:
                continue
            if (nums[i] + nums[y]) == target:
                if i == y:
                    continue
                return [i, y]


def unit_tests():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1], "❌ fuck"
    print("✅ passed!!!")
    assert two_sum([3, 2, 4], 6) == [1, 2], "❌ fuck"
    print("✅ passed!!!")
    assert two_sum([3, 3], 6) == [0, 1], "❌ fuck"
    print("✅ passed!!!")


if __name__ == '__main__':
    unit_tests()
