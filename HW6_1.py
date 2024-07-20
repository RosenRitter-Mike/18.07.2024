numbers: list[int] = [i for i in range(80,100)];
print(f"first number: {numbers[0]}");
print(f"last number: {numbers[-1]}");
print(f"numbers list length: {len(numbers)}");
print(f"numbers[3:12]: {numbers[3:12]}");
print(f"numbers[3:]: {numbers[3:]}");
print(f"numbers[:9]: {numbers[:9]}");
numbers.insert(10, 999)
print(f"number in the middle: {numbers[10]}");
print(f"numbers in reverse order: {numbers[::-1]}");
print(f"numbers in odd indexes: {numbers[::2]}");