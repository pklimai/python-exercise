# Convert a number to a Roman notation

n = int(input())


def f1(ones, fives, tens, num):
    return {
        0: "",
        1: ones * 1,
        2: ones * 2,
        3: ones * 3,
        4: ones + fives,
        5: fives,
        6: fives + ones,
        7: fives + ones * 2,
        8: fives + ones * 3,
        9: ones + tens,
        10: tens
    }[num]


print(f1("M", "-", "-", n // 1000) +
      f1("C", "D", "M", (n % 1000) // 100) +
      f1("X", "L", "C", (n % 100) // 10) +
      f1("I", "V", "X", n % 10))
