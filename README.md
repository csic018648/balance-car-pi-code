Raspberry pi 4 平衡車

 

● 材料清單：
品項	個數	品項	個數
raspberry pi 4	1*	WS2812燈條	1*
散熱鋁殼組	1	電池	1
記憶卡	1*	JY-901傳感器	1*
USB Camera	1*	觸摸開關	1*
DFR0592馬達驅動板	1*	DC-SW-pi電源線+開關	1*
驅動板架高排針	1*	13pin杜邦線	1
30F編碼器馬達	2*	束帶	15*
編碼器馬達連接線	2*	樹梅派魔鬼沾綁帶	2*
輪子	2*	泡棉膠	3*
輪子連軸器+螺絲	2*	M3銅柱3cm	4*
馬達支架	2*	M3銅柱螺絲0.8cm	8*
馬達固定螺絲	12*	M2螺絲1cm	2*
支架固定螺絲+螺帽	8*	M2螺帽	4*
金屬底盤	1*	鍵盤滑鼠	1*
壓克力頂板	1	讀卡機	1*
10吋螢幕+支架組	1*	Type-C 電源線	1*
HDMI to micro HDMI線	1*	Micro USB數據線	1*
Micro USB電源線	1*		
 
 
● 電路腳位對應表：

Part 1	Part 2
DFR0592
馬達控制板	對應接點	Raspberry pi 4
GPIO	感測器及模組
E1+	編碼器VCC (馬達1)	3.3V PWR	JY-901 VCC
E1-	編碼器GND(馬達1)	GPIO3	JY-901 SCL
E1A	編碼器A相(馬達1)	GPIO2	JY-901 SDA
E1B	編碼器B相(馬達1)	GND	JY-901 GND
M1+	電機線M+(馬達1)		
M1-	電機線M-(馬達1)	GPIO23	觸摸開關 OUT1
		GND	觸摸開關 GND
E2+	編碼器VCC (馬達2)	3.3V PWR	觸摸開關 VCC
E2-	編碼器GND(馬達2)		
E2A	編碼器A相(馬達2)	GND	WS2812 GND
E2B	編碼器B相(馬達2)	5V PWR	WS2812 VCC
M2+	電機線M+(馬達2)	GPIO18	WS2812 IND
M2-	電機線M-(馬達2)		
		5V PWR	散熱風扇 紅線
+ (7-12VCC)	12.6V電池正電源	GND	散熱風扇 黑線
- (GND)	12.6V電池負電源		

 
圖片來源：https://docs.microsoft.com/en-us/windows/iot-core/learn-about-hardware/pinmappings/pinmappingsrp
 
● 組裝說明：
 
組裝車底盤

 
固定馬達支架 (使用M3平頭螺絲 8mm螺牙長度)

 
固定馬達 (使用M3螺絲 4mm螺牙長度)

 
 
將馬達固定於支架上

 
組裝輪子

 
裝上連軸器(向內推到底鎖緊並確認連軸器與馬達有些微縫隙預防軸心卡死)
 
 
將輪子與聯軸器鎖緊 (螺絲下須墊隨附之墊片)

 
安裝上蓋支撐銅柱 (使用M3螺絲 8mm螺牙長度)

 
安裝好車底盤將如上圖
 
 
安裝電池

 
將束帶由一邊長孔穿至底下由另一邊長孔穿出並放上電池

 
串接另外兩條束帶加以固定電池，盡可能使電池置中固定
(可在電池底部黏貼兩小塊泡棉膠加強固定位置)

 
 
取出電源線組

 
將電源線組DC座與電池插頭相連，並用束帶整線固定好

 
將電池充電孔使用束帶固定
 
 
將電源線用束帶固定至另一端

 
九軸感測器安裝

 
注意排針焊接方向與接腳 使用VCC GND SDA SCL
(詳細接腳對應請參考 "電路腳位對應表" 部分)

 
   
裁切適當大小之泡棉膠黏接於感測器背面

 
此處將固定九軸感測器，為預防底盤漆面脫落而短路，
黏貼一塊透明膠帶於此區塊作絕緣。

 
貼上九軸感測器，並接上4pin杜邦線
(九軸感測器位置相當重要，盡可能與輪軸方向垂直效果最好)
 
 
頂蓋及周邊安裝

 
將觸摸開關鎖上螺絲與一層M2螺帽 (使用M2螺絲 10mm螺牙長度)

 
頂版由上方蓋住觸摸開關，並用M2螺帽鎖緊固定
(頂板正反面也需注意)
 
 
對上車體，將電源開關線由缺口處滑入

 
押入開關固定於頂板上

 
固定頂板於銅柱上 (使用M3螺絲 8mm螺牙長度)

 
 
