# Loops to Comprehensions & Conditionals to Ternaries

&nbsp;


<div width="95%">
<table style="border: none;">
  <tr style="border: none;">
    <th style="border: none;"><img align="left" src="../images/pre comprehension loop.png"><br></th>
    <td width="50%" align="right" style="border: none;"><img align="left" src="../images/comprehensions.png"><br></td>
  </tr>
  <tr>
   <th style="border: none;"><br><img align="left" src="../images/If Else.png"></th>
    <td width="50%" align="right" style="border: none;"><img align="left" src="../images/ternary expressions.png"></td>
  </tr>
</table>
</div>
<br>



&nbsp;
&nbsp;
&nbsp;

#### Comprehension Code Example

```python

#This Loop
my_results = []

for number in range(51):
	if item % 2 != 0:
		my_results.append(number**3)


#Becomes this comprehension
odd_cubes = [number**3 for number in range(51) if number%2 != 0]

```

&nbsp;
&nbsp;


####  Ternary Code Example

```python

numbers = [1,2,3,4,5,6,7,8,9]

for index, item in enumerate(numbers_group):
     #This conditional
    if item % 2 == 0:
        numbers[index] = item**2
    else:
        numbers[index] = item**3

#-------------------------------------------------

	#Becomes this ternary expression
	for index, number in numbers:
		numbers[index] = item**2 if item % 2 == 0 else item**3

```

### General Review

*  [**Comprehensions**](https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/)  _flatten_ the loops used to create different data structures such as Lists, Dictionaries, or Sets.
	*  Execute slightly faster than their loop equivalents, because they  execute directly in C instead of the Python interpreter.
	*  Can include conditional tests
	*  Can be _nested_ (thereby flattening a nested loop)
	*  Can be used to create Lists, Sets, Dictionaries & more.
*  [**Ternary Operators**](https://syntaxdb.com/ref/python/ternary) _flatten_ the **`if`** .... **`else`** conditional statements (_but not if they're complex or include an **`elif`**_)


&nbsp;


**Data**

```python

words = ['Alligator', 'Aardvark', 'Pig', 'Bear', 'Moose', 'Python', 'Mouse', 'Owl', 'Giraffe']
numbers=[1,2,3,4,5,6,7,8,9]

```

&nbsp;
&nbsp;
&nbsp;

### Exercises:  Re-Write Each Loop or Conditional as a Comprehension or Ternary

**Comprehensions** -- _If the loop prints something, include it in a list instead._

1.  

```python

for word in words:
	if 'a' in word:
		print(word)
	
```

&nbsp;

2.

```python

output = []

for word in words:
	output.append((word, len(word)))

```

&nbsp;

3.

```python

squared = []

for number in numbers:
	squared.append(number**2)

```

&nbsp;

4.

```python

results = []

for index, item in enumerate(words):
	results.append((item + ' ')*index)

```

&nbsp;

5. 

```python
#for this, you can omit printing or appending.  Just replace the even indexes with '_'
for index, item in enumerate(words):
	if index%2 == 0:
		print(item)
		words[index] = '_'


```


&nbsp;

----

**Ternary Operators** -- _if the conditional is in a loop, only replace the conditional part_


**Data**

```python

snacks = ['Pie', 'Apple', 'Potato Chip', 'Carrot', 'Chocolate', 'Plum', 'Jawbreaker', 'Green Bean', 'Cake']
numbers = [5, 10, 15, 20, 25, 55, 67, 88, 90, 101, 33, 45, 72]

```

&nbsp;


1.

```python

for index, food in enumerate(snacks):
	if index % 2 == 0:
		print('Healthy')
	else:
		print('Not so healthy')

```

&nbsp;

2.

```python

for number in numbers:
	if number % 5 == 0:
		print('BUZZ!')
	else:
		print('FIZZLE')

```

&nbsp;

3.

```python

for snack in snacks:
	if len(snack) <= 5:
		print(snack)
	else:
		print(len(snack))

```

&nbsp;


4.

```python

for index, item in enumerate(snacks):
	if index % 2 == 0:
		print(f'{item}s are a pretty healthy snack!')
	else:
		print(f"While {item}s are yummy, we shouldn't eat too many of them")

```

