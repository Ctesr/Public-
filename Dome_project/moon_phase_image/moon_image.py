import os
import math
import random
from datetime import datetime, timedelta
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle

# 月相计算
def moon_phase(date: datetime) -> float:
    known_new_moon = datetime(2000, 1, 6, 18, 14)
    synodic_month = 29.53058867
    days_since_known = (date - known_new_moon).total_seconds() / 86400.0
    return (days_since_known % synodic_month) / synodic_month

# 绘制带坑洞的满月图像（透明背景）
def draw_full_moon_with_craters(phase: float, size: int = 1000) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    radius = size // 2 - 10
    center = (size // 2, size // 2)

    # 画紫色满月
    draw.ellipse([center[0]-radius, center[1]-radius, center[0]+radius, center[1]+radius], fill="purple")

    # 添加坑洞
    for _ in range(random.randint(25, 40)):
        r = random.randint(6, 18)  # 坑洞半径
        angle = random.uniform(0, 2 * math.pi)
        dist = random.uniform(0, radius - r)
        x = center[0] + dist * math.cos(angle)
        y = center[1] + dist * math.sin(angle)
        crater_color = (60, 0, 90, random.randint(160, 220))  # 深紫色、半透明
        draw.ellipse([x - r, y - r, x + r, y + r], fill=crater_color)

    # 根据月相遮罩
    offset = int(radius * 2 * (0.5 - abs(phase - 0.5)))
    mask = Image.new("L", (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)

    if phase == 0 or phase == 1:
        pass
    elif phase == 0.5:
        mask_draw.ellipse([center[0]-radius, center[1]-radius, center[0]+radius, center[1]+radius], fill=255)
    elif phase < 0.5:
        mask_draw.pieslice([center[0]-radius, center[1]-radius, center[0]+radius, center[1]+radius], 90, 270, fill=255)
        mask_draw.ellipse([center[0]-radius+offset, center[1]-radius, center[0]+radius-offset, center[1]+radius], fill=0)
    else:
        mask_draw.pieslice([center[0]-radius, center[1]-radius, center[0]+radius, center[1]+radius], 270, 90, fill=255)
        mask_draw.ellipse([center[0]-radius+offset, center[1]-radius, center[0]+radius-offset, center[1]+radius], fill=0)

    alpha = Image.new("L", (size, size), 0)
    alpha.paste(mask, (0, 0))
    img.putalpha(alpha)
    return img

# 保存 SVG
def save_svg_phase(file_name, phase, output_dir):
    fig, ax = plt.subplots(figsize=(2, 2), dpi=300)
    ax.axis("off")
    ax.add_patch(Circle((0.5, 0.5), 0.45, color="purple"))
    offset = 0.45 * 2 * (0.5 - abs(phase - 0.5))

    if phase == 0 or phase == 1:
        pass
    elif phase == 0.5:
        ax.add_patch(Circle((0.5, 0.5), 0.45, color="white"))
    elif phase < 0.5:
        ax.add_patch(Wedge((0.5, 0.5), 0.45, 90, 270, color="white"))
        ax.add_patch(Circle((0.5 - offset, 0.5), 0.45, color="purple"))
    else:
        ax.add_patch(Wedge((0.5, 0.5), 0.45, 270, 90, color="white"))
        ax.add_patch(Circle((0.5 + offset, 0.5), 0.45, color="purple"))

    plt.xlim(0, 1)
    plt.ylim(0, 1)
    svg_path = os.path.join(output_dir, f"{file_name}.svg")
    plt.savefig(svg_path, format='svg', bbox_inches='tight', transparent=True)
    plt.close(fig)

# 日期范围
start_date = datetime(2025, 5, 1)
end_date = datetime(2025, 5, 30)

# 输出路径
base_dir = "./moon_phases_2025_05"
formats = ["png"]
output_dirs = {fmt: os.path.join(base_dir, fmt) for fmt in formats}
for dir_path in output_dirs.values():
    os.makedirs(dir_path, exist_ok=True)

# 生成图像
for i in range((end_date - start_date).days + 1):
    date = start_date + timedelta(days=i)
    file_name = f"day{(i+1):02d}"
    phase = moon_phase(date)

    img = draw_full_moon_with_craters(phase)
    img.save(os.path.join(output_dirs["png"], f"{file_name}.png"))
    # img.save(os.path.join(output_dirs["webp"], f"{file_name}.webp"))
    # img.convert("RGB").save(os.path.join(output_dirs["jpg"], f"{file_name}.jpg"))
    # save_svg_phase(file_name, phase, output_dirs["svg"])

print(f"✅ 全部生成完毕！图片保存在 {base_dir}，按格式分文件夹，命名为 day01 ~ day31。")
