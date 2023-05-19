import random
import matplotlib.pyplot as plt
class QuickSort_RP:
    def __init__(self, arr):
        self.arr = arr
        self.NumberOfSwaps = 0

    def partition(self, low, high):
        pivot_index = random.randint(low, high)  # Randomly choose pivot index
        pivot = self.arr[pivot_index]  # Select pivot element

        # Move pivot element to the beginning of the subarray
        self.arr[pivot_index], self.arr[low] = self.arr[low], self.arr[pivot_index]

        i = low + 1  # Index of the smaller element
        j = high

        while True:
            while i <= j and self.arr[i] <= pivot:
                i += 1
            while i <= j and self.arr[j] >= pivot:
                j -= 1

            if i <= j:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]  # Swap elements
                self.NumberOfSwaps += 1
            else:
                break

        self.arr[low], self.arr[j] = self.arr[j], self.arr[low]  # Move pivot to its correct position
        return j

    def quick_sort(self, low, high):
        if low < high:
            pivot_index = self.partition(low, high)  # Partition the array
            self.quick_sort(low, pivot_index - 1)  # Sort the left subarray
            self.quick_sort(pivot_index + 1, high)  # Sort the right subarray

    def sort(self):
        self.swap_count = 0  # Reset swap count
        self.quick_sort(0, len(self.arr) - 1)
        return self.NumberOfSwaps
    def Visulization(self):
        plt.bar(range(len(self.arr)), self.arr)
        plt.xlabel('Indices')
        plt.ylabel('Array Values')
        plt.title('Number of Swaps: {}'.format(self.NumberOfSwaps))
        plt.show()
    
class QuickSort_StartP(QuickSort_RP):
    def __init__(self):
        self.NumberOfSwaps = 0  # Initialize the number of swaps counter

    def quick_sort(self, array, start, end):
        """
        The main function that implements QuickSort.
        """
        if start < end:
            pivot_index = self.partition(array, start, end)
            self.quick_sort(array, start, pivot_index - 1)  # Sort elements before the pivot
            self.quick_sort(array, pivot_index + 1, end)    # Sort elements after the pivot
        return array

    def partition(self, array, low, high):
        """
        This function takes the first element as the pivot and places it at its sorted position.
        All elements smaller than the pivot are placed to the left, and all elements greater than
        the pivot are placed to the right.
        """
        pivot = array[low]
        start = low + 1
        end = high

        while True:
            # Find the element from the right side that is smaller than the pivot
            while start <= end and array[end] >= pivot:
                end = end - 1

            # Find the element from the left side that is greater than the pivot
            while start <= end and array[start] <= pivot:
                start = start + 1

            # Swap the elements if they are out of order
            if start <= end:
                array[start], array[end] = array[end], array[start]
                self.NumberOfSwaps += 1
            else:
                break

        # Move the pivot element to its correct position
        array[low], array[end] = array[end], array[low]

        # Increment the swaps counter if the pivot element is moved from its original position
        if low != end:
            self.NumberOfSwaps += 1
        return end

    def print_arr(self, arr):
        """
        Function to print the array.
        """
        for element in arr:
            print(element, end=" ")
        print()

    def Visualization(self):
        plt.bar(range(len(array)),array)
        plt.xlabel('Indices')
        plt.ylabel('Array Values')
        plt.title('Number of Swaps: {}'.format(self.NumberOfSwaps))
        plt.show()




class QuickSort_EP(QuickSort_RP):
    def __init__(self):
        self.swaps = 0  # Initialize the swaps counter

    def sort(self, arr):
        if len(arr) <= 1:
            return arr  # Base case: return the array if it has 0 or 1 element

        pivot = arr[-1]  # Select the last element of the array as the pivot
        left = []
        right = []

        for i in range(len(arr) - 1):
            if arr[i] < pivot:
                left.append(arr[i])  # Append elements smaller than the pivot to the left subarray
            else:
                right.append(arr[i])  # Append elements greater than or equal to the pivot to the right subarray
                self.swaps += 1  # Increment the swaps counter for each element moved to the right subarray

        quick_sort_left = QuickSort_EP()  # Create an instance of QuickSort_EP for sorting the left subarray
        left = quick_sort_left.sort(left)  # Recursively sort the left subarray
        quick_sort_right = QuickSort_EP()  # Create an instance of QuickSort_EP for sorting the right subarray
        right = quick_sort_right.sort(right)  # Recursively sort the right subarray

        return left + [pivot] + right  # Concatenate the sorted left subarray, pivot, and sorted right subarray

    def get_swaps(self):
        return self.swaps  # Return the total number of swaps

    def Visualization(self):
        plt.bar(range(len(self.arr)), self.arr)  # Create a bar plot of the array values
        plt.xlabel('Indices')  # Set the x-axis label
        plt.ylabel('Array Values')  # Set the y-axis label
        plt.title('Number of Swaps: {}'.format(self.NumberOfSwaps))  # Set the plot title with the number of swaps
        plt.show()  # Display the plot


'''Decreasing Order'''
# array =  [i for i in range(2000,0,-1)]
'''Increasing Order'''
array = [i for i in range(1000)]
'''Random Order'''
# array = [random.randint(1, 3000) for _ in range(3000)]



# to use class QuickSort random pivot 
# qs = QuickSort_RP(array)
# numberofswaps = qs.sort()
# qs.Visulization()
# print(qs.arr)
# print()
# print()
# print('The number of swaps is ' , numberofswaps)

# to use class QuickSort , pivot element is the first element in array 
qs = QuickSort_StartP()
print(qs.quick_sort(array, 0, len(array)-1))
print(qs.NumberOfSwaps)
qs.Visualization()
# to use class QuickSort , pivot element is the last element in array
# quicksort = QuickSort_EP()
# sorted_arr = quicksort.sort(array)
# num_swaps = quicksort.get_swaps()

# print("Sorted array:", sorted_arr)
# print("Number of swaps:", num_swaps)

