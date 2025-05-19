import pandas as pd


def read_excel_tags(file_path, sheet_name=0, column_name="Handle", output_path=None):
    try:
        # 读取Excel文件
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # 检查是否存在 'handle' 列
        if column_name not in df.columns:
            print(f"错误：文件中未找到 '{column_name}' 列！")
            return

        # 提取 'handle' 列
        handle_data = df[column_name].drop_duplicates().tolist()

        # 去除字符串中的 \t
        handle_data = [str(value).replace('\t', '') for value in handle_data]

        # 打印提取后的数据
        print(f"提取的 'handle' 列数据: {handle_data}")

        # 如果需要保存到新的 Excel 文件
        if output_path:
            # 将提取结果保存到 Excel 文件
            result_df = pd.DataFrame(handle_data, columns=[column_name])
            result_df.to_excel(output_path, index=False)
            print(f"结果已保存到: {output_path}")

        return handle_data

    except FileNotFoundError:
        print(f"错误：文件 {file_path} 未找到！")
    except Exception as e:
        print(f"发生错误：{str(e)}")


# 文件路径
file_path = r"D:\JCtestgit\Dome_project\handles.xlsx"
# 输出文件路径
output_path = r"D:\JCtestgit\Dome_project\output.xlsx"

# 调用函数并保存结果
handles = read_excel_tags(file_path, output_path=output_path)
print(f"读取到的 'handle' 数据: {handles}")
