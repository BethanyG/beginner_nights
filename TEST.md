<details>
 	<summary>Basic syntax</summary>
<br>

- [ ] [Argument unpacking][argument-unpacking]

- [ ] [Comments][comments-general]

  - [ ] TODO: Explain # syntax in Python

- [ ] [Expressions][expressions]

  - [ ] [Order of Evaluation][order-of-evaluation]

- [ ] Statements
  - [ ] TODO: Explain the importance of statements in Python
  - [ ] [`pass`][keyword-pass]
  </details>
  <details>
 	<summary>Builtin Types</summary>
<br>

_**TODO:** Casting between types in Python can be a bit unclear; this will need expansion_

- [ ] [Type conversion][type-conversion]

<details>
  <summary>Primitives</summary>
<br>

_These are types that represent discreet values in memory that do not contain other values; all have a dedicated literal syntax._

  <details>
    <summary>Bascis</summary>
    <br>
    
- [ ] [`None`][keyword-none]
- [ ] [`bool`][builtin-types-bool]
  - [ ] [`True`][keyword-true]
  - [ ] [`False`][keyword-false]
- [ ] [`int`][builtin-types-int]
- [ ] [`float`][builtin-types-float]
- [ ] [`str`][builtin-types-str]
  - [ ] [String methods][string-methods]
  - [ ] [String formatting][string-formatting]
  - [ ] [String splitting][string-splitting]
  - [ ] [String translation][string-translation]

</details>

<details>
<summary>Intermediate</summary>
<br>

_These are less commonly used primitives, but still important to know._

- [ ] [`complex`][builtin-types-complex]
- [ ] [`bytes`][builtin-types-bytes]

  </details>
  </details>

  <details>
     <summary>Containers</summary>
     <br>

_These are types that hold one or more of some other primitive type; they're the building blocks of more complex data structures._

  <details>
      <summary>Basic</summary>
      <br>
      
_Again, these are non-negotiable: every Python user must be comfortable with their use and abuse to be considered fluent, as they appear in **most** workaday code. These are also common enough that they each have their own dedicated literal syntax._

- [ ] [`tuple`][builtin-types-tuple]
- [ ] [`range`][builtin-types-range]
- [ ] [`list`][builtin-types-list]
  - [ ] [List Methods][list-methods]
- [ ] [`dict`][builtin-types-dict]
- [ ] [`set`][builtin-types-set]

  </details>

<details>
<summary>Intermediate</summary>
<br>

_Much more rarely used containers that you might want to know and recognize._

- [ ] [`bytearray`][builtin-types-bytearray]
- [ ] [`frozenset`][builtin-types-frozenset]

  </details>

  <details>
  <summary>Advanced</summary>
  <br>

_These will very rarely be encountered in the wild, the first because it's more of an internal implementation detail and the second because it's hyper-specific._

- [ ] [`slice`][builtin-types-slice]
- [ ] [`memoryview`][builtin-types-memoryview]


  </details>

  <details>
  <summary>OOP-Specific</summary>
  <br>
  
  - [ ] [`type`][builtin-types-type]
  - [ ] [`object`][builtin-types-object]
  - [ ] [`property`][builtin-types-property]

</details>
</details>
</deatils>
</details>

  
<details>
 	<summary>Language-unique concepts</summary>
<br>

-  [ ] [The Zen of Python][zen-of-python]
-  [ ] [Pythonic][pythonic]
-  [ ] [Python Enhancement Proposals][python-enhancement-proposals]
-  [ ] [PEP 8][pep-8-style-guide]
-  [ ] [Dunder Methods][dunder-methods]

</details>
<details>
 	<summary>General concepts</summary>
<br>

- [ ] [Arithmetic][arithmetic-general]

  - [ ] [Modular Division][modular-division]

- [ ] [Bitwise manipulation][bitwise-manipulation-general]

  - [ ] [Binary numbers][binary-numbers]
  - [ ] [Bitflags][bitflags]
  - [ ] [Bitwise operators][bitwise-operators]
  - [ ] [Powers of Two][powers-of-two]

