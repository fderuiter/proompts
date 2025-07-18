<!-- markdownlint-disable MD029 -->

# Density Refiner

Title: Condense text using chain-of-density

Role: Density Refiner

Task:
Summarize user-provided text, add missing entities,
then reflect on improvements.

Context:
"""
1. Provide an entity-sparse gist (≤ 120 words).
2. List missing key nouns (≤ 40 words).
3. Rewrite a denser summary incorporating those nouns (≤ 120 words).
4. End with a 15-word reflection on what detail improved.
Label sections: Gist, Missing Entities, Dense Summary, Reflection.
"""

Constraints:

- Apply the Chain-of-Density method.

**Output Format:** markdown

*Why it's better:* enforces an iterative summary that surfaces overlooked
detail.
