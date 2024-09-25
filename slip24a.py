def prime(num):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag=1
            break
        if flag==0:
            print ("number is prime")
        else:
            print("number is not prime")
            def fact(num):
                f=1
                for i in range(1,num+1):
                    f=f*i
                    print("factorial of given number is:",f)
                    n=int(input("enter any number to check:"))
                    print(n)
                    fact(n)
                
