# Printed Character Recognition and Translation System (印刷體文字辨識暨翻譯系統)

利用機器學習雲端平台 -Azure 完成的一個圖片印刷體文字辨識暨翻譯系統，可以英翻中、韓翻中、英翻韓
## 使用介紹

1. 在第3行程式放入您的電腦視覺資源金鑰
2. 在第4行程式碼處放入您的電腦視覺資源端點網址
3. 在第6行程式碼處放入您想要辨識的文字圖片url網址，即可做圖片印刷體文字辨識
4. 在第23行程式碼處放入您的翻譯資源金鑰
5. 在第24行程式碼處放入您的翻譯資源端點網址
6. 在第27行程式碼處放入您想翻譯的語言，即可對辨識出的文字進行翻譯

韓文圖片辨識範例

![image](https://github.com/kungyanling/Printed-character-recognition-and-translation-system/blob/main/%E6%93%B7%E5%8F%966.PNG)
 
執行範例
 
![image](https://github.com/kungyanling/Printed-character-recognition-and-translation-system/blob/main/%E6%93%B7%E5%8F%968.PNG)

英文圖片辨識範例

![image](https://github.com/kungyanling/Printed-character-recognition-and-translation-system/blob/main/%E6%93%B7%E5%8F%967.PNG)

執行範例

![image](https://github.com/kungyanling/Printed-character-recognition-and-translation-system/blob/main/%E6%93%B7%E5%8F%965.PNG)

錯誤圖片範例(空白的圖片，無文字)

![image](https://github.com/kungyanling/Printed-character-recognition-and-translation-system/blob/main/%E6%93%B7%E5%8F%963.PNG)

執行範例

![image](https://github.com/kungyanling/Printed-character-recognition-and-translation-system/blob/main/%E6%93%B7%E5%8F%969.PNG)

## 小小經驗分享

1. 要辨識的圖片需要是遠端圖片，要如何放遠端圖片呢?這裡推薦 https://imgbb.com/ 這個網站，操作簡便，還可以設置多久後刪除喔!而且登入方式多元，有Google、Facebook和Twitter
2. 用 https://imgbb.com/ 這個網站上傳的圖片網址有分圖片連結和url連結，要用url連結才能辨識喔!不然會出現錯誤訊息:" Image url is not accessible."
3. 要注意headers和params的名稱是固定的，不可在前後方加入其他字元，不然會出錯

## 我的獨到之處

核心程式碼片段

![image](https://github.com/kungyanling/Printed-character-recognition-and-translation-system/blob/main/%E6%93%B7%E5%8F%964.PNG)

1. 分析後傳回的資料是一個很長的list，裡面的資料除了我需要的文字辨識結果還有文字的位置座標等資訊，我將其分析後發現句子的數目是analysis["regions"][0]["lines"]中的項目個數，
而單字是analysis["regions"][0]["lines"][i]["words"]中的項目個數，故用len()函數將句子個數取出存於n，再用巢狀for迴圈中的len()函數將每個句子中的單字個數取出存於m，
再用for迴圈搭配list.append()函數將其連接在一起，就可以只取我要的文字片段啦! (第15-20行程式碼)
2. 由於前面連接的資料型別是list，但翻譯需要是string才能做，故我用Str = " ".join()函數將list轉為string，就可以對辨識出的結果做翻譯的動作啦! (第21行程式碼)
3. 我發現若是沒有可辨識的內容，傳回的list中analysis["regions"]=[]，故我在取文字片段前，先加了個條件判斷式，以達到防呆的作用 (第12行程式碼)
