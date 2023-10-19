import tkinter as tk
from tkinter import filedialog
top = tk.Tk()
top.title("CS2自定义一键聊天CFG")
top.geometry("750x300")
file_directory = tk.StringVar()
chat_text = tk.StringVar()
keystroke = tk.StringVar()
text_to_show = tk.StringVar()
text_to_show.set('bind k "kill"')
def Gets_the_file_directory():
    file_directory.set(filedialog.askdirectory())
    print('CS2CFG文件地址为：',file_directory.get())
def Get_chat_text():
    chat_text.set(text1.get())
    print(chat_text.get())
def Get_keystroke():
    keystroke.set(keystroke_text.get())
    print(keystroke.get())
def Write_to_the_configuration_ile():
    Get_keystroke()
    Get_chat_text()
    Save_the_location = file_directory.get()
    full_path = Save_the_location+'/'+ 'YScscfg' + '.cfg'
    file = open(full_path, 'w')
    file.write('bind'+' '+keystroke.get()+' '+'say'+' '+'"'+chat_text.get()+'"'+';')
    print('导出完成')
def Instruction_display():
    text_2 =text_to_show.get()+'\n'+text_show.get()
    text_to_show.set(text_2)
    print(text_to_show.get())
def Save_all():
    Save_the_location = file_directory.get()
    full_path = Save_the_location + '/' + 'YScscfg' + '.cfg'
    file = open(full_path, 'w')
    file.write(text_to_show.get())
tk.Button(text='选择cfg文件目录',command=Gets_the_file_directory,width=20).grid(row=0,column=0)
tk.Entry(textvariable=file_directory,width=80).grid(row=0,column=1)
tk.Label(text='设置文本',width=20).grid(row=1,column=0)
text1 = tk.Entry(width=80)
text1.grid(row=1,column=1)
tk.Label(text='设置按键',width=20).grid(row=2,column=0)
keystroke_text = tk.Entry(width=80)
keystroke_text.grid(row=2,column=1)
tk.Button(text='导出配置',command=Write_to_the_configuration_ile).grid(row=3,column=0)
tk.Label(text='在用游戏中使用”exec YScscfg“来加载配置\n如果按键是单词请自己带上引号\ncfg存放位置为steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg').grid(row=5,column=1)
text_show = tk.Entry(width=80)
text_show.grid(row=6,column=1)
tk.Label(text='自定义指令').grid(row=6,column=0)
tk.Label(textvariable=text_to_show).grid(row=8,column=1)
tk.Button(text='输出',command=Instruction_display).grid(row=7,column=1)
tk.Button(text='保存',command=Save_all).grid(row=7,column=0)
top.mainloop()
