import random as rd;

bool_list: list[bool] = [rd.choice([True, False]) for _ in range(3)];

print(f"bool list: {bool_list}");
print(f"All True? {all(bool_list)}");
print(f"Any True? {any(bool_list)}");
print(f"All False? {not any(bool_list)}");
print(f"Any False? {not all(bool_list)}");

num_list: list[int] = [rd.randint(-2, 2) for _ in range(5)];
print(f"num list: {num_list}");
print(f"All True? {all(num_list)}");
print(f"Any True? {any(num_list)}");
print(f"All False? {not any(bool_list)}");
print(f"Any False? {not all(bool_list)}");

