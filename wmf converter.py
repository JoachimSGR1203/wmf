from PIL import Image
import os, tkinter, tkinter.filedialog, tkinter.messagebox
import re

root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('画像変換プログラム','wmfファイルを選択してください')

file = tkinter.filedialog.askopenfilenames(filetypes = fTyp,initialdir = iDir)
list = list(file)

root.destroy()

for mapfile in list:
    im = Image.open(mapfile)
    path = str(os.path.dirname(mapfile))
    onlyfilename, ext = os.path.splitext(os.path.basename(mapfile))
    str_onlyfilename = str(onlyfilename)

    im.save(path + '\\'+ str_onlyfilename + '.jpg', quality=100)
