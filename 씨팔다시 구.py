sen=input("문장을 입력해 주세요:")


i=len(sen)-1

while i >= 0:
    if sen[i] == " ":
        print("-", end="")
    
    else:
        print("%s" % sen[i], end="")
    
    i=i-1


