
import sqlite3, qrcode
import tkinter as tk 
from tkinter import ttk
import os, pdfkit, win32print, win32api
from tkinter import filedialog
from pathlib import Path
from qrCode import start

path = r"C:\Program Files\wkhtmltopdf\bin"
os.environ["PATH"] += os.pathsep + path
BASE_DIR = Path(__file__).resolve().parent

GHOSTSCRIPT_PATH = BASE_DIR / "GHOSTSCRIPT/bin/gswin64.exe"
GSPRINT_PATH = BASE_DIR /"Ghostgum/gsview/gsprint.exe"
GHOSTSCRIPT_PATH = str(GHOSTSCRIPT_PATH).replace("/",'\\')
GSPRINT_PATH = str(GSPRINT_PATH).replace("/", '\\')
print(GHOSTSCRIPT_PATH)

os.environ.update()

table_data = """

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="generator" content="RocketCake">
	<title></title>
</head>
<body style="background-color:#FFFFFF; padding-top:20px;  margin: 0;">
<div style="text-align:center;">
  <table id="table_11b4f6cd" cellpadding="3" cellspacing="1"  style="box-sizing: border-box; vertical-align: bottom; position:relative; display: inline-table; width:50%; height:240px; background:none; border: 1px solid #8C8C8C; table-layout: fixed; ">
	<tr>
		<td width="29%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div style="" id="cell_10e32479">
      <div style="text-align:center;">
        <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; font-weight:bold; ">ID</span>
        </div>
      </div>
		</td>
		<td width="70%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div style="" id="cell_4915d68c">
      <div style="text-align:left;">
        <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; ">{id}</span>
        </div>
      </div>
		</td>
	</tr>
	<tr>
		<td width="29%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div style="" id="cell_23932c22">
      <div style="text-align:center;">
        <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; font-weight:bold; ">الاسم</span>
        </div>
      </div>
		</td>
		<td width="70%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div style="" id="cell_3dae042d">
      <div style="text-align:left;">
        <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; ">{name}</span>
        </div>
      </div>
		</td>
	</tr>
	<tr>
		<td width="29%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div style="" id="cell_30ba40bc">
      <div style="text-align:center;">
        <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; font-weight:bold; ">المرحلة</span>
        </div>
      </div>
		</td>
		<td width="70%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div style="" id="cell_65b495a2">
      <div style="text-align:left;">
        <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; ">{level}</span>
        </div>
      </div>
		</td>
	</tr>
	<tr>
		<td width="29%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div style="" id="cell_64f37254">
      <div style="text-align:center;">
        <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; font-weight:bold; ">المواليد</span>
        </div>
      </div>
		</td>
		<td width="70%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div style="" id="cell_7912be8c">
      <div style="text-align:left;">
        <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; ">{born}</span>
        </div>
      </div>
		</td>
	</tr>
	<tr>
		<td width="29%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div style="" id="cell_780a4201">
      <div style="text-align:center;">
        <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; font-weight:bold; ">السكن الحالي</span>
        </div>
      </div>
		</td>
		<td width="70%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div style="" id="cell_3f14847d">
      <div style="text-align:left;">
        <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; ">{city}</span>
        </div>
      </div>
		</td>
	</tr>
	<tr>
		<td width="29%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div style="" id="cell_499f9dd1">
      <div style="text-align:center;">
        <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; font-weight:bold; ">رقم ولي الامر</span>
        </div>
      </div>
		</td>
		<td width="70%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div style="" id="cell_2fe25639">
      <div style="text-align:left;">
        <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; ">{number}</span>
        </div>
      </div>
		</td>
	</tr>
	<tr>
		<td width="29%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div style="" id="cell_552b321a">
      <div style="text-align:center;">
        <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; font-weight:bold; ">فصيله الدم</span>
        </div>
      </div>
		</td>
		<td width="70%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div style="" id="cell_567eab73">
      <div style="text-align:left;">
        <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; ">{blod}</span>
        </div>
      </div>
		</td>
	</tr>
	<tr>
		<td width="29%" height="18px" style="vertical-align: top; overflow:hidden; ">    <div style="" id="cell_1ef4dcbd">
      <div style="text-align:center;">
        <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; font-weight:bold; ">ملاحظات مهمة</span>
        </div>
      </div>
		</td>
		<td width="70%" height="18px" style="vertical-align: top; overflow:hidden; ">    <div style="" id="cell_21c46e0d">
      <div style="text-align:left;">
        <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; ">{note}</span>
        </div>
      </div>
		</td>
	</tr>
    </table>
  </div>
</body>
</html>

"""



