from audioop import reverse


input = [[1, 2], [3, 4], [5, 6, 7]]

def ters(x):
    reverse_x = []
    for i in x[::-1]:
        reverse_x.append(i[::-1])
    reverse_x == x
    return reverse_x
print(ters(input))

#Buradaki ana amacım listeyi değiştirirken ana listeyi koruyabilmek oldu.
