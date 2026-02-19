#Q1.Write a list comprehension to generate squares of numbers from 1 to 10.
squares = [i**2 for i in range(1, 11)]
print(squares)
# 2. Create a list of even numbers between 1 and 50 using list
# comprehension.
evens = [i for i in range(1, 51) if i % 2 == 0]
print(evens)
# 3. Convert all strings in a list to uppercase using list comprehension.
words=["apple","banana","mango"]
upper_words=[w.upper() for w in words]
print(upper_words)
# 4. Given a list of integers, create a new list that contains only the positive
# numbers.
nums=[-2,-4,8,6,0,-8]
positive_num=[n for n in nums if n>0]
print(positive_num)

#5.Create a list of tuples (num, num^2) for numbers 1 to 5.
result=[(i,i*2) for i in range(1,6)]
print(result)

#6. Extract all vowels from a given string using list comprehension.
text="hello World"
vowels=[ch for ch in text if ch.lower()in "aeiou"]
print(vowels)
#7. Flatten a 2D list using list comprehension.
matrix=[[1,2],[2,3],[4,5],[5,6]]
flat=[item for row in matrix for item in row]
print(flat)

#8.Replace all negative numbers in a list with 0 using list comprehensio
nums=[-2,-4,8,6,0,-8]
replace_negative=[0 if n<0 else n for n in nums]
print(replace_negative)

#9. Given a list of words, create a list of lengths of each word.
words=["apple","banana","mango"]
lengths=[len(w) for w in words]
print(lengths)

#10.Filter out words that start with the letter 'A' or 'a'.
words=["apple","banana","mango","Avocado","ant"]
filtered=[w for w in words if w.lower().startswith('a')]
print(filtered)

#11. From a list of numbers, generate a list of “even” or “odd” strings using
# list comprehension.
# (Like → [“even”, “odd”, “odd”, “even”…])
no=[1,2,34,5,6,7]
results=["even" if n%2==0 else "odd" for n in nums]
print(result)

#12. Create a list of numbers divisible by both 3 and 5 in range 1–100.
divi=[i for i in range(1,101) if i%3 ==0 and i%5==0]
print(divi)

# 13. Write a nested list comprehension to generate a multiplication table
# for 1–5.
table=[[i*j for j in range(1,11)]for i in range(1,6)]
print(table)

# 14. Convert a dictionary’s keys into a list using list comprehension.
d={"a":1,"b":2,"c":3}
keys_list=[k for k in d]
print(keys_list)
# 15. Extract numeric digits from a string using list comprehension.
numerictex="a12cr9"
digits=[ch for ch in numerictex if ch.isdigit()]
print(digits)

# 16. Use list comprehension to remove all spaces from a string.
text1="hello world python"
no_space=[ch for ch in text if ch!= " "]
print("".join(no_space))

# 17. Create a list of characters that appear more than once in a string.
text1="hello world python"
duplicates=[ch for ch in set(text) if text.count(ch)]>1
print(duplicates)

# 18. From a list of sentences, generate a list of all words (split using list
# comprehension).
sentences=["I love python","List comprehension is cool"]
words=[word for s in sentences for word in s.split()]
print(words)
# 19. Create a list of unique elements from a list using list comprehension +
# condition.
numbers=[1,3,3,4,5,6,6,7]
unique=[x for i,x in enumerate(numbers)if x not numbers[:i]]
# 20. Generate all pairs (x, y) where x is from list A and y is from list B
# (cartesian product).
A=[1,2,3]
B=["a","b"]
pairs=[(x,y)for x in A for y in B]
print(pairs)


#lamda functions

#1. Write a lambda to add two numbers.
add=lambda a,b: a+b
print(add(3,5))

#2. Create a lambda to check if a number is even.
is_even==lambda n:n %2==0
print(is_even(4))

#3. Write a lambda to get the last character of a string.
last_char=lambda s:s[-1]
print(last_char("python"))

#4.Use lambda with map() to square every number in a list.
no=[1,2,3,4,5,6]
squares=list(map(lambda x:x**2,nums))
print(squares)

#5. Use lambda with filter() to get only odd numbers from a list.
odds=list(filter(lambda x:x%2!=0,no))
print(odds)

# 6. Use sorted() + lambda to sort a list of tuples by second value.
data = [(1, 5), (2, 3), (4, 1), (3, 7)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

# 7. Create a lambda to check if a string is a palindrome.
is_palindrome=lambda s : s==s[::-1]
print(is_palindrome("madam"))
# 8. Use lambda to find maximum of three numbers.
max3=lambda a,b,c :max(a,b,c)
print(max3(10,25,15))

# 9. Write a lambda to reverse a string.
reverse=lambda s :s[: :-1]
print(reverse("python"))

# 10. Use lambda with map() to convert a list of strings to integers.
num_str=["1","2","3","4"]
nums_int=list(map(lambda x :int(x),num_str))
print(nums_int)

# 11. Use lambda with filter() to remove empty strings from a list.
words=["apple","","banana","","mango"]
clean=list((filter(lambda x:x!="",words)))
print(clean)