connection = sqlite3.connect("data.sqlite")
cur = connection.cursor()

createLevelTabelCommand = """CREATE TABLE IF NOT EXISTS levels(level_id INTEGER PRIMARY KEY autoincrement, name text)"""

createAccountTabelCommand = """CREATE TABLE IF NOT EXISTS account(user_id INTEGER PRIMARY KEY autoincrement, name text, level_id integer, born_date text, city_now text, phone_number text, blod_type text, note text, FOREIGN KEY(level_id) REFERENCES levels(level_id))"""

cur.execute(createLevelTabelCommand)
cur.execute(createAccountTabelCommand)

def insertToLevels(levels):
    cur.execute(f"""INSERT INTO levels VALUES(NULL, '{levels}')""")
    connection.commit()

def insertToAccount(name, level_id, born_date, city_now, phone_number, blod_type, note):
    cur.execute(f"""INSERT INTO account VALUES(NULL, '{name}', '{level_id}', '{born_date}', '{city_now}', '{phone_number}', '{blod_type}', '{note}')""")
    connection.commit()
    
#insertToAccount("سيسيسششششششششششششششششششيسي", '3', "born_date", "القامشلي", "0988603800", "A+", "مسي سي سي  س سي  س س ي")

#cur.execute("""SELECT * FROM levels""")
#cur.execute("""DELETE FROM account""")
#connection.commit()
def getAllLevels():
    return cur.execute("""SELECT * FROM levels""").fetchall()

def getAllData():
    return cur.execute("""SELECT * FROM account""").fetchall()
#print(cur.fetchall())
#connection.close()

def delete(user_id, secoundFrame, myCanvas, mainFrame, myScrolBar):
    print(user_id)
    cur.execute(f"""DELETE FROM account WHERE user_id={user_id}""")
    connection.commit()
    secoundFrame.destroy()
    myCanvas.destroy()
    mainFrame.destroy()
    myScrolBar.destroy()
    reloadPage(False)

def DeleteLevel(level_id):
    cur.execute(f"""DELETE FROM levels WHERE level_id={level_id}""")
    connection.commit()

def getUserData(user_id):
    accuonts = cur.execute(f"""SELECT FROM account WHERE user_id={user_id}""")


root = tk.Tk()
root.geometry("800x600")


