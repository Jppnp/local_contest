def main():
    text1 = input()
    text2 = input()
    n = len(text1)
    m = len(text2)
    copy = float((max(n,m)) / 3 )
    text1 = list(text1)
    text2 = list(text2)

    if(m < n):
        text1 , text2 = text2, text1
        n, m = m, n
    different = 0
    for i in range(n):
        if(text1[i] != text2[i]):
            different += 1

    different += abs(n - m)
    print(int(copy))
    if(different >= int(copy)):
        print("no")
    else:
        print("yes")
    

main()