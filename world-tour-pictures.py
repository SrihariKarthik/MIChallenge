from stegano import lsb

def hide(image_path, output_path, text):
    img = lsb.hide(image_path, text)
    img.save(output_path)
    print("Success", "Successful hide the message in the image")  

listofhiddentext=[]

def show(image_path):
    img = lsb.reveal(image_path)
    listofhiddentext.append(img)
    return listofhiddentext



listofimg = ['Non Hidden Pictures/PlainPicture1.png','Non Hidden Pictures/PlainPicture2.png','Non Hidden Pictures/PlainPicture3.png','Non Hidden Pictures/PlainPicture4.png','Non Hidden Pictures/PlainPicture5.png']
listofencrypting = ['Picture1.png','Picture2.png','Picture3.png','Picture4.png','Picture5.png']
listoftext=['Painting and Fashion','Great Technology','Ancient Ruins','Culture and Heritage', 'The Silicon Valley']

for i in range(0,len(listofimg)):
    hide(listofimg[i],listofencrypting[i],listoftext[i])



for i in listofencrypting:
    show(i)

print(listofhiddentext)

from googletrans import Translator

translator = Translator()

listoftransalated=[]
listoflanf=['fr','ja','it','ms','en']
for i in range(0,len(listofhiddentext)):
    x= translator.translate(listofhiddentext[i],dest=listoflanf[i])
    print(x)
    listoftransalated.append(x.text)

print(listoftransalated)

listcode=''
for i in listoftransalated:
    listcode += i.lower()
    if i != listoftransalated[-1]:
            listcode += '_'


print(listcode)