- [ ] [Boolean logic][boolean-logic-general]

  - [ ] [Boolean values][boolean-values]

    - [ ] [Booleans are integers][booleans-are-integers]
    - [ ] [`True`][keyword-true]
    - [ ] [`False`][keyword-false]

  - [ ] [Boolean operators][boolean-operators]
    - [ ] [`not`][keyword-not]
    - [ ] [Short-circuiting][short-circuiting]
      - [ ] [`and`][keyword-and]
      - [ ] [`or`][keyword-or]

- [ ] [Bracket Notation][bracket-notation]

  - [ ] [Indexing][indexing]
  - [ ] [Slicing][slicing]

- [ ] [Comparisons][comparisons-general]

  - [ ] [Comparison operators][comparison-operators]
  - [ ] [Integer comparison][integer-comparison]
  - [ ] [Rich comparison methods][rich-comparison-methods]
  - [ ] [Equality operator][equality-operator]
  - [ ] [Equivalence][equivalence]
  - [ ] [Inequality][inequality]

- [ ] [Conditionals][conditionals-general]

  - [ ] [Conditionals structures][conditional-structures]
    - [ ] [`if`][keyword-if]
    - [ ] [`elif`][keyword-elif]
    - [ ] [`else`][keyword-else]

- [ ] [Enumeration][enumeration]

  - [ ] [Enumerated values][enumerated-values]

- [ ] [Functions][functions-general]

  - [ ] [Function Definition][function_definition]
    - [ ] [`def`][keyword-def]
    - [ ] [`lambda`][keyword-lambda]
    - [ ] [Function signature][function-signature]
      - [ ] [Arguments & parameters][arguments-and-parameters]
      - [ ] [Positional parameters][positional-parameters]
      - [ ] [Positional-only parameters][positional-only-parameters]
      - [ ] [Keyword parameters][keyword-parameters]
      - [ ] [Keyword-only parameters][keyword-only-parameters]
      - [ ] [Default arguments][default-arguments]
      - [ ] [`\*args``][star-args]
      - [ ] [`\*\*kwargs``][star-star-kwargs]
  - [ ] [Return Values][return-value]
    - [ ] [`return`][keyword-return]
  - [ ] [Generators][generators]
    - [ ] [`yield`][keyword-yield]
  - [ ] [Type hinting][type-hinting]
  - [ ] [Call semantics][call-semantics]

- [ ] [Identity testing][identity-testing]

  - [ ] [`is`][keyword-is]

- [ ] [Loops][loops-general]

  - [ ] [`while` loops][while-loops]
    - [ ] [`while`][keyword-while]
  - [ ] [`for` loops][for-loops]
    - [ ] [`for`][keyword-for]
  - [ ] [Exiting loops][exiting-loops]
    - [ ] [`break`][keyword-break]
    - [ ] [`continue`][keyword-continue]
  - [ ] [Iteration][iteration]

    - [ ] [Iterables][iterables]
    - [ ] [Iterators][iterators]

  - [ ] [Membership testing][membership-testing]
    - [ ] [`in`][keyword-in]

- [ ] [Operators][operators]

  - [ ] [Operator overloading][operator-overloading]
  - [ ] [Operator precedence][operator-precedence]

- [ ] [Scope][scope]

  - [ ] [Namespaces][namespaces]
    - [ ] [`global`][keyword-global]
    - [ ] [`nonlocal`][keyword-nonlocal]
  - [ ] [`del`][keyword-del]

- [ ] [Variables][variables]
  - [ ] [Assignment][assignment]
    - [ ] [Multiple assignment][multiple-assignment]
    - [ ] [Tuple unpacking][tuple-unpacking]
    - [ ] [Constants][constants]
</details>

<details>
 	<summary>Intermediate Concepts</summary>
<br>

- [ ] [Comprehension Syntax][comprehension-syntax]

  - [ ] [List comprehension][list-comprehension]
  - [ ] [Dict comprehension][dict-comprehension]
  - [ ] [Set comprehension][set-comprehension]
  - [ ] [Generator comprehension][generator-comprehension]

