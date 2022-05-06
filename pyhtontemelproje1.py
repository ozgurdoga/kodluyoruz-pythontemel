input = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output = []
def flatten(x):
    for i in x:
        if type(i) == list:
            flatten(i)
        else:
            output.append(i)
            
            
flatten(input)
print(output)