def EditAccount(user_id, secoundFrame, myCanvas, mainFrame, myScrolBar, levelsItem):
    userData=cur.execute(f"""SELECT * FROM account WHERE user_id={user_id}""").fetchall()
    userData = userData[0]
    options = []
    for id, name in levelsItem.items():
        options.append(name)

    clicked = tk.StringVar()
    try:
        clicked.set(levelsItem[userData[2]])
    except:
        clicked.set("غير معروف")
    
    print(userData)
    newWindow = tk.Toplevel(root)
    newWindow.geometry("400x400")
    tk.Label(newWindow, text ="تعديل البيانات").grid(column=1,columnspan=2)
    
    user_label = tk.Label(newWindow, text="الاسم:", pady=5).grid(row=1, column=0)
    user_ent = tk.Entry(newWindow, width=40)
    user_ent.insert(0 ,userData[1])
    user_ent.grid(row=1, column=1)
    
    level_label = tk.Label(newWindow, text="المرحلة:", pady=5).grid(row=2, column=0)
    level_ent = tk.OptionMenu(newWindow, clicked, *options)
    
    level_ent.grid(row=2, column=1)
    
    born_label = tk.Label(newWindow, text="المواليد:", pady=5).grid(row=3, column=0)
    born_ent = tk.Entry(newWindow, width=40)
    born_ent.insert(0 ,userData[3])
    born_ent.grid(row=3, column=1)
    
    num_label = tk.Label(newWindow, text="رقم ولي الامر:", pady=5).grid(row=4, column=0)
    num_ent = tk.Entry(newWindow, width=40)
    num_ent.insert(0 ,userData[4])
    num_ent.grid(row=4, column=1)

    city_label = tk.Label(newWindow, text="السكن الحالي:", pady=5).grid(row=5, column=0)
    city_ent = tk.Entry(newWindow, width=40)
    city_ent.insert(0 ,userData[5])
    city_ent.grid(row=5, column=1)
    
    blod_label = tk.Label(newWindow, text="فصيلة الدم:", pady=5).grid(row=6, column=0)
    blod_ent = tk.Entry(newWindow, width=40)
    blod_ent.insert(0 ,userData[6])
    blod_ent.grid(row=6, column=1)
    
    note_label = tk.Label(newWindow, text="ملاحضات مهمة:", pady=5).grid(row=7, column=0)
    note_ent = tk.Text(newWindow, width=30, height=5)
    note_ent.insert('1.0' ,userData[7])
    note_ent.grid(row=7, column=1)
    
    def update():
        
        for key, value in levelsItem.items():
         if clicked.get() == value:
            level_ent = key
        
        cur.execute(f''' UPDATE account SET name ='{user_ent.get()}', level_id={level_ent}, born_date='{born_ent.get()}', city_now='{city_ent.get()}', phone_number='{num_ent.get()}', blod_type='{blod_ent.get()}', note='{note_ent.get("1.0",tk.END)}' WHERE user_id = {int(user_id)}''')
        connection.commit()
        secoundFrame.destroy()
        myCanvas.destroy()
        mainFrame.destroy()
        myScrolBar.destroy()
        newWindow.destroy()
        reloadPage(False)
        
    def printData():

        data =table_data.format(id=user_id, name=user_ent.get(), level=clicked.get(), born=born_ent.get(), city=city_ent.get(), number=num_ent.get(), blod=blod_ent.get(), note=note_ent.get("1.0",tk.END))
        pdfkit.from_string(data,'Data.pdf')
        files = [('PDF FILE ', '*.pdf')]
        file_path = filedialog.asksaveasfile(mode="wb" ,filetypes = files, defaultextension = files)
        pdf_file = open('Data.pdf', 'rb').read()
        file_path.write(pdf_file)
  
        currentprinter = win32print.GetDefaultPrinter()
        win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "Data.pdf"', '.', 0)

    def createQrCode():
      data = f"{userData[1]}, {userData[2]}, {userData[3]}, {userData[4]}, {userData[5]}, {userData[6]}, {userData[7]}".encode().hex()
      print(data)
      QR_Data = qrcode.make(data).save("QR_Data.png")
      files = [('PNG FILE ', '*.png')]
      file_path = filedialog.asksaveasfile(mode="wb" ,filetypes = files, defaultextension = files)
      pdf_file = open('QR_Data.png', 'rb').read()
      file_path.write(pdf_file)


    save_btn = tk.Button(newWindow, text="حفظ", command=update, padx=10)
    save_btn.grid(column=1,columnspan=2, pady=10)
    
    print_btn = tk.Button(newWindow, text="طباعة", command=printData, padx=10)
    print_btn.grid(column=1,columnspan=2, pady=10)
    
    print_btn = tk.Button(newWindow, text="QrCode استخراج", command=createQrCode, padx=10)
    print_btn.grid(column=1,columnspan=2, pady=10)
      
      
      
        
