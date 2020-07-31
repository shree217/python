msg = input(">")
list = msg.split(" ")
emojis = {
    ":)":"😃",
    ":(":"😢"
}
output = ""
for i in list:
    output += emojis.get(i,i) + " "
print(output)
