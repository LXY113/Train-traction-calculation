import tkinter as tk

# 创建一个函数来处理输入并显示输出
def show_output():
    # 获取输入框的内容
    parameter1 = entry1.get()
    parameter2 = entry2.get()
    
    # 这里可以添加对参数的处理逻辑
    output = f"参数1: {parameter1}, 参数2: {parameter2}"
    
    # 显示输出
    text_output.delete('1.0', tk.END)  # 清空输出框
    text_output.insert(tk.END, output)  # 插入处理后的结果

# 创建主窗口
root = tk.Tk()
root.title("参数输入与输出")

# 第一行：文本
label1 = tk.Label(root, text="输入参数1")
label1.grid(row=0, column=0)

# 第二行：输入框
entry1 = tk.Entry(root)
entry1.grid(row=1, column=0)

# 第三行：文本
label2 = tk.Label(root, text="输入参数2")
label2.grid(row=2, column=0)

# 第四行：输入框
entry2 = tk.Entry(root)
entry2.grid(row=3, column=0)

# 第五行：输出框
text_output = tk.Text(root, height=5, width=50)
text_output.grid(row=4, column=0)

# 创建一个按钮，点击时调用show_output函数
button = tk.Button(root, text="显示输出", command=show_output)
button.grid(row=5, column=0)

# 运行主循环
root.mainloop()