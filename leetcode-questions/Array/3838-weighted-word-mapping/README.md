# 3838. Weighted Word Mapping

**Difficulty:** Easy
**Tags:** Array, String, Simulation
**Language:** python

## Problem

See: https://leetcode.com/problems/weighted-word-mapping/

## My Solution

See `solution.py`

## Approach
The solution processes each word in the input list independently. For each word, it calculates a cumulative "weight sum" by iterating through its characters and looking up their corresponding weights from the provided `weights` list (indexed by `char - 'a'`). This total weight sum for the word is then transformed into a single output character using a modulo 26 operation, followed by a reverse alphabetical mapping (e.g., a modulo result of 0 maps to 'z', 1 maps to 'y', and so on). These derived characters, one for each input word, are concatenated to form the final result string.

## Complexity
- Time: O(S), where `S` is the total number of characters across all words in the input list (`sum(len(word) for word in words)`). Each character is visited and processed exactly once.
- Space: O(N), where `N` is the number of words in the input list. This space is used to store the resulting string, which will have a length equal to `N`.

## Pattern
Simulation, Character Mapping

## Could it be improved?
The current approach is already optimal. It processes each character in the input exactly once to compute the necessary weighted sum, which is the minimum work required to read and process all relevant input data. The space complexity is also optimal as it primarily stores the generated output string.