- [ ] Context managers

  - [ ] [`with`][keyword-with]

- [ ] [Decorators][decorators]

- [ ] [Docstrings][docstrings]

- [ ] [Exceptions][exceptions-general]

  - [ ] [Exception handling][exception-handling]
  - [ ] [Exception catching][exception-catching]
    - [ ] [`try`][keyword-try]
    - [ ] [`except`][keyword-except]
    - [ ] [`else`][keyword-else]
    - [ ] [`finally`][keyword-finally]
  - [ ] [Exception hierarchy][exception-hierarchy]
  - [ ] [Raise][raise]
    - [ ] [Exception message][exception-message]
    - [ ] [`raise`][keyword-raise]
    - [ ] [`assert`][keyword-assert]

- [ ] [Importing][importing]

  - [ ] [`import`][keyword-import]
  - [ ] [`from`][keyword-from]
  - [ ] [`as`][keyword-as]

- [ ] [Standard Library][standard-library]
  - [ ] [Data structures][data-structures]
    - [ ] [Lookup efficiency][lookup-efficiency]
    - [ ] [Recursive data structures][recursive-data-structures]
  - [ ] [Regular Expressions][regular-expressions]
</details>

<details>
 	<summary>Object-oriented concepts</summary>
<br>

- [ ] [Objects][objects-general]

  - [ ] [Everything is an object][everything-is-an-object]

- [ ] [Classes][classes-general]

  - [ ] [Custom classes][custom-classes]
    - [ ] [`class`][keyword-class]
  - [ ] [Class members][class-members]
    - [ ] Behavior
      - [ ] [Methods][methods-general]
        - [ ] [Instance Methods][instance-methods]
          - [ ] [Implicit self][implicit-self]
          - [ ] [Initialization][initialization]
          - [ ] [Instantiation][instantiation]
        - [ ] [Class methods][class-methods]
          - [ ] [Constructor][constructor]
        - [ ] [Static Methods][static-methods]
    - [ ] [State][state]
      - [ ] [Instance Attributes][instance-attributes]
      - [ ] [Instance Properties][instance-properties]
        - [ ] [Property Decorator][property-decorator]

- [ ] [Inheritance][inheritance-general]

  - [ ] [Class inheritance][class-inheritance]

- [ ] [Composition][composition-general]

  - [ ] [Class composition][class-composition]

- [ ] [Encapsulation][encapsulation-general]

  - [ ] [Non-Public Methods][non-public-methods]

- [ ] [Interfaces][interfaces-general]

  - [ ] [Duck Typing][duck-typing]

- [ ] [Mutation][mutation-general]

  - [ ] [Immutability in Python][immutability]
  - [ ] [Mutability in Python][mutability]

- [ ] [Polymorphism][polymorphism-general]
  - [ ] [Dynamic typing][dynamic-typing]
 </details>

<details>
 	<summary>Functional concepts</summary>
<br>

- [ ] [Anonymous functions][anonymous-functions-general]

  - [ ] [`lambda`][keyword-lambda]

- [ ] [Higher-order functions][higher-order-functions]

  - [ ] [Decorators as higher-order functions][decorators-as-higher-order-functions]
  - [ ] [`map`][builtin-functions-map]
  - [ ] [`filter`][builtin-functions-filter]

- [ ] [Immutability][immutability]

- [ ] [Nested functions][nested-functions]

- [ ] [Partial application][partial-application]

  - [ ] TODO: `functools.partial`

- [ ] [Recursion][recursion]

  - [ ] **TODO:** explain limitations of recursion in Python, ie `RecursionLimit`

- [ ] [REPL][repl]
  - [ ] TODO: Discuss the interactive Python interpreter
</details>
  
<details>
<summary>Advanced concepts (probably outside scope of Exercism)</summary>
<br>

- [ ] Asynchronous operatons
  - [ ] [`async`][keyword-async]
  - [ ] [`await`][keyword-await]
</details>
