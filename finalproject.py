from pandas import *
from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests
import os

# reading CSV file
data = read_csv("frameCSV.csv")

# converting column data to list
Name = data['Name'].tolist()
Student_Id = data['Student ID'].tolist()
Upload_Your_decent_Photo = data['Upload Your decent Photo'].tolist()
img_list = []
for i in Upload_Your_decent_Photo:
    j = i[33:]
    img_list.append(j)

k = []
for h in Student_Id:
    g = 'F:/photoframe folder/pic/' + str(h) + '.png'
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


arr = os.listdir('F:/photoframe folder/pic')

picinpicfolder = []
for p in arr:
    pp = 'F:/photoframe folder/pic/' + str(p)
    picinpicfolder.append(pp)

finalpic = []
for gigi in arr:
    gii = 'F:/photoframe folder/finalpic/' + gigi[:-4] + '.png'
    finalpic.append(gii)

edited = []
for r in Student_Id:
    ss = 'F:/photoframe folder/editedpic/' + str(r) + '.png'
    edited.append(ss)

for o, p, real in zip(Name, Student_Id, edited):

    mimage = Image.open('F:/photoframe folder/template.png')

    font_type = ImageFont.truetype("arial.ttf", 70, encoding="unic")
    font_type1 = ImageFont.truetype("arial.ttf", 70, encoding="unic")
    text1 = o
    w, h = font_type.getsize(text1)
    draw = ImageDraw.Draw(mimage)
    roll = str(p)
    draw.text(xy=((1000 - w) / 2, 800), text=text1, fill=(255, 69, 0), font=font_type)
    draw.text(xy=(350, 900), text=roll, fill=(255, 69, 0), font=font_type1)

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
            kkk = 'F:/photoframe folder/pic/{}.png'.format(str(li))
            fff = 'F:/photoframe folder/editedpic/{}.png'.format(str(my))
            mmm = 'F:/photoframe folder/finalpic/{}.png'.format(str(li))
            secmain = Image.open(kkk)
            image = Image.open(fff)
            secmain = secmain.resize((600, 600))
            bigsize = (secmain.size[0] * 3, secmain.size[1] * 3)
            mask = Image.new('L', bigsize, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + bigsize, fill=255)
            mask = mask.resize(secmain.size, Image.ANTIALIAS)
            secmain.putalpha(mask)

            output = ImageOps.fit(secmain, mask.size, centering=(0, 0))
            output.putalpha(mask)

            image.paste(secmain, (190, 170), secmain)
            image.save(mmm)
