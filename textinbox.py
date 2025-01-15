#Print input in box of +

def heading(title, padding=0):
    topline = "\u250F"+ "\u2501"* len(title) + "\u2513"
    textline = "\u2503" +title+"\u2503"
    bottomline = "\u2517"+ "\u2501"* len(title) + "\u251B"
    return topline+"\n" + textline +"\n"+bottomline

inp = input("Insert String Here:\n")
print(heading(inp)+"\n")



