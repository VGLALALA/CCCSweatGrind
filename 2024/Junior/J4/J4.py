"""

Problem J4: Troublesome Keys
Improved Solution
Given the peculiar behavior of Alex's keyboard, where one key (the silly key) always types a wrong letter and another key (the quiet key) types nothing, the task is to identify these keys based on the sequence of keys pressed and the resulting text displayed. The constraints include handling both small (N≤50) and large (N≤500,000) input sizes efficiently.

Input Specification:
The input consists of two lines. The first line contains the sequence of keys pressed by Alex, and the second line contains the resulting text displayed. Both lines consist only of lowercase letters.

Output Specification:
The output should consist of two lines. The first line should display the letter corresponding to the silly key and the wrong letter it displays, separated by a space. The second line should display the letter corresponding to the quiet key, or a dash (-) if the quiet key was not pressed.

Algorithm:
1. Initialize variables to track the potential silly and quiet keys, and a flag to indicate if the previous key was quiet.
2. Iterate through the sequence of keys pressed and the displayed text in parallel, comparing each key pressed with the corresponding displayed letter.
3. If a mismatch is found and the previous key was not quiet, mark the current key as potentially quiet and move to the next key.
4. If a mismatch is found and the previous key was quiet, identify the current key as the silly key and the corresponding displayed letter as the wrong letter.
5. If no mismatches are found, continue to the next pair of keys.
6. After iterating through all keys, if no quiet key was identified, return the silly key and wrong letter, along with a dash for the quiet key.
7. If a quiet key was identified, return the silly key, wrong letter, and the quiet key.

Sample Input 1:
forloops
fxrlxxps

Expected Output 1:
o x
-

Sample Input 2:
forloops
fxrlxxp

Expected Output 2:
o x
s

"""

def thing(s1, s2):
    offset = 0
    quiet = '-'
    silly = ''
    for i, c in enumerate(s1):
        if i-offset < len(s2) and c == s2[i-offset]:
            continue
        elif c == quiet:
            offset+=1
            continue
        elif (i+1 == len(s1) and i-offset >= len(s2)) or (i+1 < len(s1) and i-offset < len(s2) and s2[i-offset] == s1[i+1]):
            quiet = s1[i]
            offset += 1
        else:
            silly = (c, s2[i-offset])
    print(' '.join(silly))
    print(quiet)

def takeinput():
    p = input()
    d = input()
    return p,d
p,d = takeinput()
thing(p,d)




