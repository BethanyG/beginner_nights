# Python reference

Python is an interpreted, dynamically (but strongly) typed, and garbage-collected general programming language that has become extremely popular due to its readability, low barrier for entry, and exceptionally deep ecosystem of libraries and tools. Python is object-based, but is inherently multi-paradigm and has drawn together influences from a wide range of programming languages, including ABC, Haskell, Lisp, and Modula-3. It is ideal for prototyping and ad-hoc tasks, but also sees wide use in scientific computing, web development, and automation.


## Concepts

Below are the concepts that were extracted/identified in Python based on Exercism's V2 exercises and topics in the [Python 3 Documentation](https://docs.python.org/3/) -- specifically the [Python Tutorial](https://docs.python.org/3/tutorial/index.html) and the [Python Library Reference](https://docs.python.org/3/library/index.html)

## Unique to Python

- [ ] [The Zen of Python][zen-of-python]
- [ ] [Pythonic][pythonic]
- [ ] [Python Enhancement Proposals][python-enhancement-proposals]
- [ ] [PEP 8][pep-8-style-guide]
- [ ] [Dunder Methods][dunder-methods]


## Baseline concepts introduced in the "basics" exercise


<details>
    <summary> Entrypoint
      <br>
    </summary>

- [ ] [Arithmetic][arithmetic-general]
- [ ] [Assignment][assignment]
- [ ] [Comments][comments-general]
  - [ ] TODO: Explain # syntax in Python

- [ ] [Constants][constants]
- [ ] [Docstrings][docstrings]
- [ ] [Expressions][expressions]
- [ ] [Functions][functions-general]
  - [ ] [Function Definition][function_definition]
    - [ ] [`def`][keyword-def]
    - [ ] [`pass`][keyword-pass]
    - [ ] [`None`][keyword-none]
    - [ ] [Return Values][return-value]
        - [ ] [`return`][keyword-return]

- [ ] Statements
  - [ ] TODO: Explain the importance of statements in Python

  - [ ] [Variables][variables]

</details>


## General concepts


<details>
    <summary> Core
      <br>
    </summary>

- [ ] [Argument unpacking][argument-unpacking]
- [ ] [Arithmetic][arithmetic-general]
  - [ ] [Modular Division][modular-division]
  - [ ] [Arithmetic Operators][arithmetic-operators]

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

- [ ] [`dict`][builtin-types-dict]

- [ ] [Enumeration][enumeration]
  - [ ] [Enumerated values][enumerated-values]
  - [ ] [`enumerate()`][builtin-functions-enumerate]

- [ ] [Functions][functions-general]
  - [ ] [Function Definition][function_definition]
    - [ ] [`def`][keyword-def]
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
        - [ ] [`none`][keyword-none]

  - [ ] [Anonymous functions][anonymous-functions-general]
    - [ ] [`lambda`][keyword-lambda]

  - [ ] [Nested functions][nested-functions]

  - [ ] [Type hinting][type-hinting]
  - [ ] [Call semantics][call-semantics]

- [ ] [Identity testing][identity-testing]
  - [ ] [`is`][keyword-is]

- [ ] [Iteration][iteration]
  - [ ] [Iterables][iterables]
  - [ ] [Iterators][iterators]

  - [ ] [Loops][loops-general]
      - [ ] [`while` loops][while-loops]
        - [ ] [`while`][keyword-while]

      - [ ] [`for` loops][for-loops]
        - [ ] [`for`][keyword-for]
        - [ ] [`range`][builtin-types-range]

      - [ ] [Exiting loops][exiting-loops]
        - [ ] [`break`][keyword-break]
        - [ ] [`continue`][keyword-continue]

- [ ] [Membership testing][membership-testing]
  - [ ] [`in`][keyword-in]

- [ ] [Numbers]
  - [ ] [`int`][builtin-types-int]
  - [ ] [`float`][builtin-types-float]
  - [ ] [`complex`][builtin-types-complex]
    - [ ] [cmath][library-cmath]

  - [ ] [`fractions`][library-fractionsraction]
  - [ ] [`decimal`][library-decimal]
  - [ ] [math][library-math]

- [ ] [Operators][operators]
  - [ ] [Operator overloading][operator-overloading]
  - [ ] [Operator precedence][operator-precedence]

- [ ] [REPL][repl]
  - [ ] TODO: Discuss the interactive Python interpreter

- [ ] [sequences][builtin-types-sequence]
  - [ ] [common sequence operations][common-sequence-operations]
    - [ ] [bracket notation][bracket-notation]
      - [ ] [Indexing][indexing]
      - [ ] [Slicing][slicing]
      - [ ] Slice assignment

  - [ ] [`list`][builtin-types-list]
    - [ ] [List Methods][list-methods]

  - [ ] [`range`][builtin-types-range]
  - [ ] [`str`][builtin-types-str]
    - [ ] [str-methods][string-methods]
    - [ ] [String formatting][string-formatting]
    - [ ] [str-splitting][string-splitting]
    - [ ] [str-translation][string-translation]

  - [ ] [`tuple`][builtin-types-tuple]

- [ ] [Scope][scope]
  - [ ] [`del`][keyword-del]

  - [ ] [Namespaces][namespaces]
    - [ ] [`global`][keyword-global]
    - [ ] [`nonlocal`][keyword-nonlocal]

- [ ] [`set`][builtin-types-set]
  - [ ] [`frozenset`][builtin-types-frozenset]

