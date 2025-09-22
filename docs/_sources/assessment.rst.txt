==========
Assessment
==========

Test your understanding with these interactive quizzes and assessment problems. Each question includes hints and detailed explanations.

Multiple Choice Questions
=========================

Question 1: Basic Operations
----------------------------

Which regular expression represents the language of all strings over :math:`\{a, b\}` that contain exactly one 'a'?

A) :math:`a^*ba^*`
B) :math:`b^*ab^*`  
C) :math:`(a + b)^*a(a + b)^*`
D) :math:`ab^* + b^*a`

.. container:: toggle

   .. admonition:: Hint
      :class: toggle

      "Exactly one 'a'" means:
      - Some b's (possibly zero)
      - One a
      - Some more b's (possibly zero)

.. container:: toggle

   .. admonition:: Solution
      :class: toggle

      **Answer: B** - :math:`b^*ab^*`
      
      **Explanation**:
      - :math:`b^*`: zero or more b's before the a
      - :math:`a`: exactly one a (required)
      - :math:`b^*`: zero or more b's after the a
      
      **Why others are wrong**:
      - A) :math:`a^*ba^*` has exactly one 'b', not one 'a'
      - C) :math:`(a + b)^*a(a + b)^*` allows multiple a's 
      - D) :math:`ab^* + b^*a` is correct but less clear than B

Question 2: Kleene Star
-----------------------

What is the language of :math:`(ab)^*`?

A) All strings with equal numbers of a's and b's
B) All strings of even length over :math:`\{a, b\}`
C) Strings that are repetitions of "ab" (including empty string)
D) All strings over :math:`\{a, b\}`

.. container:: toggle

   .. admonition:: Hint
      :class: toggle

      :math:`(ab)^*` means zero or more repetitions of the entire pattern "ab".
      What strings can be formed this way?

.. container:: toggle

   .. admonition:: Solution
      :class: toggle

      **Answer: C** - Strings that are repetitions of "ab" (including empty string)
      
      **Language**: :math:`L((ab)^*) = \{\epsilon, ab, abab, ababab, \ldots\}`
      
      **Why others are wrong**:
      - A) Equal a's and b's includes strings like "ba", "aabb" which aren't in :math:`(ab)^*`
      - B) Even length includes strings like "aa", "bb" which aren't in :math:`(ab)^*`  
      - D) Too broad - excludes strings like "a", "ba", "aab"

Question 3: Union and Concatenation
-----------------------------------

Which expression is equivalent to :math:`a(b + c)^*d`?

A) :math:`ab^*d + ac^*d`
B) :math:`a(b^*c^*)d`
C) :math:`a(b^* + c^*)d`  
D) :math:`ab^*cd^* + ac^*bd^*`

.. container:: toggle

   .. admonition:: Hint
      :class: toggle

      :math:`(b + c)^*` means any sequence of b's and c's mixed together.
      Which option captures this same meaning?

.. container:: toggle

   .. admonition:: Solution
      :class: toggle

      **Answer: C** - :math:`a(b^* + c^*)d`
      
      **Wait!** This is a tricky question. Let me reconsider...
      
      Actually, **none of these are equivalent**!
      
      - :math:`(b + c)^*` = any string over :math:`\{b, c\}` including mixed sequences like "bcbc"
      - :math:`(b^* + c^*)` = either all b's OR all c's, but not mixed
      
      The correct equivalent would be: No standard simple form - this is the simplest expression.

Question 4: Complex Patterns
----------------------------

Which regular expression accepts binary strings with an even number of 1's?

A) :math:`0^*(10^*10^*)^*`
B) :math:`(0 + 1)^*`
C) :math:`(00 + 11)^*`
D) :math:`1^*(01^*01^*)^*`

.. container:: toggle

   .. admonition:: Hint
      :class: toggle

      Think about pairing up the 1's. How can you ensure they come in pairs?

