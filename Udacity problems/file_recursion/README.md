### Explanation for File recursion Problem

Problem Statement: The goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c" (Or any other suffix)

#### 
**Time Complexity**: Sum of lengths of all paths.
Say avg length of paths: m and
Number of paths: n
TC: O(mn)

**Space Complexity**: Since , function is being called recursively, stack space is being used.
SC: maximum of length of all paths

