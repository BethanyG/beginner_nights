# Working with Loops & Lists

&nbsp;


<div width="95%">
<table style="border: none;">
  <tr style="border: none;">
    <th style="border: none;"><img align="left" src="../images/For loop.png"><br></th>
    <td width="50%" align="right" style="border: none;"><img align="left" src="../images/While Loop.png"><br></td>
  </tr>
  <tr>
   <th style="border: none;"><br><img align="left" src="../images/pre comprehension loop.png"></th>
    <td width="50%" align="right" style="border: none;"><img align="left" src="../images/comprehensions.png"></td>
  </tr>
</table>
</div>
<br>




### General Review

#### Lists

*  Made either by calling the _constructor_ [**`list()`**](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists), or by using the _literal form_ **`[ ]`**
*  Are _**sequence types**_, & support all the [**common sequence operations**](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
*  Are _**ordered**_ via _index_, starting from **0**, on the left-hand side.
*  Are _**mutable**_ (_can be updated, overwritten, & appended to_)
*  Can be _**sliced**_, using **`[start:stop:step]`** notation.  A slice returns a _**copy**_ of the list.
*  Can contain just about anything .... including sub-lists & other data structures.


#### For Loops

*  Used for _**Definite Iteration**_ (**i.e.** _when the number of iterations is fixed_).
*  Always includes a _**`range()`**_ or other  [**sequence type**](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range).  May or may not include a "test".
*  Both _**index**_ and _**data**_ can be accessed through the use of [**`enumerate()`**](https://docs.python.org/3/library/functions.html#enumerate)
*  Can be converted into a _**comprehension**_, if it includes the creation or update of a List or Dictionary.



#### While Loops

* Used for _**indefinite iteration**_ (**i.e.**, _when you don't know ahead of time how many cycles it will take_)
*  Always include a "test" for loop continuation.
*  May or may not employ _**continue**_ or _**break**_ (_for skipping ahead or stopping short._)
*  Can be converted to a "_**"do-while"**_ by including a condition check _**after**_ the code block.

&nbsp;


### Exercises