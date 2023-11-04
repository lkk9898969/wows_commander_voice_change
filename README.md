wows_commander_voice_change
戰艦世界修改指揮官語音小程式。
巴哈文章:https://forum.gamer.com.tw/C.php?bsn=21052&snA=19822

##### 修改user_preferences.xml語音資料，進而達成修改語音的目的。
### 檔案說明:
* lkk94.py : 透過搜尋文字檔內容，獲取語音代碼(IDS_SOUND_MOD)，產生soundmodecode.py。
* lkk95.py : 0.12.6版本以前的修改程式。修改的目標檔案為preferences.xml
* lkk106.pu : 0.12.6版本以後的修改程式。修改的目標檔案為user_preferences.xml
* Windows*.py : 各個視窗物件。使用ui to py.bat將windows*.ui檔案轉成py檔以供使用。
* icon.py 、 icon.ico : 程式圖標。 

#### 請注意自0.12.6之前，語音資料存於preferences.xml
#### 對應程式為lkk95.py
#### 自0.12.6之後，語音資料存於user_preferences.xml
#### 對應程式為lkk106.py