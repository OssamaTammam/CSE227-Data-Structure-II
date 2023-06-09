import random
import time

import pandas as pd

import HeapSort
import HybridMergeSelection
import InsertionSort
import MergeSort
import QuickSort
import SelectionSort


def generateRandomArray(size):
    randomArray = []
    for i in range(size):
        temp = random.randint(0, 1000)
        randomArray.append(temp)
    return randomArray


def isSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            return False
    return True


def copyArray(original, clone):
    clone.clear()
    clone.extend(original)


if __name__ == '__main__':
    originalArray = generateRandomArray(10)
    tempArray = []
    print(f"Original array is {originalArray}")
    print("---------------------------------------------------------------------------")

    # quick sort algorithm
    copyArray(originalArray, tempArray)
    start = time.time()
    QuickSort.quickSort(tempArray, 0, len(tempArray) - 1)
    end = time.time()
    runningTime = (end - start) * 1000
    print(
        f"Running time for Quick Sort is {runningTime} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    print("---------------------------------------------------------------------------")

    # merge sort algorithm
    copyArray(originalArray, tempArray)
    start = time.time()
    MergeSort.mergeSort(tempArray)
    end = time.time()
    runningTime = (end - start) * 1000
    print(
        f"Running time for Merge Sort is {runningTime} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    print("---------------------------------------------------------------------------")

    # heap sort algorithm
    copyArray(originalArray, tempArray)
    start = time.time()
    HeapSort.heapSort(tempArray)
    end = time.time()
    runningTime = (end - start) * 1000
    print(
        f"Running time for Heap Sort is {runningTime} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    print("---------------------------------------------------------------------------")

    # selection sort algorithm
    copyArray(originalArray, tempArray)
    start = time.time()
    SelectionSort.selectionSort(tempArray)
    end = time.time()
    runningTime = (end - start) * 1000
    print(
        f"Running time for Selection Sort is {runningTime} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    print("---------------------------------------------------------------------------")

    # insertion sort algorithm
    copyArray(originalArray, tempArray)
    start = time.time()
    InsertionSort.insertionSort(tempArray)
    end = time.time()
    runningTime = (end - start) * 1000
    print(
        f"Running time for Insertion Sort is {runningTime} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    print("---------------------------------------------------------------------------")

    # hybrid merge and selection sort algorithm
    copyArray(originalArray, tempArray)
    start = time.time()
    HybridMergeSelection.hybridMergeSelection(tempArray, 6)
    end = time.time()
    runningTime = (end - start) * 1000
    print(
        f"Running time for Hybrid Merge and Selection Sort is {runningTime} ms \nArray after sorting is {tempArray}\nIs sorted = {isSorted(tempArray)}")
    print("---------------------------------------------------------------------------")

    # find kth smallest element algorithm
    copyArray(originalArray, tempArray)
    start = time.time()
    k = QuickSort.findKthElement(tempArray, 0, len(tempArray) - 1, 3)
    end = time.time()
    runningTime = (end - start) * 1000
    print(
        f"Running time for Finding Kth (200th) Smallest Element is {runningTime} ms \nKth smallest element is {k}")
    print("---------------------------------------------------------------------------")

    quickSortTime = []
    mergeSortTime = []
    heapSortTime = []
    selectionSortTime = []
    insertionSortTime = []
    arraySizes = []
    arraySize = 1000

    calcTimeStart = time.time()

    while arraySize <= 10000:
        originalArray = generateRandomArray(arraySize)

        # quick sort running time
        copyArray(originalArray, tempArray)
        start = time.time()
        QuickSort.quickSort(tempArray, 0, len(tempArray) - 1)
        end = time.time()
        runningTime = (end - start) * 1e6

        quickSortTime.append(runningTime)

        # merge sort running time
        copyArray(originalArray, tempArray)
        start = time.time()
        MergeSort.mergeSort(tempArray)
        end = time.time()
        runningTime = (end - start) * 1e6

        mergeSortTime.append(runningTime)

        # heap sort running time
        copyArray(originalArray, tempArray)
        start = time.time()
        HeapSort.heapSort(tempArray)
        end = time.time()
        runningTime = (end - start) * 1e6

        heapSortTime.append(runningTime)

        # selection sort running time
        copyArray(originalArray, tempArray)
        start = time.time()
        SelectionSort.selectionSort(tempArray)
        end = time.time()
        runningTime = (end - start) * 1e6

        selectionSortTime.append(runningTime)

        # insertion sort running time
        copyArray(originalArray, tempArray)
        start = time.time()
        InsertionSort.insertionSort(tempArray)
        end = time.time()
        runningTime = (end - start) * 1e6

        insertionSortTime.append(runningTime)

        arraySizes.append(arraySize)
        arraySize += 1000

    calcTimeEnd = time.time()
    try:
        df = pd.DataFrame({'Input Size (N)': arraySizes,
                           'Quick Sort': quickSortTime,
                           'Merge Sort': mergeSortTime,
                           'Heap Sort': heapSortTime,
                           'Selection Sort': selectionSortTime,
                           'Insertion Sort': insertionSortTime}).T
        df.to_excel(excel_writer="running_times.xlsx")
    except:
        print("Error while writing to excel file")

    print(f"Time for all calculations is {calcTimeEnd - calcTimeStart} seconds")
