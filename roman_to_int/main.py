# https://leetcode.com/problems/roman-to-integer/

rn = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def romanToInt(s: str):
    total = 0
    for i in range(len(s)):
        if (i == len(s) - 1) or rn[s[i]] >= rn[s[i + 1]]:
            total += rn[s[i]]
        else:
            total -= rn[s[i]]
    return total


def unit_tests():
    assert romanToInt("III") == 3, "❌ fuck on III"
    print("✅ III passed!!!")
    assert romanToInt("LVIII") == 58, "❌ fuck on LVIII"
    print("✅ LVIII passed!!!")
    assert romanToInt("MCMXCIV") == 1994, "❌ fuck on MCMXCIV"
    print("✅ LVIII passed!!!")


if __name__ == "__main__":
    unit_tests()
