# -python-assignment5
### TASK 1
1. **Dictionary Lookup**: It initializes a dictionary (`dictionary`) that contains student names as keys and their marks as values. Here, `"Alice"` is stored with a score of `85`.

2. **User Input Handling**: The program prompts the user to enter a student's name with the first letter capitalized. The input is stored in the variable `name`.

3. **Data Retrieval & Exception Handling**:
   - The program tries to fetch the marks of the student using `dictionary[name]`.
   - If the name exists in the dictionary, it prints their marks.
   - If the name does **not** exist (causing a `KeyError`), it gracefully handles the error with an `except` block, printing `"Student not found"` instead of crashing.


### TASK 2 
This Python program demonstrates **list slicing and reversing**. Here's what it does step by step:

1. **Creates a list**: `list = [1,2,3,4,5,6,7,8,9,10]` containing numbers from `1` to `10`.

2. **Extracts the first five elements** using slicing (`list[0:5]`), assigning them to `reversedslice`.  
   - `reversedslice = [1, 2, 3, 4, 5]`

3. **Reverses the extracted elements** using `.reverse()`.  
   - Now `reversedslice = [5, 4, 3, 2, 1]`

4. **Prints results**:
   - `"Original list:"` → `[1,2,3,4,5,6,7,8,9,10]`  
   - `"Extracted first five elements:"` → `[1, 2, 3, 4, 5]`  
   - `"Reversed extracted elements:"` → `[5, 4, 3, 2, 1]`
