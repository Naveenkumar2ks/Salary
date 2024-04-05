def salary(n):
    da=(10*n)/100;
    ta=(12*n)/100;
    gs=n+da+ta;
    return gs;

n=int(input("Enter the basic salary:"));
t=salary(n);
print(t)