def addNewLevel(secoundFrame, myCanvas, mainFrame, myScrolBar, levelsItem):
    
    newWindow = tk.Toplevel(root)
    newWindow.geometry("400x350")
    tk.Label(newWindow, text ="اضافة مرحلة").grid(column=1,columnspan=2)
    
    
    options = []
    first_level = ""
    for id, name in levelsItem.items():
        first_level = name
        options.append(name)
    
    clicked = tk.StringVar()
    clicked.set(first_level)
    
    level_label = tk.Label(newWindow, text="المرحلة: ", pady=5).grid(row=1, column=0)
    level_ent = tk.Entry(newWindow, width=40)
    level_ent.grid(row=2, column=1)

    
    def update():
        insertToLevels(level_ent.get())
        secoundFrame.destroy()
        myCanvas.destroy()
        mainFrame.destroy()
        myScrolBar.destroy()
        newWindow.destroy()
        reloadPage(False)

    def deleteLevel(levelsItem):
        
        for key, value in levelsItem.items():
         if clicked.get() == value:
            DeleteLevel(key) 
            
        secoundFrame.destroy()
        myCanvas.destroy()
        mainFrame.destroy()
        myScrolBar.destroy()
        newWindow.destroy()
        reloadPage(True)
        
    save_btn = tk.Button(newWindow, text="حفظ", command=lambda: update(), padx=10)
    save_btn.grid(column=1,columnspan=2, pady=10)
    
    
    
    tk.Label(newWindow, text ="حذف مرحلة").grid(row=4, column=1,columnspan=2, pady=(30,0))
    
    
    level_del_ent = tk.OptionMenu(newWindow, clicked, *options)
    level_del_ent.grid(row=6, column=1)
    
    delete_btn = tk.Button(newWindow, text="حذف", padx=10, command=lambda: deleteLevel(levelsItem))
    delete_btn.grid(column=1,columnspan=2, pady=10)





def addNewUser(secoundFrame, myCanvas, mainFrame, myScrolBar, levelsItem , is_from_qrcode=False):
    

    options = []
    first_level = ""
    for id, name in levelsItem.items():
        first_level = name
        options.append(name)

    clicked = tk.StringVar()
    clicked.set(first_level)
    
    
    newWindow = tk.Toplevel(root)
    newWindow.geometry("400x350")
    tk.Label(newWindow, text ="اضافة مستخدم جديد").grid(column=1,columnspan=2)
    
    user_label = tk.Label(newWindow, text="الاسم:", pady=5).grid(row=1, column=0)
    user_ent = tk.Entry(newWindow, width=40)
    user_ent.grid(row=1, column=1)
    
    level_label = tk.Label(newWindow, text="المرحلة:", pady=5).grid(row=2, column=0)
    level_ent = tk.OptionMenu(newWindow, clicked, *options)
    
    level_ent.grid(row=2, column=1)
    
    born_label = tk.Label(newWindow, text="المواليد:", pady=5).grid(row=3, column=0)
    born_ent = tk.Entry(newWindow, width=40)
    born_ent.grid(row=3, column=1)
    
    num_label = tk.Label(newWindow, text="رقم ولي الامر:", pady=5).grid(row=4, column=0)
    num_ent = tk.Entry(newWindow, width=40)
    num_ent.grid(row=4, column=1)

    city_label = tk.Label(newWindow, text="السكن الحالي:", pady=5).grid(row=5, column=0)
    city_ent = tk.Entry(newWindow, width=40)
    city_ent.grid(row=5, column=1)
    
    blod_label = tk.Label(newWindow, text="فصيلة الدم:", pady=5).grid(row=6, column=0)
    blod_ent = tk.Entry(newWindow, width=40)
    blod_ent.grid(row=6, column=1)
    
    note_label = tk.Label(newWindow, text="ملاحضات مهمة:", pady=5).grid(row=7, column=0)
    note_ent = tk.Text(newWindow, width=30, height=5)
    note_ent.grid(row=7, column=1)
    
    def update():
        
        for key, value in levelsItem.items():
         if clicked.get() == value:
            level_ent = key
        
        cur.execute(f''' INSERT INTO account VALUES(NULL, '{user_ent.get()}', {level_ent}, '{born_ent.get()}', '{city_ent.get()}', '{num_ent.get()}', '{blod_ent.get()}', '{note_ent.get("1.0",tk.END)}')''')
        connection.commit()
        secoundFrame.destroy()
        myCanvas.destroy()
        mainFrame.destroy()
        myScrolBar.destroy()
        newWindow.destroy()
        reloadPage(False)
        
    if is_from_qrcode:
      QR_Data = start()
      QR_Data = bytes.fromhex(QR_Data)
      QR_Data = QR_Data.decode()
      QR_Data = QR_Data.split(',')
      print(QR_Data)
      user_ent.insert(0, QR_Data[0])
      clicked.set(levelsItem[int(QR_Data[1])])
      born_ent.insert(0, QR_Data[2])
      num_ent.insert(0, QR_Data[3])
      city_ent.insert(0, QR_Data[4])
      blod_ent.insert(0, QR_Data[5])
      note_ent.insert('1.0', QR_Data[6])
      
    save_btn = tk.Button(newWindow, text="حفظ", command=update, padx=10)
    save_btn.grid(column=1,columnspan=2, pady=10)


