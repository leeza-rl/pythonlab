src = open("leeza.txt","r")
data = src.read()
src.close()

dst = open("abc.txt","w")
dst.write(data)
dst.close()
print("files copied successsfully.")