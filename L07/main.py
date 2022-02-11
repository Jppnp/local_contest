
def main():
    n = int(input())
    text = input()
    q = text.split(" ")
    q.sort(reverse=True)
    pair = 0
    sum = 0
    status = True
    for i in range(n-1):
        if (status) :
            if (abs(int(q[i]) - int(q[i+1])) < 10):
                pair += 1
                avg = (int(q[i]) + int(q[i+1]))
                sum += avg / 2
                status = False
        else:
            status = True
    if(pair == 0):
        print("0.00")
    else:
        sum = float(sum / pair)
        print("%.2f" %sum)

main()