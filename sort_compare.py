import argparse
# other imports go here

import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    

def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue



def shellSort(a_list):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)

        print("After increments of size", sublistcount, "The list is",alist)

        sublistcount = sublistcount // 2





def python_sort(a_list):
    """
    Use Python built-in sorted function

    :param a_list:
    :return: the sorted list
    """
    return sorted(a_list)

def benchmark_sort(sort_func, the_size):
    total_time = 0
    for i in range(100):
        mylist = get_me_random_lis(the_size)
        start = time.time()
        sort_func(mylist)
        time_spent = time.time() - start
        total_time += time_spent

avg_time = total_time / 100
print(f"{sort_func.__name__} took {avg_time:10.7f} second to run, on average for a list of {the_size} elements")



if __name__ == "__main__":
    """Main entry point"""
    list_sizes = [500, 1000, 5000]

    # the_size = list_sizes[0]

    for the_size in list_sizes:
        print(f"Testing sorting algorithms with list size {the_size}:")

        benchmark_sort(python_sort, the_size)
        benchmark_sort(insertion_sort, the_size)

        total_time = 0
        for i in range(100):
            mylist = get_me_random_list(the_size)
            start = time.time()
            shellsort(mylist)
            time_spent = time.time() - start
            total_time += time_spent

        # Repeat the same loop and use shellSort(...)

        avg_time = total_time / 100
        print(f"Shell sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        print("-" * 50)
