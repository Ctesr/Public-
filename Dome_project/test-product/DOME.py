import os
from PIL import Image, ImageDraw, ImageFont
import string  # 用于获取字母
# 创建保存图片的文件夹
output_folder = "generated_images9"
os.makedirs(output_folder, exist_ok=True)

# 图片尺寸
width, height = 11999, 11999 # 正方形图片
bg_color = (10, 5, 255)  # 浅天蓝色
margin = 20  # 边距

# 生成数字（1到1000）
# numbers = range(1, 31)
# for num in numbers:
#     num_str = str(num)
#     image = Image.new("RGB", (width, height), bg_color)
#     draw = ImageDraw.Draw(image)
#
#     # 初始字号（较大）
#     font_size = 600
#     font = None
#
# # 要生成的英文字母（大写）
# letters = list(string.ascii_uppercase)  # ['A', 'B', ..., 'Z']
letters = ["b"]
for ch in letters:
    image = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # 初始字号（较大）
    font_size = 8600
    font = None

    # 动态调整字号，确保文本不超出图片范围
    while True:
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()  # 回退到默认字体

        # 计算文本边界框
        bbox = draw.textbbox((0, 0), ch, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # 检查是否超出图片范围（考虑边距）
        if (text_width <= width - 2 * margin) and (text_height <= height - 2 * margin):
            break  # 字号合适，退出循环
        else:
            font_size -= 5  # 每次减少5px，直到合适

    # 计算完全居中位置（考虑字体基线）
    # 使用 `textlength` 和 `textsize` 更精确计算
    text_width = font.getlength(ch)
    ascent, descent = font.getmetrics()
    text_height = ascent + descent

    # 计算文本的左上角坐标（真正居中）
    x = (width - text_width) / 2
    y = (height - text_height) / 2 - descent  # 调整基线偏移

    # 绘制文本（使用锚点 "mm" 表示中心对齐）
    draw.text((width // 2, height // 2), ch, font=font, fill="black", anchor="mm")

    # 保存图片
    image_path = os.path.join(output_folder, f"day{ch}.png")
    image.save(image_path)

    # # 打印进度（每100个数字打印一次）
    # if num % 100 == 0:
    #     print(f"已生成 {num} 张图片")

print(f"所有图片生成完毕！保存路径: {os.path.abspath(output_folder)}")