將馬達控制線接上，並由長孔穿至上層

 
取出樹梅派金屬散熱器上蓋，並將散熱貼片貼置定位

 
放上風扇，用螺絲固定於上蓋散熱槽內，將上蓋蓋於樹梅派上
 
 
將底蓋夾入魔鬼沾並預留出上圖長度方便後續固定， 
將隨附之螺絲固定整體，並綁緊於頂板上方，不可過於搖晃。

 
取出馬達控制板將左右輪依序接上
(詳細接腳對應請參考 "電路腳位對應表" 部分)

 
將增高座接至馬達驅動板 (後方空四格插槽不接)
 
 
將整體擴展板接至樹梅派GPIO接腳上 (後方空四個接腳不接)

 
觸摸開關接線 使用到OUT1 VCC GND
(詳細接腳對應請參考 "電路腳位對應表" 部分)
 
 
將所有線經過頂蓋溝槽並使用樹帶纏繞固定
(注意連接馬達驅動板的線是否過於緊繃，以不拉扯線為原則)


 
做此步驟時請確認電源開關為關閉狀態。
將電源線頭穿過頂板接至馬達驅動板
!!!!!!! 注意正負極性，反接將燒壞主板!!!!!!! 

 
● Raspbian-buster映像檔安裝：
(電腦系統需求：windows或Mac)
	至下列網址點擊Download下載Raspberry Pi OS：
	https://www.raspberrypi.org/software/operating-systems/
 

	至下列網址下載balenaEtcher：
https://www.balena.io/etcher/
 

	接下來，將要燒錄的micro SD卡插入電腦，開啟balenaEtcher 選擇剛下載好的Raspberry Pi OS (zip檔)
 

 
	選擇要燒錄的micro SD卡位置，若自動選擇的燒錄位置不正確請修改
 

	點擊flash進行燒錄，燒錄過程請勿拔出SD卡
 

	出現成功燒錄後即可取出SD卡，並將SD卡插入Raspberry pi開機
 
 
● 首次開機相關設定：
首次使用或到未知網域時，須先將Raspberry pi 4透過micro HDMI to HDMI線連接到螢幕，並接上滑鼠鍵盤。設定wifi連接，並開啟VNC功能。

	將平衡車電源開啟，待螢幕出現桌面，點擊右上角網路圖示選擇要連接的wifi名稱，並輸入密碼。
 

 

	待連接成功後，圖示將為藍色wifi圖示，此時將滑鼠移至此wifi圖示上不點選圖示過2秒即出現當前wifi的ip address (此圖IP為: 192.168.1.139)，將此ip記錄下來，後續當平衡車連接此wifi時都將是此ip位址。
 
	點擊左上角草莓圖示 => 偏好設定 => Raspberry Pi設定
 


	到 介面 頁籤檢查設定是否與下圖相同，若不一樣請修正並點選確定。
  
	將電腦連至同個wifi網路後至下列網址點擊Download VNC Viewer下載並安裝VNC。
https://www.realvnc.com/en/connect/download/viewer/ 
 


	開啟VNC點擊左上角File => New connection。
 
 
	將之前記下的IP位址輸入到VNC Server欄位 按下OK。
 

	雙擊剛建立好的連結，即可使用遠端方式連接平衡車，後續只要平衡車和電腦都在此wifi網域時，就無須再插上螢幕鍵盤滑鼠設定這些步驟。(除非路由器重設或相似情況發生)
 

	更新系統並下載安裝顯示設定檔
sudo apt-get update

sudo apt-get dist-upgrade

sudo wget https://raw.githubusercontent.com/csic018648/Raspberry-pi-4-screen-setup/main/config.txt

sudo mv /home/pi/config.txt /boot/
 
● 平衡車程式安裝說明 (有參數調控介面)：
開啟終端機依序輸入下列指令下載平衡車相關程序
	下載安裝列表檔
wget https://raw.githubusercontent.com/csic018648/balance-car-pi-with-ctrl/main/downloadlistctrl.txt

	下載列表項目
wget -i downloadlistctrl.txt

	將校正工具設定為可執行檔並建立於桌面
sudo chmod 777 自平衡車校正工具
		mv /home/pi/自平衡車校正工具 /home/pi/Desktop

