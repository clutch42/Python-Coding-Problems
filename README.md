# Python_Coding_Problems
These were done in the PyCharm IDE
<details>
<summary>
  
## Problem 767 - Strings
</summary>
Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
</details>
<details>
<summary>
  
## Problem 768 - Min / Max
</summary>
Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.
</details>
<details>
<summary>
  
## Problem 769 - Probability
</summary>
Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.
</details>
<details>
<summary>
  
## Problem 770 - Nim Sum
</summary>
The game of Nim is played as follows. Starting with three heaps, each containing a variable number of items, two players take turns removing one or more items from a single pile. The player who eventually is forced to take the last stone loses. For example, if the initial heap sizes are 3, 4, and 5, a game could be played as shown below:

```
  A  |  B  |  C
-----------------
  3  |  4  |  5
  3  |  1  |  3
  3  |  1  |  3
  0  |  1  |  3
  0  |  1  |  0
  0  |  0  |  0 
```
  
In other words, to start, the first player takes three items from pile B. The second player responds by removing two stones from pile C. The game continues in this way until player one takes last stone and loses.

Given a list of non-zero starting values [a, b, c], and assuming optimal play, determine whether the first player has a forced win.
</details>
<details>
<summary>
  
## Problem 771 - Character Mapping
</summary>
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
</details>
<details>
<summary>
  
## Problem 772 - Boggle
</summary>
Boggle is a game played on a 4 x 4 grid of letters. The goal is to find as many words as possible that can be formed by a sequence of adjacent letters 
in the grid, using each cell at most once. Given a game board and a dictionary of valid words, implement a Boggle solver.
</details>
<details>
<summary>
  
## Problem 773 - Inversions / Merge Sort
</summary>
We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
</details>
<details>
<summary>
  
## Problem 774 - Read N Characters from File
</summary>
Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.
</details>
<details>
<summary>
  
## Problem 775 - Overlapping Intervals
</summary>
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
</details>
<details>
<summary>
  
## Problem 776 - Josephus Problem
</summary>
There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with the kth person, and removing every successive kth person going clockwise until there is no one left.
Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.
For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.
Bonus: Find an O(log N) solution if k = 2.
</details>
<details>
<summary>
  
## Problem 777 - Ternary Search Tree
</summary>
A ternary search tree is a trie-like data structure where each node may have up to three children. Here is an example which represents the words code, cob, be, ax, war, and we.
```
       c
    /  |  \
   b   o   w
 / |   |   |
a  e   d   a
|    / |   | \ 
x   b  e   r  e 
```

The tree is structured according to the following rules:
left child nodes link to words lexicographically earlier than the parent prefix
right child nodes link to words lexicographically later than the parent prefix
middle child nodes continue the current word
For instance, since code is the first word inserted in the tree, and cob lexicographically precedes cod, cob is represented as a left child extending from cod.
Implement insertion and search functions for a ternary search tree.
</details>
