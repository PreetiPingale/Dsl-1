def store_percentages():
    # Assuming user inputs the number of students
    num_students = int(input("Enter the number of students: "))
    
    # Initialize an empty list to store percentages
    percentages = []
    
    # Getting percentages of students
    for i in range(num_students):
        percentage = float(input(f"Enter percentage of student {i+1}: "))
        percentages.append(percentage)
    
    return percentages
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr
def display_top_scores(arr):
    sorted_arr = sorted(arr, reverse=True)
    print("Top 5 Scores:")
    for i in range(5):
        print(sorted_arr[i])
# Storing percentages
percentages = store_percentages()

# Sorting using Selection Sort
sorted_selection = selection_sort(percentages.copy())

# Sorting using Bubble Sort
sorted_bubble = bubble_sort(percentages.copy())

# Displaying top 5 scores
display_top_scores(percentages)
