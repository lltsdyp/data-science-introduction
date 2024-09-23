def hanoi(num,src,dst,third):
    if num==1:
        print("Move {} -> {}".format(src,dst))
    else:
        hanoi(num-1,src,third,dst)
        print("Move {} -> {}".format(src,dst))
        hanoi(num-1,third,dst,src)

hanoi(5,"X","Y","Z")
