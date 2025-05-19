import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os
from datetime import datetime

# 弹窗选择文件
def choose_file():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    file_path = filedialog.askopenfilename(title="选择 Excel 文件", filetypes=[("Excel Files", "*.xlsx")])
    return file_path


# 主逻辑
def main():
    # 选择文件
    file_path = choose_file()
    if not file_path:
        print("❌ 未选择文件，程序退出")
        return

    # 读取 Excel 文件
    df = pd.read_excel(file_path)

    # 去重（根据所有列）
    df_unique = df.drop_duplicates()
    # 获取当前时间戳并格式化
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # 自动生成保存路径为当前文件夹，并命名为 "去重后的文件.xlsx"
    save_path = os.path.join(os.getcwd(), f"OK-{timestamp}.xlsx")

    # 保存去重后的文件
    df_unique.to_excel(save_path, index=False)
    print(f"✅ 去重完成，文件已保存至: {save_path}")


if __name__ == "__main__":
    main()
