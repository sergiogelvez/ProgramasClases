def pascal(n):
    if n==1:
        return [1]
    
    if n==2:
        return [1,1]
    
    previous = pascal(n-1)
    output = []
    
    for i in range(len(previous)-1):
        left = previous[i]
        right = previous[i+1]
        output.append(left + right)
    return [1] + output + [1]

print(pascal(5))