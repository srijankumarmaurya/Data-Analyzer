import numpy as np

class DataAnalytics:
    def __init__(self):
        self.main_array = None

    def create_array(self):
        try:
            print("Select the Type of array to Create :")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")
            choice = int(input("Enter your choice:- "))
            if choice == 1:
                element = input("Enter elements for 1D array:- ").split()
                arr = list(map(int, element))
                self.main_array = np.array(arr)
                print(f"Values in array: {self.main_array}")
                print("Array built successfully!")
                return self.main_array
            
            elif choice == 2:
                rows = int(input("Enter the number of rows for 2D array:- "))
                cols = int(input("Enter the number of columns for 2D array:- "))     
                arr = input(f"Enter {rows * cols} elements for the array, separated by spaces:- ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(rows, cols)
                self.main_array = arr2
                return self.main_array
            
            elif choice == 3:
                depth = int(input("Enter the depth for 3D array:- "))
                rows = int(input("Enter the number of rows for 3D array:- "))
                cols = int(input("Enter the number of columns for 3D array:- "))
                arr = input(f"Enter {depth * rows * cols} elements for the array, separated by spaces:- ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(depth, rows, cols)
                self.main_array = arr2
                return self.main_array
            
            else:
                print("Invalid choice!")

        except :
            print("something went wrong. Please enter the correct number of elements.")
   
    def indexing_operations(self,data):
        try:
            while True:
                print("Choose an option:")
                print("1. Indexing")
                print("2. Slicing")
                print("3. Go back to main menu")
                choice = int(input("Enter your choice: "))  

                if choice == 1:
                    if data.ndim == 1:
                        inx = int(input("Enter the index of the element to access:- "))
                        print(f"Value at index position {inx}: {data[inx]}")

                    elif data.ndim == 2:
                        row = int(input("Enter the row index:- "))
                        cols = int(input("Enter the column index:- "))
                        print(f"Value found at ({row}, {cols}): {data[row, cols]}")

                    elif data.ndim == 3:
                        dep = int(input("Enter the depth index:- "))
                        row = int(input("Enter the row index:- "))
                        cols = int(input("Enter the column index:- "))
                        print(f"Value found at position ({dep}, {row}, {cols}): {data[dep, row, cols]}")

                elif choice == 2:
                    print("Slicing")
                    if data.ndim == 1:
                        start = int(input("Enter the start index:- "))
                        end = int(input("Enter the end index:- "))
                        print(f"Sliced segment: {data[start:end]}")

                    elif data.ndim == 2:
                        row_start = int(input("Enter the start row index:- "))
                        row_end = int(input("Enter the end row index:- "))
                        col_start = int(input("Enter the start column index:- "))
                        col_end = int(input("Enter the end column index:- "))
                        print(f"Sliced grid matrix:\n{data[row_start:row_end, col_start:col_end]}")

                    elif data.ndim == 3:
                        dep_start = int(input("Enter the start depth index:- "))
                        dep_end = int(input("Enter the end depth index:- "))
                        row_start = int(input("Enter the start row index:- "))
                        row_end = int(input("Enter the end row index:- "))
                        col_start = int(input("Enter the start column index:- "))
                        col_end = int(input("Enter the end column index:- "))
                        print(f"Sliced multi-layer layout:\n{data[dep_start:dep_end, row_start:row_end, col_start:col_end]}")

                    else:
                        print("Invalid choice!")

                elif choice == 3:
                    print("Going to main menu...")
                    break

                else :
                    print("Invalid choice ")
        except :
            print("Invalid input. Please enter a valid choice.")     

    def math_operation(self, data):

        try:
            print("Choose a Mathematical Operation ")
            print()
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            choice = int(input("Enter your choice:- "))

            if choice == 1 :
                arr = input(f"Enter {data.size} elements for the second array, separated by spaces:- ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(data.shape)
                result = data + arr2
                print("Result of addition:")
                print(result)

            elif choice == 2 :
                arr = input(f"Enter {data.size} elements for the second array, separated by spaces:- ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(data.shape)
                result = data - arr2
                print("Subtraction results:")
                print(result)

            elif choice == 3 :
                arr = input(f"Enter {data.size} elements for the second array, separated by spaces:- ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(data.shape)
                result = data * arr2
                print("Multiplication results:")
                print(result)

            elif choice == 4 :
                arr = input(f"Enter {data.size} elements for the second array, separated by spaces:- ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(data.shape)
                # Check if any element in the second array is 0
                if 0 in arr2:
                    print(" Warning: Your input contains a zero. Division by zero is not defined.")
                result = data / arr2
                print("Division results:")
                print(result)

            else :
                print("Invalid choice!")
 
        except :
            print("Invalid input. Please enter a valid choice.")

    def search_arr(self, data):
        try:
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter values")

            choice = int(input("Enter your choice from 1-3 only:- "))

            if choice == 1:
                print("Original array:")
                print(data)
                search = int(input("Enter a value to search for:- "))

                if search in data:
                    print("Value found at index:")
                    arr = np.where(data == search)
                    print(arr)
                else:
                    print("Value not found in the array.")

            elif choice == 2:
                print("Current data setup:")
                print(data)
                sort_arr = np.sort(data)
                print("Data after sorting:")
                print(sort_arr)

            elif choice == 3:
                print()
                print("Choose a filter:")
                print("1. Values less than")
                print("2. Values greater than")

                choice = int(input("Enter your choice:- "))

                value = int(input("Enter the threshold value:- "))

                if choice == 1:
                    print("Initial array structure:")
                    print(data)
                    print("Matching items (lower values):")
                    less = data[data < value]
                    print(less)

                elif choice == 2:
                    print("Initial array structure:")
                    print(data)
                    print("Matching items (higher values):")
                    greater = data[data > value]
                    print(greater)
                else:
                    print("Invalid choice!")
            else :
                print("Invalid choice!")                
        except :
            print("Invalid input. Please enter a valid choice.")    

    def combine_arrays(self, data):
        try:
            print()
            print("Choose an option:")
            print("1. Combine arrays")
            print("2. Split array")

            choice = int(input("Enter your choice:- "))

            if choice == 1:
                arr = input(f"Enter {data.size} Elements for Another Array: ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(data.shape)
                print("Original Array:")
                print(data)
                print("Second Array:")
                print(arr2)
                print("Combined Array (Vertical Stack):")
                new = np.vstack((data, arr2))
                print(new)
 
            elif choice == 2:
                arr1 = int(input("Enter the Number of Splits: "))
                arr2 = np.array_split(data, arr1)
                print("Base array:")
                print(data)
                print("Split sequences:")
                print(arr2)
            else:
                print("Invalid Choice!")
        except:
            print("Something Went Wrong!")
    def Aggregates_operations(self, data):
        try:
            print()
            print("Choose an option:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("Original array:")
                print(data)
                sum_arr = np.sum(data)
                print(f"Sum of all elements: {sum_arr}")
            elif choice == 2:
                print("Target dataset:")
                print(data)
                mean_arr = np.mean(data)
                print(f"Calculated average value: {mean_arr}")
            elif choice == 3:
                print("Target dataset:")
                print(data)
                median_arr = np.median(data)
                print(f"Calculated middle point value: {median_arr}")
            else:
                print("Invalid choice!")
        except:
                print("Something went wrong!")
        print()

    def main_menu(self):
            print()
            print("-------------------------------------------------------")
            print("Welcome to Numpy Analyzer !")
            print("-------------------------------------------------------")
            print("Choose an choice :")
            print("1. Create a Numpy Array ")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays ")
            print("4. Search, Sort or Filter Arrays ")
            print("5. Compute Aggregates and Statistics ")
            print("6. Exit ")
    def start_program(self):
        while True :
                self.main_menu()
                choice = int(input("Enter Your Choice : "))
                if choice == 1:
                 self.main_array = obj.create_array()
                 obj.indexing_operations(self.main_array)
                elif choice == 2:
                 obj.math_operation(self.main_array)
                elif choice == 3:
                    obj.combine_arrays(self.main_array)
                elif choice == 4:
                  obj.search_arr(self.main_array)
                elif choice == 5:
                  obj.Aggregates_operations(self.main_array)
                elif choice == 6:
                    print("Thank You for using Numpy Analyzer! Goodbye!")
                    break
obj = DataAnalytics()
obj.start_program()
