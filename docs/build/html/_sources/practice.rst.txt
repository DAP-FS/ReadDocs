========
Practice
========

This section provides structured practice problems for both weak and strong learners. Each problem includes multiple levels of hints and complete solutions.

Guided Practice for Weak Learners
==================================

Problem 1: Basic Construction
-----------------------------

**Task**: Write a regular expression for the language of all strings over :math:`\{a, b\}` that end with "ab".

.. container:: toggle

   .. admonition:: Hint 1 (Structure)
      :class: toggle

      Think about this pattern: [anything][required ending]
      What should come before "ab"?

.. container:: toggle

   .. admonition:: Hint 2 (Building Blocks)
      :class: toggle

      - For "anything over {a,b}": use :math:`(a + b)^*`
      - For "must end with ab": concatenate with :math:`ab`
      - Combine: :math:`(a + b)^*ab`

.. container:: toggle

   .. admonition:: Complete Solution
      :class: toggle

      **Answer**: :math:`(a + b)^*ab`
      
      **Explanation**: 
      - :math:`(a + b)^*` generates any string over :math:`\{a, b\}` (including :math:`\epsilon`)
      - Concatenating with :math:`ab` ensures every string ends with "ab"
      - Examples: :math:`\{ab, aab, bab, aaab, abab, baab, bbab, \ldots\}`

Problem 2: Union Practice
-------------------------

**Task**: Create a regular expression for strings that either:
- Contain only a's, OR
- Contain only b's

.. container:: toggle

   .. admonition:: Hint 1 (Breaking Down)
      :class: toggle

      This is asking for a union of two languages:
      1. Language 1: strings with only a's
      2. Language 2: strings with only b's
      Use the + operator for union.

.. container:: toggle

   .. admonition:: Hint 2 (Individual Parts)
      :class: toggle

      - Only a's (including empty): :math:`a^*`
      - Only b's (including empty): :math:`b^*`  
      - Combine with union: :math:`a^* + b^*`

.. container:: toggle

   .. admonition:: Complete Solution
      :class: toggle

      **Answer**: :math:`a^* + b^*`
      
      **Language**: :math:`L(a^* + b^*) = \{\epsilon, a, aa, aaa, \ldots\} \cup \{\epsilon, b, bb, bbb, \ldots\}`
      
      **Note**: :math:`\epsilon` appears in both parts but union eliminates duplicates.

Problem 3: Star Operation
-------------------------

**Task**: Write a regular expression for strings over :math:`\{0, 1\}` where every 0 is followed by at least one 1.

.. container:: toggle

   .. admonition:: Hint 1 (Pattern Recognition)
      :class: toggle

      What patterns are allowed?
      - Any number of 1's alone: :math:`1^*`
      - 0 followed by at least one 1: :math:`01^+` (where :math:`1^+ = 11^*`)
      
      How do we combine these?

.. container:: toggle

   .. admonition:: Hint 2 (Building the Expression)
      :class: toggle

      Think of valid strings as sequences of:
      - Standalone 1's
      - Blocks of "0 followed by 1's"
      
      Pattern: :math:`(1 + 01^+)^*`
      
      But we can simplify :math:`01^+` as :math:`011^*`

.. container:: toggle

   .. admonition:: Complete Solution
      :class: toggle

      **Answer**: :math:`(1 + 011^*)^*`
      
      **Alternative**: :math:`(1^* \cdot 011^*)^* \cdot 1^*`
      
      **Explanation**: 
      - :math:`1` allows standalone 1's
      - :math:`011^*` ensures every 0 has at least one following 1
      - The star allows any number of these patterns
      - Examples: :math:`\{\epsilon, 1, 11, 01, 011, 0111, 101, 1011, \ldots\}`

Intermediate Practice
=====================

Problem 4: Multiple Conditions  
------------------------------

**Task**: Regular expression for binary strings that:
- Have odd length, AND
- Start with 1

.. container:: toggle

   .. admonition:: Hint 1 (Length Analysis)
      :class: toggle

      For odd length strings starting with 1:
      - Must start with 1 (1 symbol used)
      - Remaining length must be even
      - What generates even-length strings over :math:`\{0,1\}`?

.. container:: toggle

   .. admonition:: Hint 2 (Even Length Construction)
      :class: toggle

      Even-length strings can be built as pairs:
      - :math:`((0+1)(0+1))^*` generates all even-length strings
      - Alternatively: :math:`(00 + 01 + 10 + 11)^*`
      
      So our pattern: :math:`1 \cdot \text{[even-length strings]}`

