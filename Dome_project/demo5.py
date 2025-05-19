import pandas as pd

# 设置pandas显示选项（显示所有行和列）
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

try:
    # 读取Excel文件（修改为你的文件路径）
    file_path = r"D:\JCtestgit\Dome_project\工作簿1.xlsx"
    df = pd.read_excel(file_path)

    # 打印表格内容
    print("表格内容：")
    print(df)

except FileNotFoundError:
    print(f"错误：文件 {file_path} 未找到！")
except Exception as e:
    print(f"发生错误：{str(e)}")



# # 使用示例
# excel_to_json(
#     file_path=,
#     output_path=r"D:\JCtestgit\Dome_project\t1.json",
#     orient='records'  # 可选参数：records, index, columns, values等
# )