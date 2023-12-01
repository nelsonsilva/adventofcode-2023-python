"""https://adventofcode.com/2023/day/1"""

INPUT = [line.rstrip() for line in open("day1.txt", encoding="utf-8")]

TEST_INPUT = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

def get_calibration_values(input):
  return [int(d[0] + d[-1]) for d in [list(filter(str.isdigit, l)) for l in input]]

# Part 1
def test_calibration():
    assert get_calibration_values(TEST_INPUT) == [12, 38, 15, 77]

print(sum(get_calibration_values(INPUT)))

# Part 2
NUMBERS = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
}

def find_numbers(line):
  res = ""
  for i in range(len(line)):
    if line[i].isdigit():
      res += line[i]
      continue
    for n in NUMBERS:
      if line[i::].startswith(n):
        res += str(NUMBERS[n])
  return res

      
TEST_INPUT_2 = [
  "two1nine",
  "eightwothree",
  "abcone2threexyz",
  "xtwone3four",
  "4nineeightseven2",
  "zoneight234",
  "7pqrstsixteen",
]

def test_find_numbers():
  assert find_numbers("eightwothree") == "823"
  
def test_fixed_calibration():
  fixed = [find_numbers(l) for l in TEST_INPUT_2]
  assert get_calibration_values(fixed) == [29, 83, 13, 24, 42, 14, 76]
  
print(sum(get_calibration_values([find_numbers(l) for l in INPUT])))