def reloadPage(open_level):
        
    mainFrame = tk.Frame(root)
    mainFrame.pack(fill=tk.BOTH, expand=1)

    myCanvas = tk.Canvas(mainFrame)
    myCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    myScrolBar = ttk.Scrollbar(mainFrame, orient=tk.VERTICAL, command=myCanvas.yview)
    myScrolBar.pack(side=tk.RIGHT, fill=tk.Y)
    myCanvas.configure(yscrollcommand=myScrolBar.set)
    myCanvas.bind("<Configure>", lambda e:myCanvas.configure(scrollregion=myCanvas.bbox("all")))

    secoundFrame = tk.Frame(myCanvas)
    myCanvas.create_window((0,0), window=secoundFrame, anchor="nw")


    levelsItem = {}

    for levelItem in getAllLevels():
        levelsItem[levelItem[0]] = levelItem[1]
        
    if open_level:
        addNewLevel(secoundFrame, myCanvas, mainFrame, myScrolBar, levelsItem)
        

    add_button = tk.Button(secoundFrame, text="اضافة مستخدمين", command=lambda: addNewUser(secoundFrame, myCanvas, mainFrame, myScrolBar, levelsItem), width=20).pack(fill='y',padx=5, pady=2)
    add_button = tk.Button(secoundFrame, text="اضافة مراحل", width=20, command=lambda: addNewLevel(secoundFrame, myCanvas, mainFrame, myScrolBar, levelsItem)).pack(fill='y',padx=5, pady=2)
    add_button = tk.Button(secoundFrame, text="QR Code", command=lambda: addNewUser(secoundFrame, myCanvas, mainFrame, myScrolBar, levelsItem, True), width=20).pack(fill='y',padx=5, pady=2)
    #add_button = tk.Button(secoundFrame, text="بحث حسب الايدي", width=20, command=lambda: addNewLevel(secoundFrame, myCanvas, mainFrame, myScrolBar, levelsItem)).pack(fill='y',padx=5, pady=2)
    button_dict = {}
    button_dict2 = {}
    namesList = ['الاسم', 'المرحلة', 'المواليد', 'رقم ولي الامر', 'السكن الحالي', 'فصيلة الدم', 'ملاحضات مهمة']
    accuonts =getAllData()



    frame = tk.LabelFrame(secoundFrame, text = "")
    frame.pack(anchor='w',fill='both')
    tk.Label(frame, text="", width=14).grid(row=0, column=0)
    tk.Label(frame, text="ID", width=14).grid(row=0, column=1)
    for names in namesList:
        namesIndex = namesList.index(names) + 2
        tk.Label(frame, text=names, width=10).grid(row=0, column=namesIndex)
        
        
    for account in accuonts:
        def action(x=account[0]): 
            return delete(x, secoundFrame, myCanvas, mainFrame, myScrolBar,)
        
        def action2(x=account[0]): 
            return EditAccount(x, secoundFrame, myCanvas, mainFrame, myScrolBar, levelsItem)
        
        i = 2
        loop = 0
        
        frame = tk.LabelFrame(secoundFrame, text = "")
        frame.pack(anchor='w',fill='both')

            
        button_dict2[account[0]] = tk.Button(frame, text="تعديل", command=action2).grid(ipadx=10,row=1, column=1)
        button_dict[account[0]] = tk.Button(frame, text="حذف", command=action).grid(ipadx=10,row=1, column=0)

        for items in account:
            if loop == 2:
                try:
                    items = levelsItem[items]
                except:
                    items = "غير معروف"
                label = tk.Label(frame, text=(str(items))[0:10], width=9, font=('Times 10')).grid(row=1 ,column=i, padx=5,)
            else:
                label = tk.Label(frame, text=(str(items))[0:10], width=9, font=('Times 10')).grid(row=1 ,column=i, padx=5,)
            i +=1
            loop +=1
reloadPage(False)
root.mainloop()