● 平衡車主程式執行與參數調整 (有參數調控介面)：
	執行主程式請在終端機輸入
python3 /home/pi/PIDbalance.pyc
		
	執行自平衡車參數校正工具
		在桌面上雙擊 "自平衡車參數校正工具" 檔案，並選擇 "執行"
   

調整好欲設定的數值後點套用即可儲存參數，此時平衡車也會立即使用此次調整參數，重新開機也將沿用上次調整之數值。
 

	建立開機後自動啟動平衡程序
wget https://raw.githubusercontent.com/csic018648/balance-car-pi-with-ctrl/main/autostart

sudo mv /home/pi/autostart /etc/xdg/lxsession/LXDE-pi/
以上能使系統在之後開機就緒後自動執行平衡車程序。
 
● 平衡車程式安裝說明 (直接修改code)：
開啟終端機依序輸入下列指令下載平衡車相關程序
	下載安裝列表檔
wget https://raw.githubusercontent.com/csic018648/balance-car-pi-code/main/downloadlistcode.txt

	下載列表檔內容
wget -i downloadlistcode.txt

● 平衡車主程式執行與參數調整(直接修改code)：
	執行主程式請在終端機輸入
python3 /home/pi/PIDbalance.py

	編輯主程式內容參數請在終端機輸入
nano /home/pi/PIDbalance.py

使用鍵盤上下鍵尋找下圖所示之 offseterror、kp、ki、kd等參數做修改，修改完成後按下CTRL+X 再按Y 儲存 並按Enter離開。
  

	建立開機後自動啟動平衡程序
wget https://raw.githubusercontent.com/csic018648/balance-car-pi-code/main/autostart

sudo mv /home/pi/autostart /etc/xdg/lxsession/LXDE-pi/
以上能使系統在之後開機就緒後自動執行平衡車程序。
 
● 操作說明：
將電源開關(A處)開啟，此時指示燈(B處)成閃爍狀態，待指示燈(B處)成恆亮狀態表示系統已就緒，輕碰一次觸摸開關(C處)主程序執行PID迴圈，平衡車開始自主平衡；再輕碰一次觸摸開關(C處)，平衡車馬達釋放扭力，停止平衡運算。

● 常見問題：
開始平衡時平衡車校正方向與傾倒方向不一致時，大多問題是兩顆馬達的線路接返，請將整組M1與整組M2的線對調，亦可將JY-901九軸感測器旋轉180度固定。
若遇到無法站立、抖動嚴重或向一邊傾倒等問題，請參考後面平衡車參數調整教學部分。


 

 
● PID調控(Tune) ：

比例控制 (Kp) 
其控制器的輸出與輸入誤差訊號成 比例關係。當比例控制是唯一的控制參數時，系統輸出將會有穩態誤差的產生（Steady-state error）。因此，以平衡車來說，過大的Kp參數將使輸出動能與反饋輸入之誤差值差異過大，進而產生校正過量的情況發生，此時平衡車將出現來回擺動最後倒下的問題。反之則會使校正量過小，無法原地站立而向某一方向偏去。


微分控制 (Kd) 
此項目為輸出與輸入誤差的微分，可以得出誤差變化率，自動穩態調整過程中有可能出現震盪產生擺幅過大的問題，通常因有慣性元件或滯後元件，使其變化量落後於誤差反饋值；加入微分項計算出下個誤差變化趨勢，以提前抑制誤差控制數值至零或反向值，改善調節過程的動態特性。


積分控制 (Ki) 
其控制器的輸出與輸入誤差訊號成 正比關係，加入積分項將誤差值對時間積分，隨著時間增加積分項也會遞增，進而推動輸出增益來抵銷Kp產生的穩態誤差，直到穩態誤差趨近於零。這使得平衡車在做偏移校正時能隨時間將誤差調整趨近於目標值，使平衡車回到穩定狀態。


統整上述三個數值之PID輸出公式：

u(k)=K_p e(k)+K_i ∑_(n=0)^k▒e(n) +K_d (e(k)-e(k-1))


● 初始平衡點校正：
在不同平面時，可能會因各種為小因素導致車身初始水平不為0，使得平衡車在無外力情況下向某方向位移，因此需調整此參數做水平校正。數值為正時平衡車向一方傾斜，為負值時向另一方傾斜，微調數值使平衡車能在自行站立情況下待在原地。

 
● 馬達最低啟動值測試：

	執行測試程式前須先關閉原本已在執行的終端機(如下圖)。

 0



