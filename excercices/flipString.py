"""
ref: https://leetcode.com/problems/flip-string-to-monotone-increasing/description/
"""

def fliper(s):
    res = 0
    zeros = 0    

    for j in s:
        if j == '0':
            zeros += 1
    
    res = zeros
    for j in s:
        if j == '0':
            zeros -= 1  
            res = min(zeros, res)   
        else:
            zeros += 1           

    return res
     
               
if __name__ == '__main__':
    print(fliper("00110")) # 1
    print(fliper("010110")) # 2
    print(fliper("00011000")) # 2
    print(fliper("0101100011")) # 3
    