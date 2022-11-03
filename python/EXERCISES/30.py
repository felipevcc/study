"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"

"""

strs = ["felipe","inteligencia","libro"]
#strs = ["felipe", "felpa"]
#strs = ["ab", "a"]

def func(strs):
    strs.sort(key=len)
    prefix = ""
   
    for i in range(len(strs)): 
        word = strs[i]
        if len(strs) == 1:
            prefix = word
            break
        prev_prefix = ""
        prev_prefix2 = "" 
        
        try:
            x = len(strs[i+1]) + len(strs[i])
        except:
            break

        for j in range(len(strs[i+1])):
            #print(prev_prefix2)
            word_next = strs[i+1] 
            letter = word_next[j]
            if letter in word:
                prev_prefix2 += letter

            elif letter not in word:
                if len(prev_prefix2) > len(prev_prefix):
                    prev_prefix = prev_prefix2 
                prev_prefix2 = "" 
        
        if len(prev_prefix) <= 1:
            prefix = "" 
            break
        elif prefix == "":
            prefix = prev_prefix 
        elif len(prev_prefix) < len(prefix) and prev_prefix in prefix:
            prefix = prev_prefix 
        else:  
            break

    return prefix

if __name__ == '__main__':
    print(func(strs))

