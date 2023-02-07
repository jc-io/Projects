# DESIGN PROCESS

## DESCRIPTION OF num\_arrays.c
Total of 9 fuctions

Order of functions

- int maximum()
- int sum\_positive()
- int max\_num()
- int sum\_pos\_nums()
- int negative\_count()
- int reduce()
- int maximum\_with\_reduce()
- int sum\_positive\_with\_reduce()
- int count\_negative\_with\_reduce()

To run this program, the user must have pig\_game.c and input.txt.

### STEPS

1. Include necessary header files in num\_arrays.c: stdio.h
2. Code the function maximum()

This function will take an array of numbers.

It will then return the largest number in the array of numbers.

pseudocode:
```
def maximum(num_array, len(num_array)):
    current_max_num = num_array[0]
    for i in range(len(num_array)):
        if num_array[i] > current_max_num:
            current_max_num = num_array[i]
        else:
            current_max_num = current_max_num
    return current_max_num
```

3. Code the function sum\_positive()

This function will take an array of numbers.

It will then return the sum of all postive numbers in the array of
numbers.

pseudocode:
```
def sum_postive(num_array, len(num_array)):
    current total = 0
    for i in range(len(num_array)):
        if num_array[i] > 0:
            current_total += num_array[i]:
        else:
            current_total = current total
    return current_total
```

4. In order to to find the formula of the reduce(), I first programed
the functions maximum\_with\_reduce() and sum\_positive\_with\_reduce()
using the logic of the functions maximum() and sum\_positive() as a basis.

5. I then created functions that contained the logic each reduce type function
would use.

For maximum\_with\_reduce() there is max\_num(), maximum\_with\_reduce will then call max\_num() as an element in reduce().

max\_num() will return largest number.

pseudocode:
```
def max_num(curr, next):
    if curr > next:
        return curr
    return next

def maximum_with_reduce(num_array, len(num_array)):
    return reduce(num_array, len(num_array), max_num(), num_array[0])
```

For sum\_positive\_with\_reduce() there is sum\_pos\_nums(),

sum\_positive\_with\_reduce() will then call max\_num() as an element in reduce().

sum\_pos\_nums() will return the sum of the total postive numbers.

pseudocode:
```
def sum_pos_nums(min, next):
    if next > 0:
        return next + min
    return min

def sum_positive_with_reduce(num_array, len(num_array)):
    return reduce(num_array, len(num_array), sum_pos_nums(), num_array[0])
```

6. From here, the formula can be created and coded into reduce().

This function will take the array of numbers, the length of that array,
the function that is called, and the initial variable the function sets.

pseudocode:
```
def reduce(num_array, len(num_array), function, initial):
    for i in range(len(num_array)):
        initial = function(initial, num-array[i]
    return initial
```

7. After reduce() is done, count\_negative\_with\_reduce() can be completed as well.

Following the same format of maximum\_with\_reduce() and sum\_positive\_with\_reduce(), there will be another function containing the logic tht will be performed.

negative\_count\_with\_reduce() will then call negative\_count() as an element in
reduce().

negative\_count will return current number of negative numbers in the array.

pseudocode:
```
def negative_count(count, next_num):
    if nex_num < 0:
        return count += 1
    return count
```

8. To run the program, enter in any number of integers into input.txt with one on each line. Then, either using clang or a makefile, make the
file pig\_game from pig\_game.c

Run ./pig\_game in the terminal

An example output will be:
```
Calling maximum on the numbers!
got: 93
Calling sum_positive on the numbers!
got: 342
Calling maximum_with_reduce on the numbers!
got: 93
Calling sum_positive_with_reduce on the numbers!
got: 342
Calling count_negative_with_reduce on the numbers!
got: 12
```
