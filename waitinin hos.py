a=list(input("enter the name").split(" "))
print(a)
def wait():
    b=0
    for i in a:
        b=b+1
        print(i,"waiting at",b)
wait()
a.append('f')
print("list after adding")
wait()
a.remove(a[2])
print("list after remove")
wait()
a.insert(1,'d')
print("list after adding")
wait()