左右輪各有正反兩方向之最低啟動電壓(即透過減速齒輪後軸心轉動的最大靜摩擦力)，可在桌面開啟終端機輸入sh DC_motor_demo.sh並按下Enter 即可開始測試數值。

  
此時將平衡車立於平面上並用手輕微扶著，使平衡車不至於倒下之力道即可。觀察平衡車與數值的變化，下圖可以看到當duty = 7時，左右輪開始轉動(rpm)，因此可以推斷此方向的左右輪最大靜摩擦力為duty = 6，所以校正工具裡的左輪與右輪最低啟動值(F)為6。
 
以同樣方法執行sh DC_motor_demo_back.sh測試，得出結果則填寫在左輪與右輪最低啟動值(B)欄位中。


JY-901九軸傳感器範例程式

執行程式前須如同先前測試馬達的部分，先關閉原本已在執行的終端機，開啟新終端機輸入sh jy901test.sh並按下Enter 即可執行九軸傳感器範例程式。
此時開始循環列出當前九軸之感測值，試著將傳感器傾斜不同角度，觀看數值上的變化，需結束程式請按CTRL+C停止執行。
 
 
 
WS2812燈板範例程式

下載WS2812函式庫與執行檔
	curl -L http://coreelec.io/33 | bash

sudo pip3 install rpi_ws281x

wget https://raw.githubusercontent.com/csic018648/ws2812-sh-file/main/runWS2812.sh

wget https://raw.githubusercontent.com/csic018648/ws2812-sh-file/main/strandtest.py

sudo mv /home/pi/strandtest.py /home/pi/rpi_ws281x/python/examples

開啟新終端機輸入sh runWS2812.sh並按下Enter 即可執行燈板範例程式。
 

此時燈板開始燈光變化，需結束程式請按CTRL+C停止執行。
 
 
TensorFlow視覺影像辨識
此教程預設使用者已有裝好raspbian-buster作業系統的記憶卡，將記憶卡插入樹梅派並上電開機。(詳細教程請參閱 "Raspbian-buster映像檔安裝" 部分)
	桌面就緒後，首先開器終端機將系統update。
sudo apt-get update
sudo apt-get dist-upgrade
	待安裝好更新後，開始下載TensorFlow與必要程式庫封包。
pip3 install tensorflow
sudo apt-get install libatlas-base-dev
sudo pip3 install pillow lxml jupyter matplotlib cython
sudo apt-get install python-tk
	安裝OpenCV
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install qt4-dev-tools libatlas-base-dev
sudo pip3 install opencv-python
	安裝Protobuf
sudo apt-get install protobuf-compiler
完成後可執行protoc –version，若無錯誤將得到回覆libprotoc+版本號。
	設置TensorFlow資料結構及python封包
mkdir tensorflow1
cd tensorflow1
git clone --depth 1 https://github.com/tensorflow/models.git
	編輯python封包
sudo nano ~/.bashrc
 
	在檔案尾部加入此指令
Export PYTHONPATH=$PYTHONPATH:/home/pi/tensorflow1/models/research:/home/pi/tensorflow1/models/research/slim
 
編輯好後按下CTRL+X 再按Y 儲存 並按Enter離開。

	使用Protoc編譯Object Detection API 所需之Buffer檔案。
cd /home/pi/tensorflow1/models/research
protoc object_detection/protos/*.proto --python_out=.

	接下來到object_detection資料夾準備下載model
cd /home/pi/tensorflow1/models/research/object_detection

	下載並安裝模組
wget http://download.tensorflow.org/models/object_detection/ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz
tar -xzvf ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz

	下載影像辨識主程式
wget https://raw.githubusercontent.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi/master/Object_detection_picamera.py

	下載主程式執行檔
wget https://raw.githubusercontent.com/csic018648/TensorFlow/main/runtf.sh 
將USB Camera接入樹梅派，並將電源接上。(使用TensorFlow時，建議由Type-C接入主供電，以確保足夠的供電電流，否則可能有系統不穩定或自動重啟的機率)
      


執行程式前須如同先前測試馬達的部分，先關閉原本已在執行的終端機，開啟新終端機輸入sh runtf.sh並按下Enter 即可執行TensorFlow。
 
 
TensorFlow啟動過程需等待一小段時間，若過程無誤，一陣子後將出現攝影機鏡頭畫面，此時即可開始偵測物體。
 

以手機為例，當鏡頭範圍內出現手機，TensorFlow將匡選出來並加上Tag標明cell phone和符合條件之百分比。要結束TensorFlow時請按Q鍵離開。
 
