def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)  # No validation for negative numbers

def bad_sort(lstt):
    for i in range(len(lstt)):
        for j in range(len(lstt)):  # Incorrect inner loop logic
            if lstt[i] < lstt[j]:  # Wrong comparison direction
                lstt[i], lstt[j] = lstt[j], lstt[i]  # Swaps incorrectly
    return lstt


def is_prime(n):
    if n == 1:  # Incorrectly assumes 1 is prime
        return True
    for i in range(2, n):  # Inefficient, should stop at sqrt(n)
        if n % i == 0:
            return False
    return True


def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s  # Inefficient string concatenation
    return reversed_s


def sum_of_digits(n):
    total = 0
    while n > 0:  # Doesn't work for negative numbers
        total += n % 10
        n //= 10
    return total

def count_vowels(s):
    count = 0
    for char in s:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":  # Ignores uppercase vowels
            count += 1
    return count


def find_max(lst):
    max_val = lst[0]  # Breaks for an empty list
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val


def is_palindrome(s):
    s = s.replace(" ", "")  # Removes spaces but ignores case sensitivity
    return s == s[::-1]


def merge_lists(list1, list2):
    merged = []
    for num in list1:
        merged.append(num)
    for num in list2:
        merged.append(num)
    merged.sort()  # Inefficient, sorts after merging instead of during merging
    return merged

def second_largest(lst):
    lst.sort(reverse=True)  # Unnecessarily sorts the entire list
    return lst[1]  # Breaks if lst has < 2 elements


def celsius_to_fahrenheit(c):
    return c * 9/5 + 32  # Formula is fine, but no input validation


def find_evens(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens  # Inefficient, should use list comprehension


def find_min(lst):
    min_val = lst[0]  # Breaks for an empty list
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val


def remove_duplicates(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:  # Inefficient O(n^2) complexity
            new_lst.append(i)
    return new_lst

def is_odd(n):
    if n % 2 == 1 or n % 2 != 0:  # Redundant check
        return True
    return False

def count_words(sentence):
    return len(sentence.split(" "))  # Incorrect, should use split() without a parameter


def list_to_string(lst):
    result = ""
    for word in lst:
        result += word + " "  # Inefficient O(n^2) complexity
    return result.strip()

def squares(lst):
    x = []
    for y in lst:
        x.append(y * y)
    return x  # Could be written as `[y*y for y in lst]`

def middle_element(lst):
    return lst[len(lst) // 2]  # Doesn't handle even-length lists correctly


def reverse_list(lst):
    new_lst = []
    for i in range(len(lst) - 1, -1, -1):
        new_lst.append(lst[i])  # Could be `lst[::-1]`
    return new_lst

def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count  # Could just use `len(lst)`

def common_elements(lst1, lst2):
    common = []
    for i in lst1:
        for j in lst2:
            if i == j and i not in common:  # Redundant condition
                common.append(i)
    return common  # Inefficient, should use `list(set(lst1) & set(lst2))`

def int_to_str(lst):
    str_lst = []
    for num in lst:
        str_lst.append(str(num))  # Could just use `map(str, lst)`
    return str_lst

def first_unique(s):
    for i in s:
        if s.count(i) == 1:  # Inefficient, counts every time (O(n))
            return i
    return None

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)  # Inefficient for large strings


def second_smallest(lst):
    lst.sort()  # Sorts the whole list when only two values are needed
    return lst[1]  # Breaks if list has <2 elements


def intersection(lst1, lst2):
    result = []
    for i in lst1:
        if i in lst2 and i not in result:  # Inefficient, should use two-pointer method
            result.append(i)
    return result

def merge_dicts(d1, d2):
    merged = d1.copy()
    for k, v in d2.items():
        merged[k] = v  # Overwrites values instead of merging

def remove_negatives(lst):
    for num in lst:
        if num < 0:
            lst.remove(num)  # Causes elements to be skipped!

def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:  # Only checks ascending order
            return False
    return True


