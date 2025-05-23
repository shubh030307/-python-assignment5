# -python-assignment5
### TASK 1
1. **Dictionary Initialization:**  
   - The program creates a dictionary with student names as keys (`"Alice"`) and their marks as values (`85`).

2. **User Input Handling:**  
   - It prompts the user to enter a student's name, storing it in `name`.
   - The `.capitalize()` method ensures that the first letter is capitalized correctly, making lookup more reliable.

3. **Data Retrieval & Exception Handling:**  
   - It searches the dictionary using `dictionary[Name]` (where `Name` holds the capitalized version of the input).
   - If found, it prints their marks.
   - If not found, it gracefully handles the `KeyError` by displaying `"Student not found"` instead of crashing.



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
