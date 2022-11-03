"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

"""

#strs = ["flower", "flow", "flight"]
strs = ["ab", "a"]

def func(strs): 
    str_min = min(strs, key=len)
    #s = str_min[:3]
    letter = []
    close = False
    for i in range(len(str_min)):
        for word in strs:
            word_letter = word[i] 
            try: 
                if letter[i] != word_letter:
                    letter.pop(i)
                    close = True
                    break
            except IndexError:                
                letter.append(word_letter) 

        if close == True:
            break

    return ''.join(letter)

print(func(strs))
