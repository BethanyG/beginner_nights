# Dictionaries & Dictionary Comprehensions

&nbsp;


<div width="95%">
<table style="border: none;">
  <tr style="border: none;">
    <th style="border: none;"><img align="left" src="../images/pre dict comp loop.png"><br></th>
    <td width="50%" align="right" style="border: none;"><img align="left" src="../images/dict comprehensions.png"><br></td>
  </tr>
</table>
</div>
<br>



&nbsp;
&nbsp;
&nbsp;

#### An Example Dictionary

```python

'''Verses of the 12 days of Christmas Key == day number & Value== verse strings.'''

    verses = {12: ('twelfth', 'twelve Drummers Drumming, '),
              11: ('eleventh', 'eleven Pipers Piping, '),
              10: ('tenth', 'ten Lords-a-Leaping, '),
               9: ('ninth', 'nine Ladies Dancing, '),
               8: ('eighth', 'eight Maids-a-Milking, '),
               7: ('seventh', 'seven Swans-a-Swimming, '),
               6: ('sixth', 'six Geese-a-Laying, '),
               5: ('fifth', 'five Gold Rings, '),
               4: ('fourth', 'four Calling Birds, '),
               3: ('third', 'three French Hens, '),
               2: ('second', 'two Turtle Doves, and '),
               1: ('first', 'a Partridge in a Pear Tree.')}
               
    #to get at the tuple for the first verse, use the key         
    first_day_verse = verses[1]
    
    #to get at just the verse (index 1 of the tuple in the value position), use an index
    first_verse_only = verses[1][1]

```

&nbsp;
&nbsp;


####  A Loop that Makes/Updates a Dictionary 

```python

#this is the list of numbers we're using as keys for the dictionary
inputs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, 100, 89, 53, 66, 71, 25, 29]

#this is the empty dictionary, ready for input/updates
output_data = {}

#This updating loop
for key in inputs:
	if key < 25:
	    if key % 2 == 0:
	        output_data[key]='even'
	    else:
	        output_data[key]='odd'
	else:
		continue
#-------------------------------------------------

	#Becomes this dictionary comprehension.  Note the ternary in the value output
	output_data = {key:'even' if key%2 == 0 else 'odd' for key in inputs if key < 25}

```

&nbsp;
&nbsp;

---


### General Review
&nbsp;

*   [**`Dictionaries`**](https://realpython.com/python-dicts/)  are a data structure in Python.  They're are declared with **`{ }`**  (_**`{key : value, key_2 : value_2}`**_)

*  There's also [**`dict()`**](https://docs.python.org/3/library/stdtypes.html#dict) constructor.
*  While **`list()`** content is accessed by _**index**_, **`dict`** content is accessed by _**key**_
	* **`keys`** must be _**unique**_, & must be [**_hashable_**](https://stackoverflow.com/questions/14535730/what-do-you-mean-by-hashable-in-python).  
	*  **`values`** can be almost _anything_, including numbers, strings, nested dictionaries, tuples, lists, or even classes or functions.
* The content for each _**key**_ can be accessed by using _**index notation**_ with dictionary name & key **`dict[key]`**  will return the  **`value(s) stored`** for that key in the dictionary.
* **`dict()`**s are _iterable_.  The default iteration goes through the  **`key`s**, but you can iterate on **`values`** with a little work as well (_`enumerate()` and `dict.items()` can be your best friends here_).
* All methods that work on dictionaries are  [**here**](https://docs.python.org/3/library/stdtypes.html#typesmapping)
* Additional (very useful!) flavors of dictionaries can be found in the [**collections module**](https://docs.python.org/3/library/collections.html), which also has many useful variants & extensions of **`set()`** & **`list()`**
*   Dictionaries can be written as comprehensions

*  [**Comprehensions**](https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/)  _flatten_ the loops used to create different data structures such as Lists, Dictionaries, or Sets.
	*  Execute slightly faster than their loop equivalents, because they  execute directly in C instead of the Python interpreter.
	*  Can include conditional tests
	*  Can be _nested_ (thereby flattening a nested loop)
	*  Can be used to create Lists, Sets, Dictionaries & more.


&nbsp;


**Data**

```python

words = ['Alligator', 'Aardvark', 'Pig', 'Bear', 'Moose', 'Python', 'Mouse', 'Owl', 'Giraffe']
numbers=[1,2,3,4,5,6,7,8,9]

```

&nbsp;
&nbsp;
&nbsp;

### Exercises:  

1. Make a dictionary that combines the lists above.  Use the numbers as keys.
2. Make a dictionary that has the words as keys, and interesting facts about each as values (a random string will do here)
3. Make a dictionary that has the numbers as keys...and then lists the words as many times as the number for values
4. Update the dictionary from #1 with new animal words
5. Add new entires to dictionary #2
6. Re-write any of the above as a dictionary comprehension.