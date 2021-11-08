with open('text01.txt') as f:
    ##f_contents = f.read()
    ## reading file by taking fixed number of values::::
    size_to_read = 10
    #f_contents = f.read(size_to_read)
    #while len(f_contents) > 0:
        #print(f_contents, end = "*")
        #f_contents = f.read(size_to_read)

    ##if i want to print the same 10 values again:
    ##f.seek(0)

    ff_contents = f.read(size_to_read)
    print(ff_contents , end = "*")
    ff_contents = f.read(size_to_read)
    print(ff_contents, end = "*")
    ff_contents = f.read(size_to_read)
    print(ff_contents, end = "*")
    f.seek(0)
    ff_contents = f.read(size_to_read)
    print(ff_contents, end="*")
    ff_contents = f.read(size_to_read)
    print(ff_contents, end="*")

with open('text02.txt' , 'w') as f:
    f.write('this a python created text file ')
    f.seek(0)
    f.write('Ruk')


