import svgpathtools
from shapely.geometry import Polygon
import os

def validate_svg(svg_path):
    # 解析 SVG 文件，提取路径
    try:
        paths, _ = svgpathtools.svg2paths(svg_path)
    except Exception as e:
        print(f"无法解析 SVG 文件 {svg_path}: {e}")
        return

    # 存储有效的多边形
    valid_polygons = []

    for path in paths:
        for segment in path:
            # 获取路径的坐标
            coords = [(point.real, point.imag) for point in segment]

            # 检查坐标点是否足够构成一个有效的多边形
            if len(coords) >= 4:
                # 确保多边形闭合
                if coords[0] != coords[-1]:
                    coords.append(coords[0])  # 添加第一个点到最后以闭合多边形

                poly = Polygon(coords)

                # 检查多边形的有效性
                if poly.is_valid:
                    valid_polygons.append(poly)
                else:
                    print(f"无效多边形，已跳过: {poly}")
            else:
                print(f"路径坐标点不足，无法形成有效的多边形: {coords}")

    if valid_polygons:
        print(f"找到 {len(valid_polygons)} 个有效多边形。")
    else:
        print("没有找到有效的多边形。")


# 直接验证本地 SVG 文件
local_svg_path = r"D:\JCtestgit\Dome project\SVG\长方形.svg"  # 使用原始字符串
validate_svg(local_svg_path)

# 如果需要，可以在处理完后删除本地下载的文件
# os.remove(local_svg_path)  # 如果需要删除，可以取消注释
