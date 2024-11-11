# Largest of Three Numbers   

## Problem Statement  
Given an array of integers, find the largest product of any three numbers.  

## Approach  
1. Sort the array to identify the largest and smallest numbers efficiently.  
2. Compute the product of the three largest numbers and the product of the two smallest numbers (potential negatives) with the largest number.  
3. Return a maximum of the two computed products.   

## Complexity  
- **Time Complexity**: \(O(n \log n)\) (due to sorting).  
- **Space Complexity**: \(O(1)\).  

## Usage  
```python
from solution import largest_product_of_three

nums = [10, -10, 1, 3, 2] 
print(largest_of_three(nums))  # Output: 60 
