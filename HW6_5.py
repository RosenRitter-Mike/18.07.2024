import random as rd;

num_list: list[int] = [rd.randint(0, 10)*rd.randint(-10, 10) for _  in range(4)];
print(f"num list: {num_list}");

while True:
    try:
        choice: int = int(input("chose an index: "));
        if choice != -999:
            print(f"list member at {choice} is {num_list[choice]}");
        else:
            break;
    except Exception as e:
            # print(f"{e} is over the range of the list") if abs(e) > len(num_list) else print(f"{e} is a charecter or string");
        print(f"An {e} -- Error -- has occurred")
