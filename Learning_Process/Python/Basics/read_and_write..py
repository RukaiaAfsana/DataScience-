with open('text01.txt','r') as rf:
    with open('text03.txt' , 'w') as wf:
       # rf_contents = rf.read()
       # wf.write(rf_contents)
           # or
       for line in rf:
           wf.write(line)
