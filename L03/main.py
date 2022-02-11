from operator import itemgetter

def main():
    n = int(input())
    offer = []
    p = []
    s = []
    for i in range(n+1):
        p.append(0)
        s.append(0)
    offer.append(['0', '0', '0'])
    for i in range(n):
        text = input()
        offer.append(text.split(" "))
    offer.sort(key= lambda l: int(l[1]))
    for i in range(n+1):
        if(i == 0):
            p[i] = 0
            continue
        for j in range(i-1,0,-1):
            if(offer[i][0] >= offer[j][1]):
                if(p[i] != 0):
                    if(offer[j][2] > offer[p[i]][2]):
                        p[i] = j 
                else:
                    p[i] = j
    for i in range(1,n+1):
        s[i] = max(int(offer[i][2]) + int(offer[p[i]][2]), s[i-1] )
    print(s[n])

main()

