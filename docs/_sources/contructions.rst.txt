***************************************
Regular Expression to Finite Automata
***************************************

Converting regular expressions to finite automata is essential for implementing regex engines and understanding computational complexity. Let's master Thompson's construction and other systematic methods.

.. admonition:: Construction Methods
   :class: admonition-concept

   **Main Approaches:**
   
   1. **Thompson's Construction**: Build NFA recursively from regex components
   2. **Direct Construction**: Build DFA directly for simple patterns
   3. **Hybrid Method**: NFA via Thompson's, then convert to DFA

******************
Thompson's Construction
******************

Thompson's method builds NFAs with ε-transitions by recursively combining smaller automata.

.. admonition:: Base Cases for Thompson's Construction
   :class: admonition-example

   **Empty Set (∅):**

   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2cm, on grid, auto]
      \node[state, initial] (q0) {$q_0$};
   
   *No accepting state - accepts nothing*

   **Empty String (ε):**

   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2cm, on grid, auto]
      \node[state, initial, accepting, fill=green!20] (q0) {$q_0$};
   
   *Start state is accepting - accepts only empty string*

   **Single Symbol (a):**

   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2.5cm, on grid, auto]
      \node[state, initial] (q0) {$q_0$};
      \node[state, accepting, fill=green!20] (q1) [right=of q0] {$q_1$};
      \path[->]
        (q0) edge node {a} (q1);
   
   *Accepts exactly the string "a"*

***********************************
Recursive Construction Rules
***********************************

Union (A + B)
=============

.. admonition:: Union Construction: A + B
   :class: admonition-example

   **Given NFAs for A and B, construct NFA for A + B:**

   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2.5cm, on grid, auto]
      \node[state, initial] (start) {$q_s$};
      \node[state] (A_start) [above right=of start] {$A_s$};
      \node[state] (B_start) [below right=of start] {$B_s$};
      \node[state, accepting, fill=green!20] (A_final) [right=of A_start] {$A_f$};
      \node[state, accepting, fill=green!20] (B_final) [right=of B_start] {$B_f$};
      \node[state, accepting, fill=green!20] (final) [below right=of A_final] {$q_f$};
      \path[->]
        (start) edge node {$\epsilon$} (A_start)
        (start) edge node {$\epsilon$} (B_start)
        (A_final) edge node {$\epsilon$} (final)
        (B_final) edge node {$\epsilon$} (final)
        (A_start) edge node {NFA A} (A_final)
        (B_start) edge node {NFA B} (B_final);

   **Key Points:**
   - New start state with ε-transitions to both A and B
   - New final state with ε-transitions from both final states
   - Original NFAs remain unchanged internally

Concatenation (AB)
==================

.. admonition:: Concatenation Construction: AB
   :class: admonition-example

   **Given NFAs for A and B, construct NFA for AB:**

   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2.5cm, on grid, auto]
      \node[state, initial] (A_start) {$A_s$};
      \node[state] (A_final) [right=of A_start] {$A_f$};
      \node[state] (B_start) [right=of A_final] {$B_s$};
      \node[state, accepting, fill=green!20] (B_final) [right=of B_start] {$B_f$};
      \path[->]
        (A_start) edge node {NFA A} (A_final)
        (A_final) edge node {$\epsilon$} (B_start)
        (B_start) edge node {NFA B} (B_final);

   **Key Points:**
   - A's final state connects to B's start state via ε-transition
   - A's final state is no longer accepting
   - Only B's final state accepts

Kleene Star (A*)
================

.. admonition:: Kleene Star Construction: A*
   :class: admonition-example

   **Given NFA for A, construct NFA for A*:**

   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2.5cm, on grid, auto]
      \node[state, initial, accepting, fill=green!20] (start) {$q_s$};
      \node[state] (A_start) [right=of start] {$A_s$};
      \node[state] (A_final) [right=of A_start] {$A_f$};
      \node[state, accepting, fill=green!20] (final) [right=of A_final] {$q_f$};
      \path[->]
        (start) edge node {$\epsilon$} (A_start)
        (start) edge [bend left=60] node {$\epsilon$} (final)
        (A_start) edge node {NFA A} (A_final)
        (A_final) edge node {$\epsilon$} (final)
        (A_final) edge [bend left=60] node {$\epsilon$} (A_start);

   **Key Points:**
   - New start state (also accepting for ε)
   - ε-transition from start directly to final (for zero repetitions)
   - ε-transition from A's final back to A's start (for repetition)
   - New final state to maintain single-final-state property

