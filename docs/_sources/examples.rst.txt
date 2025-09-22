========
Examples
========

This section provides worked examples progressing from basic to advanced regular expressions. Each example includes step-by-step explanations and language descriptions.

Basic Examples
==============

Example 1: Simple Characters
-----------------------------

**Regular Expression**: :math:`abc`

**Language**: :math:`L(abc) = \{abc\}`

**Description**: Matches exactly the string "abc"

.. container:: toggle

   .. admonition:: Explanation
      :class: toggle

      This is the simplest case - literal concatenation of symbols. The language contains only one string.

Example 2: Union/Alternation  
-----------------------------

**Regular Expression**: :math:`a + b`

**Language**: :math:`L(a + b) = \{a, b\}`

**Description**: Matches either "a" or "b"

.. container:: toggle

   .. admonition:: Step-by-step
      :class: toggle

      1. :math:`L(a) = \{a\}`
      2. :math:`L(b) = \{b\}`  
      3. :math:`L(a + b) = L(a) \cup L(b) = \{a\} \cup \{b\} = \{a, b\}`

Example 3: Kleene Star
----------------------

**Regular Expression**: :math:`a^*`

**Language**: :math:`L(a^*) = \{\epsilon, a, aa, aaa, aaaa, \ldots\}`

**Description**: Zero or more repetitions of "a"

.. container:: toggle

   .. admonition:: Understanding Kleene Star
      :class: toggle

      - :math:`(L(a))^0 = \{\epsilon\}` (zero repetitions)
      - :math:`(L(a))^1 = \{a\}` (one repetition)  
      - :math:`(L(a))^2 = \{aa\}` (two repetitions)
      - :math:`L(a^*) = \bigcup_{i=0}^{\infty} (L(a))^i`

Intermediate Examples
=====================

Example 4: Combining Operations
-------------------------------

**Regular Expression**: :math:`(a + b)^*`

**Language**: All strings over alphabet :math:`\{a, b\}`

**Description**: Any sequence of a's and b's, including empty string

.. container:: toggle

   .. admonition:: Detailed Analysis
      :class: toggle

      1. :math:`L(a + b) = \{a, b\}`
      2. :math:`L((a + b)^*) = \{\epsilon, a, b, aa, ab, ba, bb, aaa, aab, \ldots\}`
      3. This generates :math:`\Sigma^*` where :math:`\Sigma = \{a, b\}`

Example 5: Specific Patterns
-----------------------------

**Regular Expression**: :math:`ab^*c`

**Language**: Strings starting with "a", followed by zero or more "b"s, ending with "c"

**Examples**: :math:`\{ac, abc, abbc, abbbc, \ldots\}`

.. container:: toggle

   .. admonition:: Construction Process  
      :class: toggle

      1. Start with :math:`a`: :math:`L(a) = \{a\}`
      2. Concatenate with :math:`b^*`: :math:`L(ab^*) = \{a, ab, abb, abbb, \ldots\}`
      3. Concatenate with :math:`c`: :math:`L(ab^*c) = \{ac, abc, abbc, abbbc, \ldots\}`

Example 6: Multiple Unions
---------------------------

**Regular Expression**: :math:`a^*b^* + c^*`

**Language**: Either (zero or more a's followed by zero or more b's) OR (zero or more c's)

.. container:: toggle

   .. admonition:: Breaking Down the Union
      :class: toggle

      - :math:`L(a^*b^*) = \{\epsilon, a, b, aa, ab, bb, aaa, aab, abb, bbb, \ldots\}`
      - :math:`L(c^*) = \{\epsilon, c, cc, ccc, \ldots\}`
      - :math:`L(a^*b^* + c^*) = L(a^*b^*) \cup L(c^*)`
      - Note: :math:`\epsilon` appears in both, but union eliminates duplicates

Advanced Examples
=================

Example 7: Complex Patterns
----------------------------

**Regular Expression**: :math:`(a + b)^*a(a + b)^*`

**Language**: All strings over :math:`\{a, b\}` containing at least one "a"

**Description**: Any string that has at least one occurrence of the symbol "a"

.. container:: toggle

   .. admonition:: Advanced Analysis
      :class: toggle

      This pattern ensures at least one "a" by:
      1. :math:`(a + b)^*` - any prefix
      2. :math:`a` - guaranteed "a"  
      3. :math:`(a + b)^*` - any suffix
      
      Alternative representation: :math:`\Sigma^* - b^*` (complement of strings with only b's)

Example 8: Even/Odd Patterns
-----------------------------

**Regular Expression**: :math:`(aa)^*`

**Language**: Strings with even number of a's (including zero)

**Examples**: :math:`\{\epsilon, aa, aaaa, aaaaaa, \ldots\}`

.. container:: toggle

   .. admonition:: Pattern Recognition
      :class: toggle

      This demonstrates how regular expressions can capture mathematical properties:
      - Even number = pairs of elements
      - :math:`(aa)^*` groups a's in pairs
      - Only generates strings where |string| ≡ 0 (mod 2)

Example 9: Practical Application
---------------------------------

**Regular Expression**: :math:`(0 + 1)^*01(0 + 1)^*`

**Language**: Binary strings containing "01" as a substring

**Description**: Any binary string that contains the pattern "01" somewhere

.. container:: toggle

   .. admonition:: Real-World Connection
      :class: toggle

      This type of pattern is useful for:
      - Finding specific bit patterns in computer science
      - Detecting state transitions (0→1)
      - Pattern matching in text processing
      
      Structure: [any prefix][required pattern][any suffix]

Challenging Examples
====================

Example 10: Multiple Constraints
---------------------------------

**Regular Expression**: :math:`0^*(10^*10^*)^*`

**Language**: Binary strings with even number of 1's

.. container:: toggle

   .. admonition:: Complex Pattern Analysis
      :class: toggle

      Breaking down the structure:
      1. :math:`0^*` - optional leading zeros
      2. :math:`(10^*10^*)^*` - pairs of 1's separated by zeros
      3. Each iteration of the outer star adds exactly two 1's
      4. Result: strings where number of 1's ≡ 0 (mod 2)

.. container:: toggle

   .. admonition:: Alternative Construction
      :class: toggle

      This could also be built using state-based thinking:
      - State 0: even number of 1's seen (accepting)
      - State 1: odd number of 1's seen (non-accepting)
      - Transitions: 0 keeps state, 1 toggles state

Practice Problems
=================

Try constructing regular expressions for these languages:

1. Strings over :math:`\{a, b\}` that start and end with the same symbol
2. Binary strings representing multiples of 3
3. Strings with no three consecutive identical characters

.. container:: toggle

   .. admonition:: Hints for Practice Problems
      :class: toggle

      1. Consider cases: starts with a, starts with b
      2. Use modular arithmetic with 3 states
      3. Think about forbidden patterns and their complements

Next Steps
==========

Ready to test your understanding? Move on to :doc:`practice` for guided exercises, or jump to :doc:`assessment` for challenging problems.
