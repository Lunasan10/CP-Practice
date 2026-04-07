# Arrays
- Are made for storing many values together.
- Arrays need to store their items in **adjacent regions of memory**

Array is a collection of items stored at *Contiguous memory* locations.
- All elements must be of the **same data type**
- **Element size matters:** every element in the arrays takes up the same amountof space in memory.
Typical sizes: 
    - Integer: 4 bytes
    - Double: 8 bytes
    - Char: 1 byte

## Addresses
**Base Address:** Number of byte where the arrays start.
| If the base address is 100 and is a array of integers (integer size is 4 bytes), the next element is at 100 + 4

**Index:** Represents the offset from the beggining of the array.
*WHy base 0 indexing?* -> This simplifies the math for the CPU, and at index 0, we are **0 steps** from the start (base address)

### Memory Formula
**Address = Base Address + (Index * Data Size)**

## Complexity
### Random Acces: O(1)
Is constant time because not depend on the size of the array. We can access to any position directly, in the same amount of time.
The computer gets each one instantly, in does not cheek each element, it *jumps directly to that position*
### Instant Acces (by index): O(1)
### FInd a specific element: O(n)
The computer must review all the elements until foun the desired element
### Update Specific Element
**O(1)**
If computer have an instant access to the element that wants to be updated.
**O(n)**
If the computer must to search for the element that wants to be updated.
### Insert Element
**O(1)**
If is in the end of the array... *BUT* **O(n)** if the array gets full and need create a larger array and copy everything.
**O(n)**
In the another cases, because the elements after the insert element must be shifted.
## Delete Element
**O(1)**
If is in the end of the array
**O(n)**
In the another cases, because the elements after the deletd element must be shifted.

## Key takeways
- Contiguous memory blocks
- Fixed data type
- Simple Address Math

## Limitations
- Fixed size (in static arrays)
- Inserction/deletion to slow
- Wasted memory if not full