************************************
Complete Construction Examples
************************************

.. admonition:: Example 1: Regular Expression (a+b)*
   :class: admonition-example

   **Step-by-Step Construction:**

   **Step 1:** Build NFAs for 'a' and 'b'
   
   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2cm, on grid, auto]
      \node[state, initial] (q0) {$q_0$};
      \node[state, accepting, fill=green!20] (q1) [right=of q0] {$q_1$};
      \path[->] (q0) edge node {a} (q1);

   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2cm, on grid, auto]
      \node[state, initial] (p0) {$p_0$};
      \node[state, accepting, fill=green!20] (p1) [right=of p0] {$p_1$};
      \path[->] (p0) edge node {b} (p1);

   **Step 2:** Union (a+b)
   
   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2.5cm, on grid, auto]
      \node[state, initial] (start) {$s$};
      \node[state] (q0) [above right=of start] {$q_0$};
      \node[state] (p0) [below right=of start] {$p_0$};
      \node[state] (q1) [right=of q0] {$q_1$};
      \node[state] (p1) [right=of p0] {$p_1$};
      \node[state, accepting, fill=green!20] (final) [below right=of q1] {$f$};
      \path[->]
        (start) edge node {$\epsilon$} (q0)
        (start) edge node {$\epsilon$} (p0)
        (q0) edge node {a} (q1)
        (p0) edge node {b} (p1)
        (q1) edge node {$\epsilon$} (final)
        (p1) edge node {$\epsilon$} (final);

   **Step 3:** Kleene Star (a+b)*
   
   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2cm, on grid, auto]
      \node[state, initial, accepting, fill=green!20] (new_start) {$s'$};
      \node[state] (union_start) [right=of new_start] {$s$};
      \node[state] (union_final) [right=3cm of union_start] {$f$};
      \node[state, accepting, fill=green!20] (new_final) [right=of union_final] {$f'$};
      \path[->]
        (new_start) edge node {$\epsilon$} (union_start)
        (new_start) edge [bend left=45] node {$\epsilon$} (new_final)
        (union_start) edge node {Union NFA} (union_final)
        (union_final) edge node {$\epsilon$} (new_final)
        (union_final) edge [bend left=45] node {$\epsilon$} (union_start);

.. admonition:: Example 2: Regular Expression ab*c
   :class: admonition-example

   **Step-by-Step Construction:**

   **Step 1:** Build NFAs for 'a', 'b', and 'c'

   **Step 2:** Build b*
   
   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2.5cm, on grid, auto]
      \node[state, initial, accepting, fill=green!20] (s) {$s$};
      \node[state] (b0) [right=of s] {$b_0$};
      \node[state] (b1) [right=of b0] {$b_1$};
      \node[state, accepting, fill=green!20] (f) [right=of b1] {$f$};
      \path[->]
        (s) edge node {$\epsilon$} (b0)
        (s) edge [bend left=60] node {$\epsilon$} (f)
        (b0) edge node {b} (b1)
        (b1) edge node {$\epsilon$} (f)
        (b1) edge [bend left=60] node {$\epsilon$} (b0);

   **Step 3:** Concatenate a(b*)c
   
   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2cm, on grid, auto]
      \node[state, initial] (a0) {$a_0$};
      \node[state] (a1) [right=of a0] {$a_1$};
      \node[state, accepting, fill=green!20] (bstar_start) [right=of a1] {$s$};
      \node[state, accepting, fill=green!20] (bstar_end) [right=2cm of bstar_start] {$f$};
      \node[state] (c0) [right=of bstar_end] {$c_0$};
      \node[state, accepting, fill=green!20] (c1) [right=of c0] {$c_1$};
      \path[->]
        (a0) edge node {a} (a1)
        (a1) edge node {$\epsilon$} (bstar_start)
        (bstar_start) edge node {$b^*$} (bstar_end)
        (bstar_end) edge node {$\epsilon$} (c0)
        (c0) edge node {c} (c1);

************************************
Direct Construction Methods
************************************

For Simple Patterns
===================