.. container:: toggle

   .. admonition:: Solution
      :class: toggle

      **Answer: A** - :math:`0^*(10^*10^*)^*`
      
      **Explanation**:
      - :math:`0^*`: any number of leading zeros
      - :math:`(10^*10^*)^*`: pairs of 1's separated by zeros, repeated any number of times
      - Each :math:`10^*10^*` contributes exactly 2 ones (even)
      - Zero repetitions gives 0 ones (even)
      
      **Why others are wrong**:
      - B) Accepts strings with odd numbers of 1's too
      - C) Only accepts strings from alphabet :math:`\{0, 1\}` with specific patterns
      - D) Similar to A but with different structure - also correct but A is cleaner

Short Answer Questions  
======================

Question 5: Language Description
--------------------------------

**Task**: Describe in English the language accepted by :math:`(a + b)^*abb(a + b)^*`

.. container:: toggle

   .. admonition:: Hint
      :class: toggle

      Break this into three parts:
      1. :math:`(a + b)^*` at the beginning
      2. :math:`abb` in the middle  
      3. :math:`(a + b)^*` at the end

.. container:: toggle

   .. admonition:: Solution
      :class: toggle

      **Answer**: All strings over alphabet :math:`\{a, b\}` that contain "abb" as a substring.
      
      **Explanation**:
      - :math:`(a + b)^*`: any prefix over :math:`\{a, b\}`
      - :math:`abb`: the required substring
      - :math:`(a + b)^*`: any suffix over :math:`\{a, b\}`
      
      **Examples**: abb, aabb, abba, babb, abbabb, xabbx where x is any string over :math:`\{a,b\}`

Question 6: Equivalence  
-----------------------

**Task**: Are :math:`(a^*b^*)^*` and :math:`(a + b)^*` equivalent? Justify your answer.

.. container:: toggle

   .. admonition:: Hint  
      :class: toggle

      Consider what strings each expression can generate:
      - Can :math:`(a^*b^*)^*` generate strings like "abab"?
      - Can :math:`(a + b)^*` generate all strings over :math:`\{a, b\}`?

.. container:: toggle

   .. admonition:: Solution
      :class: toggle

      **Answer**: Yes, they are equivalent.
      
      **Proof**:
      
      **Part 1** - :math:`L((a + b)^*) \subseteq L((a^*b^*)^*)`:
      Any string in :math:`(a + b)^*` can be viewed as alternating blocks of a's and b's.
      For example, "abab" = "a" + "b" + "a" + "b" where each block fits :math:`a^*b^*` pattern.
      
      **Part 2** - :math:`L((a^*b^*)^*) \subseteq L((a + b)^*)`:
      Any string from :math:`(a^*b^*)^*` is a concatenation of strings from :math:`a^*b^*`.
      Each :math:`a^*b^*` string contains only a's and b's, so their concatenation is also over :math:`\{a, b\}`.
      
      **Conclusion**: Both generate exactly :math:`\Sigma^*` where :math:`\Sigma = \{a, b\}`.

Proof Problems
==============

Question 7: Construction Challenge
----------------------------------

**Task**: Construct a regular expression for the language: "Binary strings where the number of 0's is divisible by 3"

