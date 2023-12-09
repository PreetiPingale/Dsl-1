def getMax(arr):
 max = arr[0]
 for num in arr:
 if num > max:
 max = num
 return max
def countSort(arr, place):
 n = len(arr)
 output = [0] * n
 count = [0] * 10
 for i in range(n):
 count[(int) ((arr[i] / place) % 10)] += 1
 for i in range(1, 10):
 count[i] += count[i - 1]
 for i in range(n - 1, -1, -1):
 idx = count[(int) ((arr[i] / place) % 10)] - 1
 output[idx] = arr[i]
 count[(int) ((arr[i] / place) % 10)] -= 1
 # copy the array output to arr
 arr[:] = output[:]
def radixSort(arr):
 max = getMax(arr)
 for place in range(1, int(max) + 1):
 countSort(arr, place)
def main():
 # Get the number of students
 n = int(input("Enter the number of students: "))
 # Create an array to store the percentages
 percentages = []
 # Get the percentage for each student
 print("Enter percentage of students:")
 for i in range(n):
 percentage = float(input())
 percentages.append(percentage) 
# Sort the percentages in ascending order

 radixSort(percentages)

 print("Marks in ascending order: \n",percentages)

 # Display the top five scores

 print("Top 5 marks: ")

 for i in range(n - 1, n - 6, -1):

 print(percentages[i])

if __name__ == "__main__":

 main()

