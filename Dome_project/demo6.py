import pandas as pd


def read_excel_tags(file_path, sheet_name=0, subset=None, keep='first', output_path=None):
    try:
        # 读取Excel文件
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # 根据指定列去重
        df_unique = df.drop_duplicates(subset=subset, keep=keep)

        # 去除字符串中的 \t
        df_unique = df_unique.applymap(lambda x: x.replace('\t', '') if isinstance(x, str) else x)

        # 打印去重后的数据行数
        print(f"去重后数据行数: {len(df_unique)}")

        # 提取每行最后一个值
        result = []
        for index, row in df_unique.iterrows():
            last_value = str(row.iloc[-1]).replace('\t', '')  # 获取每行的最后一个值并去除 \t
            result.append(last_value)

        # 如果需要保存到新的 Excel 文件
        if output_path:
            # 将结果转换为 DataFrame
            result_df = pd.DataFrame(result, columns=["Extracted_Value"])
            # 保存到 Excel 文件
            result_df.to_excel(output_path, index=False)
            print(f"结果已保存到: {output_path}")

        return result

    except FileNotFoundError:
        print(f"错误：文件 {file_path} 未找到！")
    except Exception as e:
        print(f"发生错误：{str(e)}")


# 文件路径
file_path = r"D:\JCtestgit\Dome_project\handle.xls"
# 输出文件路径
output_path = r"D:\JCtestgit\Dome_project\output.xlsx"

# 调用函数并保存结果
ids = read_excel_tags(file_path, output_path=output_path)
print(f"读取到的ID列表: {ids}")