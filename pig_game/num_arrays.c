#include <stdio.h>

int maximum(int *nums, int len) {
    int max_num = nums[0];
    for(int i = 0; i < len; i++) {
        if (nums[i] > max_num) {
            max_num = nums[i];
       }
    }
    return max_num;
}

int sum_positive(int *nums, int len) {
    int sum_num = 0;
    for(int i = 0; i < len; i++) {
        if (nums[i] > 0) {
            sum_num = sum_num + nums[i];
        }
    }
    return sum_num;
}

int max_num(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}

int sum_pos_nums(int min, int next_num) {
    if (next_num > 0) {
        return min + next_num;
    }
    return min;
}

int negative_count(int count, int next_num) {
    if (next_num < 0) {
        count++;
    }
    return count;
}

int reduce(int *nums, int len, int (*f)(int,int), int initial) {
    for (int i  = 0; i < len; i++) {
        initial = (*f)(initial, nums[i]);

    }
    return initial;
}

int maximum_with_reduce(int *nums, int size) {
    return reduce(nums, size, &max_num, nums[0]);
}

int sum_positive_with_reduce(int *nums, int size) {
    return reduce(nums, size, &sum_pos_nums, 0);
}

int count_negative_with_reduce(int *nums, int size) {
    
    return reduce(nums, size, &negative_count, 0);

}
