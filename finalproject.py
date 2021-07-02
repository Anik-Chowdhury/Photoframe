'''
I create 3 folder which one is 'pic' which download images from google drive... another 'edited pic' which add roll and name in template and last folder 'final pic' where final edited (tamplate+image+name + roll) picture stored.
Note: download images from google drive only works one time because google block IP and give you corrupted image.
the code will not work if there is any corrupted image in the 'pic' folder

'''




from pandas import *
from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests
import os

# reading CSV file
data = read_csv("responseCSV.csv")

# converting column data to list
Name = data['Name'].tolist()
Student_Id = data['Student ID'].tolist()
Upload_Your_decent_Photo = data['Upload Your decent Photo'].tolist()
interest = data['Why do you want to join RMA?']
img_list = []
for i in Upload_Your_decent_Photo:
    j = i[33:]
    img_list.append(j)

k = []
for h in Student_Id:
    g = 'F:/last/pic/' + str(h) + '.png'
    k.append(g)
    
    
    
def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


if __name__ == "__main__":
    for ww, e in zip(img_list, k):
        file_id = ww
        destination = e
        download_file_from_google_drive(file_id, destination)

arr = os.listdir('F:/last/pic')

picinpicfolder = []
for p in arr:
    pp = 'F:/last/pic/' + str(p)
    picinpicfolder.append(pp)

finalpic = []
for gigi in arr:
    gii = 'F:/last/finalpic/' + gigi[:-4] + '.png'
    finalpic.append(gii)

edited = []
for r in Student_Id:
    ss = 'F:/last/editedpic/' + str(r) + '.png'
    edited.append(ss)

for o, p,inter, real in zip(Name, Student_Id, interest, edited):

    mimage = Image.open('F:/last/Template-Empty.png')

    font_type = ImageFont.truetype("arialbd.ttf", 80, encoding="unit8")
    font_type1 = ImageFont.truetype("arialbd.ttf", 80, encoding="unit8")
    font_type2 = ImageFont.truetype("arialbd.ttf", 30, encoding="unit8")
    text1 = o
    w, h = font_type.getsize(text1)
    draw = ImageDraw.Draw(mimage)
    roll = str(p)
    text2= str(inter)
    draw.text(xy=(100, 1600), text=text1,  fill=(255, 255, 255), font=font_type)
    draw.text(xy=(100, 1685), text=roll, fill=(255, 255, 255), font=font_type1)
    draw.text(xy=(100, 1800), text=text2, fill=(255, 255, 255), font=font_type2)


    mimage.save(real)

lis = []
for gig in arr:
    gi = int(gig[:-4])
    lis.append(gi)
lisi = sorted(lis)

edit = []
for r in Student_Id:
    ss = int(r)
    edit.append(ss)
editr = sorted(edit)
for li in lisi:
    for my in editr:

        if li == my:
            kkk = 'F:/last/pic/{}.png'.format(str(li))
            fff = 'F:/last/editedpic/{}.png'.format(str(my))
            mmm = 'F:/last/finalpic/{}.png'.format(str(li))
            secmain = Image.open(kkk)
            image = Image.open(fff)
            secmain = secmain.resize((1150, 1150))
            bigsize = (secmain.size[0] * 3, secmain.size[1] * 3)
            mask = Image.new('L', bigsize, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + bigsize, fill=255)
            mask = mask.resize(secmain.size, Image.ANTIALIAS)
            secmain.putalpha(mask)

            output = ImageOps.fit(secmain, mask.size, centering=(0, 0))
            output.putalpha(mask)

            image.paste(secmain, (753, 135), secmain)
            image.save(mmm)
