a=int(input("Enter The No. : "))
if a>1:
    for i in range(2,a):
        if(a%i)==0:
            j=a/i
            print("Prime Factors of %d is : %d * %d " % (a,j,i) )
            break
    else:
        print("Prime Factors is %d * 1" % a)

