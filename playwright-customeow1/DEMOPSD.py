# from psd_tools import PSDImage
# import os
#
# def is_valid_psd(file_path):
#     """ 校验文件是否为有效的 PSD 文件 """
#     # 检查文件扩展名
#     if not file_path.lower().endswith('.psd'):
#         return False, '文件扩展名不是 .psd'
#
#     # 尝试使用 psd-tools 打开文件
#     try:
#         psd = PSDImage.open(file_path)
#         # 返回 PSD 文件的基本信息：大小和图层数量
#         return True, f"有效 PSD 文件, 尺寸: {psd.width}x{psd.height}, 图层数: {len(psd)}"
#     except Exception as e:
#         return False, f"无法解析 PSD 文件: {str(e)}"
#
# # 示例文件路径
# file_path = r'D:\JCtestgit\Dome_project\playwright-customeow1\7_pieces.psd'
#
# # 校验文件
# valid, message = is_valid_psd(file_path)
# print(message)
from psd_tools import PSDImage

def is_valid_psd(file_path):
    """ 尝试使用 psd-tools 解析 PSD 文件 """
    try:
        psd = PSDImage.open(file_path)
        return True, f"文件是有效的 PSD 格式, 尺寸: {psd.width}x{psd.height}"
    except Exception as e:
        return False, f"文件不是有效的 PSD 文件: {str(e)}"

# 示例
valid, message = is_valid_psd(r'D:\JCtestgit\Dome_project\playwright-customeow1\7_pieces.psd')
print(message,"===========",valid)
