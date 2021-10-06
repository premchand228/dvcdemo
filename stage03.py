with open("Artifacts01.txt","r") as f:
    text=f.read()
    print(text)
    ##text=text+'adding more info'
with open("Artifacts02.txt","w+") as f:
    f.write(text+"  added new lines using stage03 ")
    print(text)
    print("end of stage3")