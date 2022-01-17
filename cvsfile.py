import csv
import os
import re
import time
import tkinter.filedialog
from tkinter import *
import tkinter as tk
# from PIL import Image, ImageTk


class csvFile():
    def __init__(self):
        self.arr = []
        self.last_arr = []

    def selectPath(self):  # 选择文件
        self.arr = []   # 每次选择文件时初始化存储的数组
        self.last_arr = []
        path_ = tkinter.filedialog.askopenfilename()  # 打开文件
        var1.set(path_)
        if var1.get() != "" and not self.arr:
            try:
                with open(var1.get(), encoding="UTF-8-sig") as f:  # 格式解析失败时，则不指定数据格式
                    self.arr = f.read().split("\n")
                if not self.last_arr:
                    self.last_arr = self.arr
            except:
                with open(var1.get()) as f:
                    self.arr = f.read().split("\n")
                if not self.last_arr:
                    self.last_arr = self.arr
        self.browse()

    def browse(self):  # 浏览
        lb.delete('0', 'end')
        for i in self.arr:
            lb.insert(END, i)

    def find(self):  # 筛选
        lb.delete('0', 'end')
        self.last_arr = []
        if title.get() == 1:
            self.last_arr.append(self.arr[0])
        for i in self.arr:
            if re.findall(var2.get(), i):
                self.last_arr.append(i)
        for value in self.last_arr:
            lb.insert(END, value)

    def savePath(self):  # 保存
        if lb.get(0) != "":
            path_ = tkinter.filedialog.asksaveasfilename()  # 保存文件
            # 保存文件名不能为空
            if path_ != "":
                for i in self.last_arr:
                    with open(path_, "a+", newline="") as f:
                        f.write(i + "\n")

    def startInsert(self):  # 最前插入

        if var1.get() != "" and var2.get() != "":
            if title.get() == 1:  # 判断是否包含标题
                for i in range(len(self.last_arr)):
                    if i != 0:     # 跳过第一行
                        self.last_arr[i] = var2.get() + self.last_arr[i]
            else:
                for i in range(len(self.last_arr)):
                    self.last_arr[i] = var2.get() + self.last_arr[i]

            self.lbInset()


    def endInsert(self):  # 最后插入
        if var1.get() != "" and var2.get() != "":
            if title.get() == 1:
                for i in range(0, len(self.last_arr)):
                    if i != 0:   # 跳过第一行
                        self.last_arr[i] = self.last_arr[i] + var2.get()
            else:
                for i in range(0, len(self.last_arr)):
                    self.last_arr[i] = self.last_arr[i] + var2.get()

            self.lbInset()

    def string(self):  # 插入双引号
        print("arr"+str(self.last_arr))
        print("arr长度：%d"% len(self.last_arr))
        num=0
        for i in range (len(self.last_arr)):
            print(i)
        for index,value in enumerate(self.last_arr):
            print(value)
            lineList = str(value.split(","))
            print("split"+lineList)
            out1 = re.sub('[]]|[[]', "", lineList)  # 去掉[]
            newStr = re.sub("'", '"', out1)  # '改为"
            print("sub"+newStr)

            self.last_arr[index] = newStr
        #     print(num)
        #     num += 1
        #     time.sleep(2)
        self.lbInset()




    def lbInset(self):
        lb.delete('0', 'end')
        for i in self.last_arr:
            lb.insert(END, i)



    # def get_image(self,filename, width, height):
    #     im = Image.open("https://img95.699pic.com/photo/50025/3088.jpg_wh300.jpg").resize((width, height))
    #     return ImageTk.

    def secondary(self):   # 自定义插入
        global top
        top = Toplevel()
        top.title('自定义插入')
        top.geometry("300x100+400+200")
        top1 = Frame(top)
        top1.grid(row=0,column=0, padx=50)
        Label(top1, text="从第").grid(row=0, column=0, pady=10)
        global index
        index = IntVar()  # 行
        Entry(top1, textvariable=index, width=4).grid(row=0, column=1, pady=10)
        Label(top1, text="个字符开始插入").grid(row=0, column=2, pady=10)
        global value
        value = StringVar()  # 自定行的关键字
        Entry(top1, textvariable=value, width=7).grid(row=0, column=3, pady=10)
        Button(top1, text='确认', command=self.insert).grid(row=1, column=3, pady=20, ipadx=10)
        top.mainloop()

    def insert(self):  # 自定义插入需要的方法
        lb.delete('0', 'end')
        print("indextype："+str(type(index.get())),"index:"+str(index.get()))
        if title.get() == 1:
            for i in range(len(self.last_arr)):
                if i != 0:
                    print((self.last_arr[i])[:index.get()])
                    self.last_arr[i] = (self.last_arr[i])[:index.get()] + value.get() + (self.last_arr[i])[index.get():]
        else:
            for i in range(len(self.last_arr)):
                print((self.last_arr[i])[:index.get()])
                self.last_arr[i] = (self.last_arr[i])[:index.get()] + value.get() + (self.last_arr[i])[index.get():]

        for j in self.last_arr:
            lb.insert(END, j)
        top.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("440x520+400+200")
    # root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage(file="./中秋.png"))
    root.resizable(width=False, height=False)   # False窗口大小不可变
    root.title("文件处理")

    frame1 = Frame(root)
    frame1.grid(row=0, column=0)

    frame1_1 = Frame(frame1)
    frame1_1.grid(column=0, row=0)
    Label(frame1_1, text="文件路径：").grid(column=0, row=0)
    var1 = StringVar()  # 文件路劲
    var2 = StringVar()  # 关键字
    e1 = Entry(frame1, textvariable=var1, width="25")
    e1.grid(column=1, row=0, padx=2, pady=5)
    cf = csvFile()
    Button(frame1, text="路径选择", command=cf.selectPath).grid(column=2, row=0, padx=5, pady=5, ipadx=10)
    Label(frame1, text="关 键 字：").grid(column=0, row=1)
    e1 = Entry(frame1, textvariable=var2, width="25")
    e1.grid(column=1, row=1, padx=5, pady=5)
    title = IntVar()
    Checkbutton(frame1, text='是否含标题', variable=title).grid(column=2, row=1, padx=5, pady=5)  # 选择框，选中为1，不选中为0


    frame2 = Frame(root)
    frame2.grid(column=0, row=1)
    Button(frame2, text="浏览内容", command=cf.browse).grid(column=0, row=0, padx=10, pady=10, ipadx=10)
    Button(frame2, text="开始筛选", command=cf.find).grid(column=1, row=0, padx=10, pady=10, ipadx=10)
    Button(frame2, text="首行插入", command=cf.startInsert).grid(column=2, row=0, padx=10, ipadx=10)
    Button(frame2, text="尾行插入", command=cf.endInsert).grid(column=3, row=0, padx=10, ipadx=10)
    Button(frame2, text="指定插入", command=cf.secondary).grid(column=0, row=1, ipadx=10)
    Button(frame2, text="添加引号", command=cf.string).grid(column=1, row=1, ipadx=10)


    frame3 = Frame(root)
    frame3.grid(row=2, column=0)

    scX = Scrollbar(frame3, orient=HORIZONTAL)  # 水平滚动条 参数orient：HORIZONTAL水平 VERTICAL 垂直
    scX.pack(side=BOTTOM, fill=X)

    scY = Scrollbar(frame3, orient=VERTICAL)  # 垂直滚动条
    scY.pack(side=RIGHT, fill=Y)

    lb = Listbox(frame3, xscrollcommand=scX.set, yscrollcommand=scY.set, width=50, height=16)
    lb.pack(side=LEFT, fill=BOTH, expand=True, padx=18)
    scX.config(command=lb.xview)   # 滚动条滚动，列表随着滚动  xview表示x水平移动 yview垂直移动
    scY.config(command=lb.yview)

    frame4 = Frame(root)
    frame4.grid(row=3, column=0)

    Button(frame4, text="save", command=cf.savePath, activebackground="green").grid(column=0, row=0, padx=60, pady=10, ipadx=20)
    # activebackground点击时的背景颜色， activeforeground点击时字体颜色
    Button(frame4, text="close", command=root.quit, activebackground="red").grid(row=0, column=1, padx=80, pady=10, ipadx=20)
    mainloop()
