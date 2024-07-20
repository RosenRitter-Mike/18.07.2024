import random as rd;

num_list1: list[int] = [i for i in range(95, 106)];
print(f"num list 1: {num_list1}");
num_list2: list[int] = [i*2 for i in range(5, 11)];
print(f"num list 2: {num_list2}");
bool_list: list[bool] = [rd.choice([True, False]) for _ in range(5)];
print(f"bool list: {bool_list}");

bnum_list: list[int] = [n for _ in range(10) for n in [rd.randint(0, 100)] if n > 50];
print(f"nums larger then 50: {bnum_list}");

u_str: str = input("Type somthing? ");
char_list: list[str] = [c for c in u_str if c != ' ' and c != 't'];
print(f"char list: {char_list}");