.. admonition:: Direct Construction: Pattern a*b+
   :class: admonition-example

   **Regular Expression:** :math:`a^*b^+`
   
   **Direct NFA Construction:**

   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2.5cm, on grid, auto]
      \node[state, initial] (q0) {$q_0$};
      \node[state] (q1) [right=of q0] {$q_1$};
      \node[state, accepting, fill=green!20] (q2) [right=of q1] {$q_2$};
      \path[->]
        (q0) edge [loop above] node {a} ()
        (q0) edge node {b} (q1)
        (q1) edge node {b} (q2)
        (q2) edge [loop above] node {b} ();

   **Explanation:** 
   - State q₀: Read zero or more a's, then must see b
   - State q₁: Saw first b, need at least one more
   - State q₂: Accepting, can read more b's

.. admonition:: Direct Construction: Pattern (ab)*
   :class: admonition-example

   **Regular Expression:** :math:`(ab)^*`
   
   **Direct NFA Construction:**

   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2.5cm, on grid, auto]
      \node[state, initial, accepting, fill=green!20] (q0) {$q_0$};
      \node[state] (q1) [right=of q0] {$q_1$};
      \path[->]
        (q0) edge [bend left] node {a} (q1)
        (q1) edge [bend left] node {b} (q0);

   **Explanation:**
   - Start state q₀ is accepting (empty string accepted)
   - Cycle: a takes us to q₁, b returns to q₀
   - Only complete "ab" cycles are accepted

Complex Pattern Construction
===========================

.. admonition:: Example 3: Regular Expression (a+b)*abb
   :class: admonition-example

   **Pattern Analysis:** Strings ending with "abb"
   
   **Optimized Direct Construction:**

   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2.5cm, on grid, auto]
      \node[state, initial] (q0) {$q_0$};
      \node[state] (q1) [right=of q0] {$q_1$};
      \node[state] (q2) [right=of q1] {$q_2$};
      \node[state, accepting, fill=green!20] (q3) [right=of q2] {$q_3$};
      \path[->]
        (q0) edge [loop above] node {a,b} ()
        (q0) edge node {a} (q1)
        (q1) edge node {b} (q2)
        (q2) edge node {b} (q3)
        (q1) edge [bend right] node {a} (q1)
        (q2) edge [bend right=60] node {a} (q1)
        (q3) edge [loop above] node {b} ()
        (q3) edge [bend right=70] node {a} (q1);

   **State Meanings:**
   - q₀: Haven't started "abb" pattern
   - q₁: Saw 'a', looking for "bb"
   - q₂: Saw "ab", need one more 'b'
   - q₃: Saw "abb", accepting (but can continue)

************************************
Optimization Techniques
************************************

.. admonition:: State Minimization After Construction
   :class: admonition-concept

   **Common Optimizations:**
   
   1. **ε-transition removal**: Convert ε-NFA to NFA
   2. **State merging**: Combine equivalent states
   3. **Dead state elimination**: Remove unreachable states
   4. **DFA conversion**: Use subset construction for determinism

.. admonition:: Example 4: Before and After Optimization
   :class: admonition-example

   **Before Optimization (Thompson's result for a*):**

   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2cm, on grid, auto]
      \node[state, initial, accepting, fill=green!20] (s) {$s$};
      \node[state] (q0) [right=of s] {$q_0$};
      \node[state] (q1) [right=of q0] {$q_1$};
      \node[state, accepting, fill=green!20] (f) [right=of q1] {$f$};
      \path[->]
        (s) edge node {$\epsilon$} (q0)
        (s) edge [bend left=60] node {$\epsilon$} (f)
        (q0) edge node {a} (q1)
        (q1) edge node {$\epsilon$} (f)
        (q1) edge [bend left=60] node {$\epsilon$} (q0);

   **After Optimization:**

   .. tikz::
      :libs: arrows,automata,positioning

      [shorten >=1pt, node distance=2.5cm, on grid, auto]
      \node[state, initial, accepting, fill=green!20] (q0) {$q_0$};
      \path[->] (q0) edge [loop above] node {a} ();

   **Savings:** 4 states → 1 state, 5 transitions → 1 transition

************************************
Interactive Construction Practice
************************************

