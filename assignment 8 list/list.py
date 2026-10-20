
# Q1.
numbers = [10, 20, 30, 40, 50, 60, 70]
first_element = numbers[0]
middle_element = numbers[len(numbers) // 2]
last_element = numbers[-1]

# Q2.
numbers2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
first_five = numbers2[:5]
last_four = numbers2[-4:]
every_second_reverse = numbers2[::-2]

# Q3. 
fruits = ["apple", "banana", "cherry", "mango"]
banana_index = fruits.index("banana")
fruits[banana_index] = "orange"
fruits.insert(2, "grapes")
fruits.remove("cherry")



# Q4.
numbers4 = [12, 45, 23, 67, 89, 34]
reversed_numbers = numbers4[::-1]

# Q5. 
numbers5 = [45, 12, 89, 34, 89, 67, 45, 23]
unique_numbers = list(set(numbers5))  
unique_numbers.sort()                 
second_largest = unique_numbers[-2]   

# Q6.
numbers6 = [10, 20, 30, 40, 50, 60]
k = 2
right_part = numbers6[-k:]            
left_part = numbers6[:-k]             
rotated_list = right_part + left_part 

# Q7. 
numbers7 = [10, 20, 10, 30, 20, 40, 30, 50]

unique_ordered = sorted(set(numbers7), key=numbers7.index)




# Q8. 
data8 = [[10, 20], [30, 40], [50, 60]]
flattened = data8[0] + data8[1] + data8[2]

# Q9. 
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
main_diagonal = [matrix[0][0], matrix[1][1], matrix[2][2]]
secondary_diagonal = [matrix[0][2], matrix[1][1], matrix[2][0]]
middle_column = [matrix[0][1], matrix[1][1], matrix[2][1]]

sum_main = sum(main_diagonal)
sum_secondary = sum(secondary_diagonal)
sum_middle = sum(middle_column)

# Q10. 
data10 = [15, 5, 25, 10, 35, 20, 30]
unique_sorted = list(set(data10))
unique_sorted.sort()

largest_three = unique_sorted[-3:]    
smallest_two = unique_sorted[:2]      
smallest_two.reverse()                

transformed_list = largest_three + smallest_two