with open("Hello.txt","a") as file:
    li = ["Hello world","Python Practice"]
    file.writelines(s + '\n' for s in li)

with open("Hello.txt","r") as file:
    print(file.read())