.. container:: toggle

   .. admonition:: Complete Solution
      :class: toggle

      **Answer**: :math:`1((0+1)(0+1))^*` or :math:`1(00+01+10+11)^*`
      
      **Verification**:
      - Length 1: :math:`\{1\}` ✓
      - Length 3: :math:`\{100, 101, 110, 111\}` ✓  
      - Length 5: :math:`\{10000, 10001, 10010, \ldots, 11111\}` ✓

Problem 5: Complement Thinking
------------------------------

**Task**: Strings over :math:`\{a, b\}` that do NOT contain "aa" as a substring.

.. container:: toggle

   .. admonition:: Hint 1 (State-Based Approach)
      :class: toggle

      Think of states based on recent characters:
      - State 1: Just saw 'b' or at start (safe)
      - State 2: Just saw 'a' (danger - next 'a' is forbidden)
      
      What transitions are allowed?

.. container:: toggle

   .. admonition:: Hint 2 (Valid Patterns)
      :class: toggle

      From state analysis:
      - Can always read 'b'
      - Can read 'a' only if not just after another 'a'
      - Valid patterns: start with b's, then alternate a's with b's
      
      Try: :math:`b^*(a b^*)^*`

.. container:: toggle

   .. admonition:: Complete Solution
      :class: toggle

      **Answer**: :math:`b^*(ab^*)^*`
      
      **Explanation**:
      - :math:`b^*`: optional starting b's
      - :math:`(ab^*)^*`: any number of "a followed by b's"
      - This ensures no two a's are consecutive
      - Examples: :math:`\{\epsilon, a, b, ab, ba, bb, aba, abb, bab, bba, bbb, \ldots\}`

Advanced Practice for Strong Learners
======================================

Problem 6: Modular Arithmetic
-----------------------------

**Task**: Binary strings representing numbers divisible by 3.

.. container:: toggle

   .. admonition:: Hint (State Machine Approach)
      :class: toggle

      Use remainder states (mod 3):
      - State 0: remainder 0 (accepting - divisible by 3)
      - State 1: remainder 1  
      - State 2: remainder 2
      
      Binary transitions: if current remainder is r and next bit is b,
      new remainder = (2r + b) mod 3

.. container:: toggle

   .. admonition:: Solution Strategy
      :class: toggle

      Build transition table:
      
      .. list-table::
         :header-rows: 1
         
         * - State
           - On 0
           - On 1
         * - 0
           - 0
           - 1
         * - 1  
           - 2
           - 0
         * - 2
           - 1
           - 2
      
      Solve system of equations for state expressions.

.. container:: toggle

   .. admonition:: Complete Solution
      :class: toggle

      **Answer**: :math:`(1(01^*0 + 10^*1)^*1)^* + (0 + 1(01^*0 + 10^*1)^*10^*)`
      
      **Simplified**: Through algebraic manipulation:
      :math:`(0 + 1(01^*0 + 10^*1)^*)^*`
      
      This is complex - usually better to construct via NFA then convert!

Problem 7: Complex Constraints
------------------------------

**Task**: Strings over :math:`\{a, b, c\}` where:
- Number of a's ≡ Number of b's (mod 2)  
- Contains at least one c

.. container:: toggle

   .. admonition:: Approach Hint
      :class: toggle

      This requires tracking:
      1. Parity of (count(a) - count(b))
      2. Whether we've seen a c
      
      Four states needed: {even_diff_no_c, even_diff_has_c, odd_diff_no_c, odd_diff_has_c}

.. container:: toggle

   .. admonition:: Solution Framework
      :class: toggle

      Let E = even difference, O = odd difference, N = no c seen, Y = c seen
      
      States: EN, EY, ON, OY (accepting: EY)
      
      This leads to a complex regular expression - better solved algorithmically.

Challenge Problems
==================

For the following problems, try to construct solutions independently:

**Problem 8**: Palindromes of even length over :math:`\{0, 1\}`

**Problem 9**: Strings where every block of consecutive a's has odd length

**Problem 10**: Binary strings where the number of 01 substrings equals the number of 10 substrings

.. container:: toggle

   .. admonition:: Challenge Hints
      :class: toggle

      Problem 8: Consider that palindromes can be built from center outward
      
      Problem 9: Odd-length blocks look like :math:`a(aa)^*`
      
      Problem 10: This is equivalent to strings that start and end with same symbol!

Assessment Time
===============

Think you're ready for a quiz? Head to :doc:`assessment` to test your knowledge with MCQs and proof problems!

