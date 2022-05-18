import requests
import tkinter as tk
import tkinter.messagebox


def check():
    if entry1.get() == '输入英文单词':
        entry1.delete(0, "end")


def find():
    url = 'https://fanyi.baidu.com/sug'
    key = entry1.get()
    if key == " ":
        tkinter.messagebox.showwarning("警告！", "您没有输入单词")
        return
    dic = {
        "kw": key
    }
    resp = requests.post(url, data=dic)
    dirs = resp.json()
    resp.close()
    try:
        info = dirs['data'][0]['v']
    except:
        tkinter.messagebox.showerror("错误！", "您输入的单词有误！")
        entry1.delete(0, "end")
    else:
        # print(info)
        tkinter.messagebox.showinfo("翻译成功", info)


if __name__ == '__main__':
    window = tk.Tk()
    window.title('英文翻译小助手')
    window.config(bg='#FFC0CB')
    window.geometry('400x200')
    window.iconbitmap('H:\下载\测试点\翻译.ico')

    # 创建文本
    text = tk.Label(window, text="请输入您要翻译的英文单词", font=("华文新魏", 16, 'bold'), bg="#87CEFA",
                    width=31, height=1,
                    padx=3, pady=3, borderwidth=13, relief="flat")
    text.pack()
    # 创建动字符串
    Dy_String = tk.StringVar()

    # 创建输入框
    entry1 = tk.Entry(window, textvariable=Dy_String, validate="focusin",
                      validatecommand=check, justify='center', relief="flat", borderwidth=5)
    entry1.insert(0, "输入英文单词")
    entry1.pack(pady=20)

    # 创建翻译框
    bt = tk.Button(window, width=7, text='翻译', justify='center', bg='#FFB6C1',
                   relief="raised", borderwidth=7, command=find, font=('楷体', 15, 'bold'))
    bt.pack()
    window.mainloop()
