# Experiment 2: SHA-256 Hashing for Data Integrity and Tamper Detection

## Aim
To use hashing techniques to generate a secure SHA-256 hash, verify data integrity, and detect tampering in a file.

## Brief Theory
SHA-256 is a cryptographic hash function from the SHA-2 family. It takes an input of any length and produces a fixed 256-bit digest, which is displayed as a 64-character hexadecimal value. A hash function is one-way, so it is practically impossible to recover the original input from the hash. For the same input, the hash always remains the same, while even a single-bit change in the data produces a completely different hash value.

This property makes SHA-256 highly useful for data integrity checking. If we store a trusted reference hash and later recompute the hash of the current file, then a match indicates the file is unchanged, while a mismatch indicates tampering or accidental modification.

## Methodology
1. A text file named sample.txt was created in the experiment folder.
2. The file content was written as:
   "Network Security is important in it"
3. The Python hashlib library was used to compute the SHA-256 hash of the file in binary mode.
4. The generated hash was saved as a trusted reference value.
5. The original file was verified by comparing the current hash with the stored reference hash.
6. A small change was made in the file by changing "important" to "Important".
7. The SHA-256 hash was computed again for the modified file.
8. The new hash was compared with the original trusted hash.
9. The program also calculated how many hexadecimal characters differed between the two hashes.

## Program File
The complete Python implementation for this experiment is stored separately in the Code folder as a dedicated program file.

> [**View SHA-256 Code**](Code/SHA-256.py)
>
![alt text](Outputs/SHA256.png)
> **SHA-256 Output**

## Result
The original file produced a valid SHA-256 hash consisting of 64 hexadecimal characters. After altering only one letter in the text, the new hash changed completely. The status was reported as Mismatched, which proves that even a small modification in the file can be detected using SHA-256 hashing.

## Discussion
Before making any change, the file matched the trusted reference hash. After changing just one character from lowercase to uppercase, the hash became different. This demonstrates the avalanche effect of SHA-256, where a small input change causes a major change in the output. The experiment shows that hashing is a practical and reliable method for verifying file integrity and detecting tampering.

## Improvements
The program was improved by adding comparison logic that not only shows whether the hash matches or mismatches but also counts the number of differing hexadecimal characters between the original and modified hash values. This gives a clearer visual idea of how much the hash changed and makes the integrity check more informative.

## Conclusion
Through this experiment, SHA-256 hashing was successfully used to check data integrity. The result after changing a single character showed a completely different hash, which proves that SHA-256 is highly effective for detecting data tampering and ensuring file authenticity.