- [ ] [Type conversion][type-conversion]
  TODO: Casting between types in Python can be a bit unclear; this will need expansion
  - [ ] [Type conversion][type-conversion]

- [ ] [Variables][variables]
  - [ ] [Assignment][assignment]
    - [ ] [Multiple assignment][multiple-assignment]
    - [ ] [Tuple unpacking][tuple-unpacking]
    - [ ] [Constants][constants]

</details>


## Intermediate Concepts

<details>
    <summary> Intermediate
      <br>
    </summary>

- [ ] Aliasing
  - [ ] [`as`][keyword-as]
  - [ ] [`import`][keyword-import]

- [ ] [`bytes`][builtin-types-bytes]
  - [ ] [`bytearray`][builtin-types-bytearray]

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
    - [ ] [`from`][keyword-from]
    - [ ] [raise from][exception-chaining]
    - [ ] [`assert`][keyword-assert]

- [ ] [Generators][generators]
  - [ ] [`yield`][keyword-yield]

- [ ] [Higher-order functions][higher-order-functions]
  - [ ] [Decorators as higher-order functions][decorators-as-higher-order-functions]
  - [ ] [`map`][builtin-functions-map]
  - [ ] [`filter`][builtin-functions-filter]

- [ ] [Partial application][partial-application]
  - [ ] TODO: `functools.partial`

- [ ] [Importing][importing]
  - [ ] [relative imports][relative-imports]
  - [ ] [`import`][keyword-import]
  - [ ] [`from`][keyword-from]
  - [ ] [`as`][keyword-as]

- [ ] [Recursion][recursion]
  - [ ] TODO: explain limitations of recursion in Python, ie `RecursionLimit`

- [ ] [Regular Expressions][regular-expressions]


</details>


### Specific Object-Oriented Concepts


<details>
    <summary> OOP-Specific
      <br>
    </summary>



- [ ] [Objects][objects-general]
  - [ ] [Everything is an object][everything-is-an-object]
    - [ ] [`type`][builtin-types-type]
    - [ ] [`object`][builtin-types-object]
    - [ ] [`property`][builtin-types-property]

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
  - [ ] [Meta Classes][metaclasses]
      - [ ] [Virtual Base Classes]
      - [ ] [Abstract Base Classes]
      - [ ] [`.__subclasshook__() `]
      - [ ] [`.register()`]
  - [ ] [Duck Typing][duck-typing]

- [ ] [Mutation][mutation-general]
  - [ ] [Immutability in Python][immutability]
  - [ ] [Mutability in Python][mutability]

- [ ] [Polymorphism][polymorphism-general]
  - [ ] [Dynamic typing][dynamic-typing]
  - [ ] [Duck Typing][duck-typing]
  - [ ] [Gradual Typing][gradual-typing]
    - [ ] [Type Hinting][type-hinting]
    - [ ] [`typing`][typing-module]


</details>


## Advanced concepts (probably outside scope of Exercism)

<details>
    <summary> Advanced/Specialized
      <br>
    </summary>

- [ ] Asynchronous operatons
  - [ ] [`async`][keyword-async]
  - [ ] [`await`][keyword-await]

_These will very rarely be encountered in the wild, the first because it's more of an internal implementation detail and the second because it's hyper-specific_:
- [ ] [`slice`][builtin-types-slice]
- [ ] [`memoryview`][builtin-types-memoryview]


</details>



