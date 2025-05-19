from fontTools.ttLib import TTFont


def compress_font(input_file, output_file):
    # 打开字体文件
    font = TTFont(input_file)

    # 只保存为紧凑格式以进行压缩
    font.flavor = "woff2"  # 将字体保存为 WOFF2 格式以实现高效压缩

    # 保存压缩后的字体文件
    font.save(output_file)
    print(f"字体文件已压缩并保存为: {output_file}")


# 使用示例
 # 替换为你的字体文件路径
input_font_path = "D:\\JCtestgit\\Dome1\\NotoColorEmojiSVG-Regular.woff2"
output_font_path = "output_compressed.woff2"
compress_font(input_font_path, output_font_path)
