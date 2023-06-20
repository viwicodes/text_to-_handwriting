from PIL import Image
txt=open("dummy.txt") 
BG=Image.open("myfont/bg.png") 
sheet_width=BG.width
gap, ht = 0, 0

for i in txt.read().replace("\n",""):
    cases = Image.open("myfont/{}.png".format(str(ord(i))))
    BG.paste(cases, (gap, ht))
    size = cases.width
    height=cases.height
    gap+=size
    if sheet_width < gap or len(i)*100 >(sheet_width-gap):
        gap,ht=0,ht+140
BG.show()