[anonymous-functions-general]: ../../../reference/concepts/anonymous_functions.md
[argument-unpacking]: ./concepts/argument_unpacking.md
[arguments-and-parameters]: ./concepts/arguments_and_parameters.md
[arithmetic-general]: ../../../reference/concepts/arithmetic.md
[arithmetic-operators]: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
[assignment]: ./concepts/assignment.md
[binary-numbers]: ./concepts/binary_numbers.md
[bitflags]: ./concepts/bitflags.md
[bitwise-manipulation-general]: ../../../reference/concepts/bitwise_manipulation.md
[bitwise-operators]: ./concepts/bitwise_operators.md
[boolean-logic-general]: ../../../reference/concepts/boolean_logic.md
[boolean-operators]: ./concepts/boolean_operators.md
[boolean-values]: ./concepts/boolean_values.md
[booleans-are-integers]: ./concepts/booleans_are_integers.md
[bracket-notation]: ./concepts/bracket_notation.md
[builtin-functions-__import__]: ./concepts/builtin_functions/__import__.md
[builtin-functions-abs]: ./concepts/builtin_functions/abs.md
[builtin-functions-all]: ./concepts/builtin_functions/all.md
[builtin-functions-any]: ./concepts/builtin_functions/any.md
[builtin-functions-ascii]: ./concepts/builtin_functions/ascii.md
[builtin-functions-bin]: ./concepts/builtin_functions/bin.md
[builtin-functions-breakpoint]: ./concepts/builtin_functions/breakpoint.md
[builtin-functions-callable]: ./concepts/builtin_functions/callable.md
[builtin-functions-chr]: ./concepts/builtin_functions/chr.md
[builtin-functions-classmethod]: ./concepts/builtin_functions/classmethod.md
[builtin-functions-compile]: ./concepts/builtin_functions/compile.md
[builtin-functions-delattr]: ./concepts/builtin_functions/delattr.md
[builtin-functions-dir]: ./concepts/builtin_functions/dir.md
[builtin-functions-divmod]: ./concepts/builtin_functions/divmod.md
[builtin-functions-enumerate]: ./concepts/builtin_functions/enumerate.md
[builtin-functions-eval]: ./concepts/builtin_functions/eval.md
[builtin-functions-exec]: ./concepts/builtin_functions/exec.md
[builtin-functions-filter]: ./concepts/builtin_functions/filter.md
[builtin-functions-format]: ./concepts/builtin_functions/format.md
[builtin-functions-getattr]: ./concepts/builtin_functions/getattr.md
[builtin-functions-globals]: ./concepts/builtin_functions/globals.md
[builtin-functions-hasattr]: ./concepts/builtin_functions/hasattr.md
[builtin-functions-hash]: ./concepts/builtin_functions/hash.md
[builtin-functions-help]: ./concepts/builtin_functions/help.md
[builtin-functions-hex]: ./concepts/builtin_functions/hex.md
[builtin-functions-id]: ./concepts/builtin_functions/id.md
[builtin-functions-input]: ./concepts/builtin_functions/input.md
[builtin-functions-isinstance]: ./concepts/builtin_functions/isinstance.md
[builtin-functions-issubclass]: ./concepts/builtin_functions/issubclass.md
[builtin-functions-iter]: ./concepts/builtin_functions/iter.md
[builtin-functions-len]: ./concepts/builtin_functions/len.md
[builtin-functions-locals]: ./concepts/builtin_functions/locals.md
[builtin-functions-map]: ./concepts/builtin_functions/map.md
[builtin-functions-max]: ./concepts/builtin_functions/max.md
[builtin-functions-min]: ./concepts/builtin_functions/min.md
[builtin-functions-next]: ./concepts/builtin_functions/next.md
[builtin-functions-oct]: ./concepts/builtin_functions/oct.md
[builtin-functions-open]: ./concepts/builtin_functions/open.md
[builtin-functions-ord]: ./concepts/builtin_functions/ord.md
[builtin-functions-pow]: ./concepts/builtin_functions/pow.md
[builtin-functions-print]: ./concepts/builtin_functions/print.md
[builtin-functions-repr]: ./concepts/builtin_functions/repr.md
[builtin-functions-reversed]: ./concepts/builtin_functions/reversed.md
[builtin-functions-round]: ./concepts/builtin_functions/round.md
[builtin-functions-setattr]: ./concepts/builtin_functions/setattr.md
[builtin-functions-sorted]: ./concepts/builtin_functions/sorted.md
[builtin-functions-staticmethod]: ./concepts/builtin_functions/staticmethod.md
[builtin-functions-sum]: ./concepts/builtin_functions/sum.md
[builtin-functions-super]: ./concepts/builtin_functions/super.md
[builtin-functions-vars]: ./concepts/builtin_functions/vars.md
[builtin-functions-zip]: ./concepts/builtin_functions/zip.md
[builtin-functions]: ./concepts/builtin_functions/README.md
[builtin-types-bool]: ./concepts/builtin_types/bool.md
[builtin-types-bytearray]: ./concepts/builtin_types/bytearray.md
[builtin-types-bytes]: ./concepts/builtin_types/bytes.md
[builtin-types-complex]: ./concepts/builtin_types/complex.md
[builtin-types-dict]: ./concepts/builtin_types/dict.md
[builtin-types-float]: ./concepts/builtin_types/float.md
[builtin-types-frozenset]: ./concepts/builtin_types/frozenset.md
[builtin-types-int]: ./concepts/builtin_types/int.md
[builtin-types-list]: ./concepts/builtin_types/list.md
[builtin-types-memoryview]: ./concepts/builtin_types/memoryview.md
[builtin-types-object]: ./concepts/builtin_types/object.md
[builtin-types-property]: ./concepts/builtin_types/property.md
[builtin-types-range]: ./concepts/builtin_types/range.md
[builtin-types-sequence]: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
[builtin-types-set]: ./concepts/builtin_types/set.md
[builtin-types-slice]: ./concepts/builtin_types/slice.md
[builtin-types-str]: ./concepts/builtin_types/str.md
[builtin-types-tuple]: ./concepts/builtin_types/tuple.md
[builtin-types-type]: ./concepts/builtin_types/type.md
[builtin-types]: ./concepts/builtin_types/README.md
[call-semantics]: ./concepts/call_semantics.md
[class-composition]: ./concepts/class_composition.md
[class-inheritance]: ./concepts/class_inheritance.md
[class-members]: ./concepts/class_members.md
[class-methods]: ./concepts/class_methods.md
[classes-general]: ../../../reference/concepts/classes.md
[comments-general]: ../../../reference/concepts/comments.md
[common-sequence-operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[comparison-operators]: ./concepts/comparison_operators.md
[comparisons-general]: ../../../reference/concepts/comparisons.md
[composition-general]: ../../../reference/concepts/composition.md
[comprehension-syntax]: ./concepts/comprehension_syntax.md
[conditional-structures]: ./concepts/conditional_structures.md
[conditionals-general]: ../../../reference/concepts/conditionals.md
[constants]: ./concepts/constants.md
[constructor]: ./concepts/constructor.md
[custom-classes]: ./concepts/custom_classes.md
[data-structures]: ./concepts/data_structures.md
[decorators-as-higher-order-functions]: ./concepts/decorators_as_higher_order_functions.md
[decorators]: ./concepts/decorators.md
[default-arguments]: ./concepts/default_arguments.md
[dict-comprehension]: ./concepts/dict_comprehension.md
[docstrings]: ./concepts/docstrings.md
[duck-typing]: ./concepts/duck_typing.md
[dunder-methods]: ./concepts/dunder_methods.md
[dynamic-typing]: ./concepts/dynamic_typing.md
[encapsulation-general]: ../../../reference/concepts/encapsulation.md
[enumerated-values]: ./concepts/enumerated_values.md
[enumeration]: ../../../reference/concepts/enumeration.md
[equality-operator]: ./concepts/equality_operator.md
[equivalence]: ./concepts/equivalence.md
[everything-is-an-object]: ./concepts/everything_is_an_object.md
[exception-catching]: ./concepts/exception_catching.md
[exception-chaining]: https://docs.python.org/3/tutorial/errors.html#exception-chaining
[exception-handling]: ./concepts/exception_handling.md
[exception-hierarchy]: ./concepts/exception_hierarchy.md
[exception-message]: ./concepts/exception_message.md
[exceptions-general]: ./concepts/exceptions.md
[exiting-loops]: ./concepts/exiting_loops.md
[expressions]: ./concepts/expressions.md
[for-loops]: ./concepts/for_loops.md
[function-definition]: ./concepts/function_definition.md
[function-signature]: ./concepts/function_signature.md
[functions-general]: ../../../reference/concepts/functions.md
[generator-comprehension]: ./concepts/generator_comprehension.md
[generators]: ./concepts/generators.md
[higher-order-functions]: ../../../reference/concepts/higher_order_functions.md
[identity-testing]: ./concepts/identity_testing.md
[immutability]: ../../../reference/concepts/immutability.md
[implicit-self]: ./concepts/implicit_self.md
[importing]: ./concepts/importing.md
[indexing]: ./concepts/indexing.md
[inequality]: ./concepts/inequality.md
[inheritance-general]: ../../../reference/concepts/inheritance.md
[initialization]: ./concepts/initialization.md
[instance-attributes]: ./concepts/instance_attributes.md
[instance-methods]: ./concepts/instance_methods.md
[instance-properties]: ./concepts/instance_properties.md
[instantiation]: ./concepts/instantiation.md
[integer-comparison]: ./concepts/integer_comparison.md
[interfaces-general]: ../../../reference/concepts/interfaces.md
[iterables]: ./concepts/iterables.md
[iteration]: ./concepts/iteration.md
[iterators]: ./concepts/iterators.md
[keyword-and]: ./concepts/keywords/and.md
[keyword-as]: ./concepts/keywords/as.md
[keyword-assert]: ./concepts/keywords/assert.md
[keyword-async]: ./concepts/keywords/async.md
[keyword-await]: ./concepts/keywords/await.md
[keyword-break]: ./concepts/keywords/break.md
[keyword-class]: ./concepts/keywords/class.md
[keyword-continue]: ./concepts/keywords/continue.md
[keyword-def]: ./concepts/keywords/def.md
[keyword-del]: ./concepts/keywords/del.md
[keyword-elif]: ./concepts/keywords/elif.md
[keyword-else]: ./concepts/keywords/else.md
[keyword-except]: ./concepts/keywords/except.md
[keyword-false]: ./concepts/keywords/false.md
[keyword-finally]: ./concepts/keywords/finally.md
[keyword-for]: ./concepts/keywords/for.md
[keyword-from]: ./concepts/keywords/from.md
[keyword-global]: ./concepts/keywords/global.md
[keyword-if]: ./concepts/keywords/if.md
[keyword-import]: ./concepts/keywords/import.md
[keyword-in]: ./concepts/keywords/in.md
[keyword-is]: ./concepts/keywords/is.md
[keyword-lambda]: ./concepts/keywords/lambda.md
[keyword-none]: ./concepts/keywords/none.md
[keyword-nonlocal]: ./concepts/keywords/nonlocal.md
[keyword-not]: ./concepts/keywords/not.md
[keyword-only-parameters]: ./concepts/keyword_only_parameters.md
[keyword-or]: ./concepts/keywords/or.md
[keyword-parameters]: ./concepts/keyword_parameters.md
[keyword-pass]: ./concepts/keywords/pass.md
[keyword-raise]: ./concepts/keywords/raise.md
[keyword-return]: ./concepts/keywords/return.md
[keyword-true]: ./concepts/keywords/true.md
[keyword-try]: ./concepts/keywords/try.md
[keyword-while]: ./concepts/keywords/while.md
[keyword-with]: ./concepts/keywords/with.md
[keyword-yield]: ./concepts/keywords/yield.md
[keywords]: ./concepts/keywords/README.md
[library-decimal]: https://docs.python.org/3/library/decimal.html#module-decimal
[library-fractions]: https://docs.python.org/3/library/fractions.html
[library-math]: https://docs.python.org/3/library/math.html
[library-cmath]: https://docs.python.org/3/library/cmath.html#module-cmath
[list-comprehension]: ./concepts/list_comprehension.md
[list-methods]: ./concepts/list_methods.md
[lookup-efficiency]: ./concepts/lookup_efficiency.md
[loops-general]: ../../../reference/concepts/loops.md
[membership-testing]: ./concepts/membership_testing.md
[method-overloading]: ./concepts/method_overloading.md
[metaclasses]: https://docs.python.org/3/library/abc.html#abc.ABCMeta
[methods-general]: ../../../reference/concepts/methods.md
[modular-division]: ./concepts/modular_division.md
[multiple-assignment]: ./concepts/multiple_assignment.md
[mutability]: ./concepts/mutability.md
[mutation-general]: ../../../reference/concepts/mutation.md
[namespaces]: ./concepts/namespaces.md
[nested-functions]: ../../../reference/concepts/nested_functions.md
[non-public-methods]: ./concepts/non_public_methods.md
[objects-general]: ../../../reference/concepts/objects.md
[operator-overloading]: ./concepts/operator_overloading.md
[operator-precedence]: https://docs.python.org/3/reference/expressions.html#operator-summary
[operators]: ./concepts/operators.md
[order-of-evaluation]: ./concepts/order_of_evaluation.md
[partial-application]: ../../../reference/concepts/partial_application.md
[pep-8-style-guide]: ./concepts/pep_8_style_guide.md
[polymorphism-general]: ../../../reference/concepts/polymorphism.md
[positional-only-parameters]: ./concepts/positional_only_parameters.md
[positional-parameters]: ./concepts/positional_parameters.md
[powers-of-two]: ./concepts/powers_of_two.md
[property-decorator]: ./concepts/property_decorator.md
[python-enhancement-proposals]: ./concepts/python_enhancement_proposals.md
[pythonic]: ./concepts/pythonic.md
[raise]: ./concepts/raise.md
[recursion]: ../../../reference/concepts/recursion.md
[recursive-data-structures]: ./concepts/recursive_data_structures.md
[regular-expressions]: ./concepts/regular_expressions.md
[relative-imports]: https://docs.python.org/3/reference/import.html#package-relative-imports
[repl]: ../../../reference/concepts/repl.md
[return-value]: ./concepts/return_value.md
[rich-comparison-methods]: ./concepts/rich_comparison_methods.md
[scope]: ../../../reference/concepts/scope.md
[set-comprehension]: ./concepts/set_comprehension.md
[short-circuiting]: ./concepts/short_circuiting.md
[slicing]: ./concepts/slicing.md
[standard-library]: ./concepts/standard_library.md
[star-args]: ./concepts/star_args.md
[star-star-kwargs]: ./concepts/star_star_kwargs.md
[state]: ../../../reference/concepts/state.md
[static-methods]: ./concepts/static_methods.md
[string-formatting]: ./concepts/string_formatting.md
[string-methods]: ./concepts/string_methods.md
[string-splitting]: ./concepts/string_splitting.md
[string-translation]: ./concepts/string_translation.md
[tuple-unpacking]: ./concepts/tuple_unpacking.md
[type-conversion]: ./concepts/type_conversion.md
[type-hinting]: ./concepts/type_hinting.md
[typing-module]: https://docs.python.org/3/library/typing.html
[variables]: ../../../reference/concepts/variables.md
[while-loops]: ./concepts/while_loops.md
[zen-of-python]: ./concepts/zen_of_python.md

## Proposed Implementations

| Concept Name                         | Topics Included                                                                                                                                                                                                                                                                                                                                                                                                 | Exercise Name                                                                                                                          | Section                                           | Issue Link                                                                                                               | PR Link                                                                                                             |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| \*general                            | [Composition][composition-general]                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                        | `general`, `OOP`                                  | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*general                            | [Data Structures][data-structures]                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                        | `intermediate`, `data-structures`                 | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*general                            | [Encapsulation][encapsulation-general]                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                        | `general`, `OOP`                                  | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*general                            | [Interfaces][interfaces-general]                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                        | `general`, `OOP`                                  | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*general                            | [Lookup efficiency][lookup-efficiency]                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                        | `intermediate`, `data-structures`                 | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*general                            | [Mutation][mutation-general]                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                        | `OOP`                                             | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*general                            | [Mutability in Python][mutability]                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*general                            | [Polymorphism][polymorphism-general]                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                        | `general`, `OOP`                                  | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*general                            | [Recursive data structures][recursive-data-structures]                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                        | `intermediate`, `data-structures`                 | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*general                            | [Scope][scope]                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*general                            | [Standard Library][standard-library]                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                        | `general`, `intermediate`                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*general                            | [State][state]                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                        | `OOP`                                             | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*no stand-alone (multiple concepts) | [Arguments & Parameters][arguments-and-parameters]                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*no stand-alone (multiple concepts) | [Duck Typing][duck-typing]                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                        | `general`, `OOP`                                  | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*no stand-alone (multiple concepts) | [Dynamic Typing][dynamic-typing]                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                        | `general`, `types`, `OOP`                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*no stand-alone (multiple concepts) | [Everything-is-an-object][everything-is-an-object]                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                        | `OOP`                                             | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*no stand-alone (multiple concepts) | [del][keyword-del]                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                        | `general`, `keyword`                              | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*no stand-alone (multiple concepts) | [Expressions][expressions]                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                        | `basic`                                           | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*no stand-alone (multiple concepts) | [Identity testing][identity-testing]                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*no stand-alone (multiple concepts) | [Immutability][immutability]                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                        | `functional`                                      | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*no stand-alone (multiple concepts) | [Immutability in Python][immutability]                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                        | `general`, `OOP`                                  | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*no stand-alone (multiple concepts) | [Operators][operators]                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*no stand-alone (multiple concepts) | [Operator precedence][operator-precedence]                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*no stand-alone (multiple concepts) | [Order of Evaluation][order-of-evaluation]                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                        | `basic`                                           | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*no stand-alone (multiple concepts) | [type][builtin-types-type]                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                        | `advanced`, `OOP`                                 | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| \*no stand-alone (multiple concepts) | [type conversion][type-conversion]                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                        | `basic`, `builtin`                                | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| aliasing                             | [as][keyword-as]                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                        |                                                   | [ ]()                                                                                                                    |                                                                                                                     |
| argument unpacking                   | [Argument unpacking][argument-unpacking] splat or astrix operator                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                        | `basic`                                           | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| basics                               | [Assignment][assignment], [Variables][variables], [Constants][constants], [Objects][objects-general], [Functions][functions-general], [Function Definition][function-definition], [Arguments & Parameters][arguments-and-parameters], [def][keyword-def], [return][keyword-return], [Return Values][return-value], [Docstrings][docstrings], [Comments][comments-general],                                      | [Guidos Gorgeous Lasagna](https://github.com/exercism/v3/tree/master/languages/python/exercises/concept/guidos-gorgeous-lasagna)       | `general`                                         | [#1999](https://github.com/exercism/v3/issues/1999)                                                                      | [#2052](https://github.com/exercism/v3/pull/2052)                                                                   |
| binary data                          |                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                        |                                                   | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| bitwise                              | [Bitwise manipulation][bitwise-manipulation-general]                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| bitwise                              | [Bitwise operators][bitwise-operators]                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| bools                                | [**boo**l][builtin-types-bool], [Boolean operators][boolean-operators], [Boolean values][boolean-values], [False][keyword-false], [True][keyword-true], [and][keyword-and], [or][keyword-or]                                                                                                                                                                                                                    | [ghost-gobble-arcade-game](https://github.com/exercism/v3/tree/master/languages/python/exercises/concept/ghost-gobble-arcade-game)     | `basic`, `types`, `builtins`                      | [#1030](https://github.com/exercism/v3/issues/1030)                                                                      | [#1952](https://github.com/exercism/v3/pull/1952)                                                                   |
| bools-II                             | [Short circuiting][short-circuiting], [Boolean logic][boolean-logic-general], [Booleans are integers][booleans-are-integers],                                                                                                                                                                                                                                                                                   |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| bytes                                | [bytes][builtin-types-bytes], [bytearray][builtin-types-bytearray],                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                        | `intermediate`, `types`, `builtins`               | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| classes                              | [Classes][classes-general], [class][keyword-class], [Constructor][constructor], [property][builtin-types-property], [Instance Attributes][instance-attributes], [Instance Methods][instance-methods], [Instance Properties][instance-properties], [Instantiation][instantiation], [Initialization][initialization], [pass][keyword-pass], [self][keyword-self]                                                  |                                                                                                                                        | `OOP`, `keyword`                                  | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| classes-II                           | [Inheritance][inheritance-general], [Class Inheritance][class-inheritance], [Class Composition][class-composition], [Non-Public Methods][non-public-methods], [Static Methods][static-methods], [Class members][class-members], [Class methods][class-methods], [Property Decorator][property-decorator]                                                                                                        |                                                                                                                                        | `OOP`                                             | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| classes-III                          | [Custom Classes][custom-classes]                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                        | `OOP`                                             | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| classes-IV                           | Multiple Inheritance, MRO, Abstract Base Clases,                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                        |                                                   |                                                                                                                          |                                                                                                                     |
| comparisons                          | [Comparisons][comparisons-general], [Comparison operators][comparison-operators], [Equivalence][equivalence], [Equality operator][equality-operator], [Inequality][inequality]                                                                                                                                                                                                                                  |                                                                                                                                        | `general`                                         | [#2039](https://github.com/exercism/v3/issues/2039)                                                                      | [ ]()                                                                                                               |
| comparisons-II (rich comparisons)    | [Rich comparison methods][rich-comparison-methods]                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                        | `general`                                         | [#2171](https://github.com/exercism/v3/issues/2171)                                                                      | [ ]()                                                                                                               |
| conditionals                         | [Conditionals][conditionals-general], [Conditional structures][conditional-structures], [if][keyword-if], [elif][keyword-elif], [else][keyword-else], [else][keyword-else]                                                                                                                                                                                                                                      |                                                                                                                                        | `general`                                         | [#1103](https://github.com/exercism/v3/issues/1103)                                                                      | [#2109 ](https://github.com/exercism/v3/pull/2109) <br>note: currently in draft status                              |
| context-handlers                     | [with][keyword-with]                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                        | `intermediate`, `keyword`                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| context-handlers                     | [finally][keyword-finally]                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                        | `intermediate`,, `keyword`                        | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| decorators                           | [decorators][decorators], [Decorators as higher-order functions][decorators-as-higher-order-functions],[Property Decorator][property-decorator]                                                                                                                                                                                                                                                                 |                                                                                                                                        | `functional`, `intermediate`                      | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| dicts                                | [dict][builtin-types-dict]                                                                                                                                                                                                                                                                                                                                                                                      | [Inventory Management](https://github.com/exercism/v3/tree/master/languages/python/exercises/concept/inventory-management)             | `basic`, `types`, `containers`                    | [#877](https://github.com/exercism/v3/issues/877)                                                                        | [#1504](https://github.com/exercism/v3/pull/1504)                                                                   |
| enums                                | [enums][enums]                                                                                                                                                                                                                                                                                                                                                                                                  | [log-levels](https://github.com/exercism/v3/tree/master/languages/python/exercises/concept/log-levels)                                 | `general`                                         | [#2309](https://github.com/exercism/v3/issues/2309)                                                                      | [#2312](https://github.com/exercism/v3/pull/2312)                                                                   |
| enums-II                             | [bitflags][bitflags]                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| exceptions                           | [Exceptions][exceptions-general], [Exception message][exception-message], [raise][raise]                                                                                                                                                                                                                                                                                                                        |                                                                                                                                        | `exceptions`, `intermediate`, `keyword`           | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| exceptions-II                        | [Exception catching][exception-catching], [Exception handling][exception-handling], [try][keyword-try], [except][keyword-except], [finally][keyword-finally]                                                                                                                                                                                                                                                    |                                                                                                                                        | `intermediate`                                    | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| exceptions-III                       | [Exception hierarchy][exception-hierarchy], Custom Exceptions                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                        |                                                   | [ ]()                                                                                                                    |                                                                                                                     |
| functions                            | [Call semantics][call-semantics],[Arguments & Parameters][arguments-and-parameters], [Keyword parameters][keyword-parameters], [Positional parameters][positional-parameters], [Default arguments][default-arguments], [Positional-only parameters][positional-only-parameters], [Keyword-only parameters][keyword-only-parameters], [`*args`][star-args], [`**kwargs`][star-star-kwargs], [None][keyword-none] |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| functions-II                         | [Function Signature][function-signature], [pass][keyword-pass], [Higher-order functions][higher-order-functions], [Nested functions][nested-functions], closures, [global][keyword-global], [nonlocal][keyword-nonlocal]                                                                                                                                                                                        |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| functions-III                        | [Anonymous functions][anonymous-functions-general], [lambda][keyword-lambda]                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                        |                                                   | [ ]()                                                                                                                    |                                                                                                                     |
| functions-IV                         | recursion, dynamic programming                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                        | `functional`                                      | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| generator expressions                | [Generator expression][generator-comprehension]                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                        | `intermediate`                                    | [#1384](https://github.com/exercism/v3/issues/1384)                                                                      | [ ]()                                                                                                               |
| generators                           | [Generators][generators], [yield][keyword-yield]                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                        | `general`, `intermediate`                         | [#1378](https://github.com/exercism/v3/issues/1378)                                                                      | [ ]()                                                                                                               |
| import                               | [import][keyword-import], [importing][importing], relative imports, [from][keyword-from], [as][keyword-as]                                                                                                                                                                                                                                                                                                      |                                                                                                                                        | `intermediate`,`keyword`                          | [#1516](https://github.com/exercism/v3/issues/1516)                                                                      | [ ]()                                                                                                               |
| iteration/loops                      | [Loops][loops-general], [for loops][for-loops], [while loops][while-loops], [while][keyword-while], [for][keyword-for], [range][builtin-types-range], [Exiting loops][exiting-loops], [break][keyword-break], [continue][keyword-continue]                                                                                                                                                                      | [Making the Grade](https://github.com/exercism/v3/tree/master/languages/python/exercises/concept/making-the-grade)                     | `general`, `keyword`                              | [#1430](https://github.com/exercism/v3/issues/1430)                                                                      | [#2302 ](https://github.com/exercism/v3/pull/2302)                                                                  |
| iteration/loops-II                   | [Enumerated values][enumerated-values], [Enumerate][enumerate-built-in]                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                        |                                                   | [ ]()                                                                                                                    |                                                                                                                     |
| iterators                            | [Iterables][iterables], [Iterators][iterators], [Iteration][iteration]                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| iterators-II                         | [map][builtin-functions-map], [filter][builtin-functions-filter]                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                        | `functional`, `builtin`                           | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| list-comprehensions                  | [Comprehension Syntax][comprehension-syntax], [list comprehension][list-comprehension], comprehensions are optimized loops                                                                                                                                                                                                                                                                                      |                                                                                                                                        | `intermediate`                                    | [#1361](https://github.com/exercism/v3/issues/1361)                                                                      | [ ]()                                                                                                               |
| list-methods                         | [list methods][list-methods]                                                                                                                                                                                                                                                                                                                                                                                    | [Chaitanas Collasal Coaster](https://github.com/exercism/v3/tree/master/languages/python/exercises/concept/chaitanas-colossal-coaster) | `basic`                                           | [#2170](https://github.com/exercism/v3/issues/2170)                                                                      | [#2303 ](https://github.com/exercism/v3/pull/2303)                                                                  |
| lists                                | [list][builtin-types-list]                                                                                                                                                                                                                                                                                                                                                                                      | [Elyses Enchantments](https://github.com/exercism/v3/tree/master/languages/python/exercises/concept/elyses-enchantments)               | `basic`, `types`, `builtin`, `containers`         | [#859](https://github.com/exercism/v3/issues/859)                                                                        | [#1583](https://github.com/exercism/v3/pull/1583)                                                                   |
| memoryview                           | [memoryview][builtin-types-memoryview]                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                        | `advanced`, `types`, `builtins`                   | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| multiple assignment                  | [Multiple assignment][multiple-assignment], [Tuple unpacking][tuple-unpacking]                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| namespaces                           | [Namespaces][namespaces]                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| no stand-alone (multiple concepts)   | [Membership testing][membership-testing],[in][keyword-in] [is][keyword-is], [not][keyword-not]                                                                                                                                                                                                                                                                                                                  |                                                                                                                                        | `basic`, `keyword`                                | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| none                                 | [None][keyword-none]                                                                                                                                                                                                                                                                                                                                                                                            | [Restaurant Rozalynn](https://github.com/exercism/v3/tree/master/languages/python/exercises/concept/restaurant-rozalynn)               | `basic`, `builtin`, `keyword`                     | [#1031](https://github.com/exercism/v3/issues/1031)                                                                      | [#2283](https://github.com/exercism/v3/pull/2283)                                                                   |
| numbers-I                            | numbers-I, [int][builtin-types-int], [float][builtin-types-float], [Arithmetic][arithmetic-general], [Integer comparison][integer-comparison], [Modular Division][modular-division], % operator                                                                                                                                                                                                                 | [Currency Exchange](Chandler's Conversion Confusion)                                                                                   | `basic`, `types`, `builtin`                       | [#2208](https://github.com/exercism/v3/issues/2208) <br>note: modular-division missing currently needs improvement issue | [#2875](https://github.com/exercism/v3/pull/2875) <br>note: missing modulus operator and needs an improvement issue |
| numbers-II                           | [complex][builtin-types-complex]                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                        | `intermediate`, `types`, `builtin`                | [#2208](https://github.com/exercism/v3/issues/2208) <br>note: same issue as float/int, but will be its own exercise      | [ ]()                                                                                                               |
| numbers-III                          | [Binary numbers][binary-numbers]                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| numbers-IV                           | [Powers of Two][powers-of-two],conversion between oct, hex, binary??                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| object                               | [object][builtin-types-object]                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                        | `advanced`, `OOP`                                 | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| operator-overloading                 | [Operator overloading][operator-overloading]                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| other-comprehensions                 | [Set comprehension][set-comprehension], [Dict comprehension][dict-comprehension]                                                                                                                                                                                                                                                                                                                                |                                                                                                                                        | `intermediate`                                    | [#1376 ](https://github.com/exercism/v3/issues/1376)                                                                     | [ ]()                                                                                                               |
| partial-application                  | [Partial application][partial-application]                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                        | `functional`, `intermediate`                      | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| recursion                            | [recursion][recursion], [recursion limit][recursion-limit]                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                        | `functional`                                      | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| regular expressions-I                | [Regular Expressions][regular-expressions]                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                        | `intermediate`                                    | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| regular expressions-II               | str methods vs re, regex vs re, unicode regular expressions                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                        |                                                   | [ ]()                                                                                                                    |                                                                                                                     |
| sequences                            | [Bracket notation][bracket-notation], [Indexing][indexing], [slice][builtin-types-slice], [Slicing][slicing], [slice assignment][slice-assignment]                                                                                                                                                                                                                                                              |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| sets                                 | [set][builtin-types-set], [frozenset][builtin-types-frozenset], set operations, set operators, set methods                                                                                                                                                                                                                                                                                                      |                                                                                                                                        | `intermediate`, `types`, `builtins`, `containers` | [#1086 ](https://github.com/exercism/v3/issues/1086)                                                                     | [ ]()                                                                                                               |
| str                                  | [str][builtin-types-str]                                                                                                                                                                                                                                                                                                                                                                                        | [Processing Logs](https://github.com/exercism/v3/tree/master/languages/python/exercises/concept/processing-logs)                       | `basic`, `types`, `builtin`                       | N/A                                                                                                                      | [#824](https://github.com/exercism/v3/pull/824) <br>note: needs re-write and an improvement issue logged            |
| str-formatting                       | [String translation][string-translation]                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                        | `basic`                                           | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| str-formatting                       | [String formatting][string-formatting]                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                        | `basic`                                           | [#1647](https://github.com/exercism/v3/issues/1647)                                                                      | [#2204](https://github.com/exercism/v3/pull/2204) <br>note: PR currently draft, may be re-written                   |
| str-methods                          | [String methods][string-methods]                                                                                                                                                                                                                                                                                                                                                                                | [Litte Sister's Essay](https://github.com/exercism/v3/tree/master/languages/python/exercises/concept/little-sisters-essay)             | `basic`                                           | [#2175](https://github.com/exercism/v3/issues/2175)                                                                      | [#2847](https://github.com/exercism/v3/pull/2847)                                                                   |
| str-methods-II                       | [String splitting][string-splitting]                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                        | `basic`                                           | [#1648](https://github.com/exercism/v3/issues/1648) <br>note: may get re-worked as part of a string exercise progression | [ ]()                                                                                                               |
| testing                              | [assert][keyword-assert]                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                        | `exceptions`, `intermediate`, `keyword`           | [ ]()                                                                                                                    | [ ]()                                                                                                               |
| text-processing                      |                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                        |                                                   | [ ]()                                                                                                                    |                                                                                                                     |
| tuples                               | [tuple][builtin-types-tuple]                                                                                                                                                                                                                                                                                                                                                                                    | [Tisbury Treasure Hunt](https://github.com/exercism/v3/tree/master/languages/python/exercises/concept/tisbury-treasure-hunt)           | `basic`, `types`, `builtin`, `containers`         | [#1097](https://github.com/exercism/v3/issues/1097)                                                                      | [#1824](https://github.com/exercism/v3/pull/1824)                                                                   |
| type-hinting                         | [Type hinting][type-hinting]                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                        | `general`                                         | [ ]()                                                                                                                    | [ ]()                                                                                                               |