# 导入模块
import psutil
import tkinter as tk
import tkinter.ttk as ttk

# 创建一个窗口
window = tk.Tk()
window.title("Windows Task Manager")
window.geometry("600x400")

# 创建一个表格
tree = ttk.Treeview(window, columns=["Name", "PID", "Status", "Memory", "CPU"])
tree.heading("#0", text="Name")
tree.heading("#1", text="PID")
tree.heading("#2", text="Status")
tree.heading("#3", text="Memory")
tree.heading("#4", text="CPU")
tree.column("#0", width=200)
tree.column("#1", width=50)
tree.column("#2", width=100)
tree.column("#3", width=100)
tree.column("#4", width=100)
tree.pack(fill=tk.BOTH, expand=True)

# 获取系统的进程信息
processes = psutil.process_iter(["name", "pid", "status", "memory_percent", "cpu_percent"])

# 将进程信息插入到表格中
for p in processes:
    name = p.info["name"]
    pid = p.info["pid"]
    status = p.info["status"]
    memory = f"{p.info['memory_percent']:.2f}%"
    cpu = f"{p.info['cpu_percent']:.2f}%"
    tree.insert("", "end", values=[name, pid, status, memory, cpu])

# 运行窗口
window.mainloop()
