# Lists & Tuples Exercises

&nbsp;


<div width="95%">
<table style="border: none;">
  <tr style="border: none;">
    <th style="border: none;"><img align="left" height="100" src="../images/Waterworks List.png"></th>
    <td width="30%" align="right" style="border: none;"><em><h6>"A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements ... Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ].  
<br><br>
Lists are great to use when you want to work with many related values. They enable you to keep data together that belongs together, condense your code, & perform the same methods & operations on multiple values at once." <br><br>Lisa Tagliaferri, DigitalOcean, LLC  <a href="https://www.digitalocean.com/community/tutorials/understanding-lists-in-python-3">Understanding Lists </a></h6></em></td>
  </tr>
  <tr>
   <th style="border: none;"><img align="left" height="100" src="../images/Fireworks Tuple.png"></th>
    <td width="50%" align="right" style="border: none;"><em><h6>"A Tuple is a comma-separated sequence of values very similar to a list ... the main difference between tuples & lists is that lists are mutable & tuples are not ... if [a tuple] needs to be changed, a new object must be created.  
<br><br>
Lists typically contain items that are similar to each other, whereas tuples usually contain items that are diverse in type or character. However, there's no hard and fast rule to this. But if you want to be able to update the individual items, use a list. Otherwise, use a tuple." <br><br>Quackit.com,  <a href="https://www.quackit.com/python/tutorial/python_tuples.cfm">Python Tuples</a></em></h6></td>
  </tr>
</table>
</div>
<br>




#### General Review

1.   Create a Tuple  using `tuple()` & then using `()`  _what is the difference between the two methods?_
2.   Create a list using `list()` & then using `[]` _what is the difference between the two methods?_
3.   What kinds of data can you put in a list?  What kinds can you include in a Tuple?

&nbsp;


```python
sample_data     = ["apple", "pear", "banana", "cherry", "grape", "watermelon", "strawberry",
                   "mango" "pineapple", "blueberry", "blackberry", "raspberry", "peach", "plum"]

second_sample = ("dog", "cat", "parrot", "fish", "guinea pig" )
```

&nbsp;

#### Using the "sample_data" list above:

1.   Return "plum", starting from the left-hand end.  How do you do it from the right-hand end?
2.   Return "mango", starting from the left-hand end.  How about from the right-hand end?
3.   Replace "raspberry" with "huckleberry".
4.   Swap the positions of  "apple" & "cherry".
5.   How would you alphabetize the list?
6.   Delete "watermelon".
7.   Add ["zucchini", "carrot", "onion"] onto the end of the list.

&nbsp;

#### Using the "second_sample" Tuple above:

1. Return "parrot", starting from the right-hand side,  then from the left.
2. Return "guinea pig", starting from the right-hand side, then from the left.
3. Can you change "cat" into "elephant"?  Why or why not?
4. Make a new Tuple by re-ordering the content of the original Tuple.
5. Can you append the Tuple to the list?  Can you append the list to the Tuple?  Why/why not?
6. Add ("rat", "monkey") to the Tuple (_this is a bit of a trick question!_)