.. admonition:: Practice 1: Build NFA for (a+b)*a
   :class: admonition-exercise

   **Challenge:** Use Thompson's construction to build an NFA for :math:`(a+b)^*a`

   **Hint:** First build NFAs for 'a', 'b', then union, then star, then concatenate with final 'a'

   .. container:: toggle

      .. admonition:: Step-by-Step Solution
         :class: admonition-solution

         **Final NFA:**
         
         .. tikz::
            :libs: arrows,automata,positioning

            [shorten >=1pt, node distance=2cm, on grid, auto]
            \node[state, initial] (q0) {$q_0$};
            \node[state] (q1) [right=of q0] {$q_1$};
            \node[state, accepting, fill=green!20] (q2) [right=of q1] {$q_2$};
            \path[->]
              (q0) edge [loop above] node {a,b} ()
              (q0) edge node {a} (q1)
              (q1) edge node {a} (q2)
              (q1) edge [bend left] node {b} (q0);

         **Explanation:** This is the optimized version after ε-removal.

.. admonition:: Practice 2: Build NFA for b*ab*
   :class: admonition-exercise

   **Challenge:** Construct minimal NFA directly (not using Thompson's)

   .. container:: toggle

      .. admonition:: Direct Construction Solution
         :class: admonition-solution

         .. tikz::
            :libs: arrows,automata,positioning

            [shorten >=1pt, node distance=2.5cm, on grid, auto]
            \node[state, initial] (q0) {$q_0$};
            \node[state, accepting, fill=green!20] (q1) [right=of q0] {$q_1$};
            \path[->]
              (q0) edge [loop above] node {b} ()
              (q0) edge node {a} (q1)
              (q1) edge [loop above] node {b} ();

         **Language:** Any number of b's, then one 'a', then any number of b's.

.. admonition:: Practice 3: Complex Pattern (aa+bb)*
   :class: admonition-exercise

   **Challenge:** Build NFA for strings of even-length runs of identical symbols

   .. container:: toggle

      .. admonition:: Advanced Solution
         :class: admonition-solution

         .. tikz::
            :libs: arrows,automata,positioning

            [shorten >=1pt, node distance=2.5cm, on grid, auto]
            \node[state, initial, accepting, fill=green!20] (q0) {$q_0$};
            \node[state] (q1) [above right=of q0] {$q_1$};
            \node[state] (q2) [below right=of q0] {$q_2$};
            \path[->]
              (q0) edge node {a} (q1)
              (q0) edge node {b} (q2)
              (q1) edge node {a} (q0)
              (q2) edge node {b} (q0);

         **States:**
         - q₀: Ready for next pair (accepting)
         - q₁: Saw first 'a', need another
         - q₂: Saw first 'b', need another

************************************
Algorithm Complexity Analysis
************************************

.. admonition:: Construction Complexity Comparison
   :class: admonition-concept

   .. list-table:: Time and Space Complexity
      :header-rows: 1
      :widths: 25 25 25 25

      * - **Method**
        - **Time**
        - **Space**
        - **Notes**
      * - Thompson's
        - O(m)
        - O(m)
        - m = regex length
      * - Direct NFA
        - O(m)
        - O(2^m)
        - Worst case exponential
      * - NFA to DFA
        - O(2^n)
        - O(2^n)
        - n = NFA states
      * - Regex to DFA
        - O(2^m)
        - O(2^m)
        - Combined approach

Construction Strategy Guide
==========================

.. list-table:: When to Use Each Method
   :header-rows: 1
   :widths: 30 70

   * - **Method**
     - **Best For**
   * - Thompson's Construction
     - Complex nested expressions, systematic approach needed
   * - Direct NFA Construction
     - Simple patterns, when minimal states are crucial
   * - Direct DFA Construction
     - Very simple patterns, when determinism is required
   * - Hybrid (Thompson + Optimization)
     - General purpose, balanced complexity and result size

.. note:: 💡 Construction Tips

   **Best Practices:**
   
   1. **Start simple**: Master base cases before complex nesting
   2. **Verify incrementally**: Test each construction step
   3. **Optimize later**: Get correct construction first, then minimize
   4. **Use symmetry**: Look for patterns that can simplify construction
   5. **Consider alternatives**: Sometimes direct construction beats Thompson's

   **Common Errors:**
   - Forgetting ε-transitions in Thompson's method
   - Incorrect final state designation
   - Missing self-loops in star constructions
   - Wrong direction of transitions

Next Steps
==========

Master these construction techniques, then explore :doc:`practice` for hands-on exercises and :doc:`assessment` for comprehensive testing of your automata construction skills!