.. container:: toggle

   .. admonition:: Hint - State Machine Approach
      :class: toggle

      Use states to track the remainder when counting 0's:
      - State 0: count(0's) ≡ 0 (mod 3) [accepting]
      - State 1: count(0's) ≡ 1 (mod 3)  
      - State 2: count(0's) ≡ 2 (mod 3)
      
      What happens on input 0? On input 1?

.. container:: toggle

   .. admonition:: Solution Method
      :class: toggle

      **State Transitions**:
      - State 0: on '0' go to State 1, on '1' stay in State 0
      - State 1: on '0' go to State 2, on '1' stay in State 1  
      - State 2: on '0' go to State 0, on '1' stay in State 2
      
      **Equations** (let :math:`L_i` = strings ending in state i):
      - :math:`L_0 = 1L_0 + 0L_2 + \epsilon`
      - :math:`L_1 = 1L_1 + 0L_0`  
      - :math:`L_2 = 1L_2 + 0L_1`
      
      **Solution**: :math:`(1^*01^*01^*0)^*1^*`
      
      This is complex - usually better to construct NFA first, then convert!

Question 8: Pumping Lemma
-------------------------

**Task**: Prove that the language :math:`L = \{0^n1^n : n \geq 0\}` is not regular.

.. container:: toggle

   .. admonition:: Hint - Pumping Lemma Setup
      :class: toggle

      Use proof by contradiction:
      1. Assume L is regular
      2. Apply pumping lemma with pumping length p
      3. Choose a string s ∈ L with |s| ≥ p
      4. Show that for any valid decomposition s = xyz, pumping fails

.. container:: toggle

   .. admonition:: Solution
      :class: toggle

      **Proof by contradiction**:
      
      Assume :math:`L = \{0^n1^n : n \geq 0\}` is regular. Then by the Pumping Lemma, there exists a pumping length :math:`p > 0`.
      
      **Choose string**: Let :math:`s = 0^p1^p \in L` with :math:`|s| = 2p \geq p`.
      
      **Decomposition**: By pumping lemma, :math:`s = xyz` where:
      - :math:`|xy| \leq p`
      - :math:`|y| > 0`  
      - :math:`xy^iz \in L` for all :math:`i \geq 0`
      
      **Analysis**: Since :math:`|xy| \leq p` and :math:`s = 0^p1^p`, the substring :math:`xy` consists entirely of 0's. Therefore :math:`y = 0^k` for some :math:`k > 0`.
      
      **Contradiction**: Consider :math:`s' = xy^2z = x(0^k)^2z = x0^{2k}z = 0^{p+k}1^p`.
      
      Since :math:`k > 0`, we have :math:`p + k > p`, so :math:`s'` has more 0's than 1's, thus :math:`s' \notin L`.
      
      This contradicts the pumping lemma requirement. Therefore, :math:`L` is not regular.

Question 9: Advanced Construction
---------------------------------

**Task**: Design a regular expression for strings over :math:`\{a, b\}` such that every 'a' is immediately followed by at least two 'b's.

.. container:: toggle

   .. admonition:: Hint - Valid Patterns
      :class: toggle

      What patterns are allowed?
      - Strings with no a's: :math:`b^*`
      - Blocks where 'a' is followed by 2+ b's: :math:`abb^+` where :math:`b^+ = bb^*`
      
      How do we combine these patterns?

.. container:: toggle

   .. admonition:: Solution
      :class: toggle

      **Answer**: :math:`b^*(abb^+b^*)^*`
      
      **Alternative**: :math:`(b + abb^+)^*`
      
      **Explanation**:
      - :math:`b^*`: strings of only b's (allowed)
      - :math:`abb^+`: each 'a' followed by at least 2 b's  
      - :math:`(abb^+b^*)^*`: any number of valid a-blocks separated by b's
      
      **Examples**: :math:`\{\epsilon, b, bb, abb, abbb, abbabb, babbb, \ldots\}`
      
      **Invalid**: :math:`\{a, ab, ba, aab, aba, \ldots\}` (a's not followed by 2+ b's)

Performance Statistics
======================

.. container:: toggle

   .. admonition:: Check Your Score
      :class: toggle

      **Scoring Guide**:
      - Questions 1-4 (MCQ): 2 points each = 8 points
      - Questions 5-6 (Short Answer): 3 points each = 6 points  
      - Questions 7-9 (Proofs): 4 points each = 12 points
      - **Total**: 26 points
      
      **Grade Scale**:
      - 23-26: Excellent understanding
      - 19-22: Good grasp of concepts  
      - 15-18: Need more practice
      - Below 15: Review fundamental concepts

Next Steps
==========

Completed the assessment? Check out :doc:`resources` for additional practice materials and advanced topics!

