path="C:\\Users\\Administrator\\Desktop\\資料夾\\戰艦文字檔\\really_selfmake_cheng\\global.po"
mod={}
# mod2={}
with open(path,"r",encoding="utf-8") as f:
    text=f.readline()
    while(text!=""):
        msgid=text
        find=msgid.find("IDS_SOUND_MOD")
        if find != -1:
            idlength=len(msgid)
            msgstr=f.readline()
            strlength=len(msgstr)
            mod.setdefault(msgstr[8:strlength-2],msgid[7:idlength-2])
            # mod2.setdefault(msgid[7:idlength-2],msgstr[8:strlength-2])
        text=f.readline()
with open("soundmodcode.py",'w',encoding='utf-8') as f:
    f.write("mod = "+str(mod).replace(",",",\n"))
    # f.write(str(mod2).replace(",",",\n"))