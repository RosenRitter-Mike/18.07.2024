import statistics as st
import numpy as np

t_list: list[float] = [];
while True:
    temp: float = float(input("Input temperature: "));
    if temp == -999:
        break;
    elif temp > 50 or temp < -50:
        continue;
    else:
        t_list.append(temp);

print(f"before concat: {t_list}");
more_numbers: list[float] = [-20.0, 39.1, 18.5];
t_list.extend(more_numbers);
print(f"after concat: {t_list}");
print(f"max(t_list) = {max(t_list)}");
print(f"min(t_list) = {min(t_list)}");
print(f"sum(t_list) = {sum(t_list)}");
print(f"len(t_list) = {len(t_list)}");
print(f"mean value of t_list: {st.mean(t_list) : .2f}");

print(f"before deletion: {t_list}");
del t_list[0];
print(f"after deletion: {t_list}");

print(f"before removal of 18.5: {t_list}");
t_list.remove(18.5);
print(f"after removal: {t_list}");

print(f"last temperature: {t_list[-1]}");
temp_last: float = t_list.pop();
print(f'popped temperature: {temp_last}');
print(f"new last temperature: {t_list[-1]}");

clone = t_list.copy()
clone.sort(reverse=True)
print(f"after sort reverse [clone]: {clone}");

'''

m.מה ההבדל ביןsortלביןsorted

One changes the list (sort), 
while the other returns a new list which is a copy of the list and which is sorted (sorted). 

n.איזה טיפוס מחזירה פונקצייתreversed? כיצד ניתן להפוך אותו לרשימה?

The reversed() function returns a reversed iterator object.
list(reversed(name_of_your_list)) turns the iterator object into a list.

'''