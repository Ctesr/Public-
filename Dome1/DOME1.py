from svgpathtools import svg2paths, Path, Line, CubicBezier, QuadraticBezier, Arc
#
# paths, attributes = svg2paths('example.svg')
# for path in paths:
#     print(path.d())  # 输出路径数据
# line = Line(start=0+0j, end=100+100j)  # 创建一条从 (0, 0) 到 (100, 100) 的直线
# bezier = CubicBezier(100+100j, 150+50j, 200+150j, 300+100j)  # 创建三次贝塞尔曲线
# path = Path(line, bezier)  # 合并到一个路径中
# # 平移路径
# translated_path = path.translated(50 + 50j)  # 向右下平移 50 单位
# # 获取路径长度
# length = path.length()
# # 计算路径的边界框
# bbox = path.bbox()
# print(f"路径长度: {length}, 边界框: {bbox}")


# from svgpathtools import svg2paths
# import ezdxf


def svg_to_dxf(svg_file, dxf_file):
    # 解析 SVG 路径
    paths, attributes = svg2paths(svg_file)

    # 创建一个新的 DXF 文档
    doc = ezdxf.new()
    msp = doc.modelspace()

    # 遍历 SVG 路径并转换为 DXF 数据
    for path in paths:
        for segment in path:
            if segment.__class__.__name__ == 'Line':
                # 添加直线到 DXF
                msp.add_line(
                    (segment.end.real, segment.end.imag) , # 终点
                    (segment.start.real, segment.start.imag)  # 起点

                )
            elif segment.__class__.__name__ == 'CubicBezier':
                # 将三次贝塞尔曲线近似为折线
                bezier_points = [segment.point(t) for t in [i / 10 for i in range(11)]]  # 细分为 10 段
                for i in range(len(bezier_points) - 1):
                    msp.add_line(
                        (bezier_points[i].real, bezier_points[i].imag),
                        (bezier_points[i + 1].real, bezier_points[i + 1].imag)
                    )
            elif segment.__class__.__name__ == 'QuadraticBezier':
                # 将二次贝塞尔曲线近似为折线
                bezier_points = [segment.point(t) for t in [i / 10 for i in range(11)]]
                for i in range(len(bezier_points) - 1):
                    msp.add_line(
                        (bezier_points[i].real, bezier_points[i].imag),
                        (bezier_points[i + 1].real, bezier_points[i + 1].imag)
                    )
            elif segment.__class__.__name__ == 'Arc':
                # 将圆弧近似为折线
                arc_points = [segment.point(t) for t in [i / 10 for i in range(11)]]
                for i in range(len(arc_points) - 1):
                    msp.add_line(
                        (arc_points[i].real, arc_points[i].imag),
                        (arc_points[i + 1].real, arc_points[i + 1].imag)
                    )

    # 保存为 DXF 文件
    doc.saveas(dxf_file)
    print(f"DXF 文件已保存到 {dxf_file}")


# 调用转换函数
svg_to_dxf('D:\JCtestgit\Dome1\TEST-01.svg', '1112.dxf')


from svgpathtools import svg2paths
import ezdxf
import matplotlib.pyplot as plt
import numpy as np


def svg_to_dxf_with_preview(svg_file, dxf_file):
    paths, attributes = svg2paths(svg_file)
    fig, ax = plt.subplots()

    for path in paths:
        x_vals = []
        y_vals = []

        for segment in path:
            if segment.__class__.__name__ == 'Line':
                x_vals.extend([segment.start.real, segment.end.real])
                y_vals.extend([segment.start.imag, segment.end.imag])
            elif segment.__class__.__name__ == 'CubicBezier':
                bezier_points = [segment.point(t) for t in np.linspace(0, 1, 100)]
                x_vals.extend([p.real for p in bezier_points])
                y_vals.extend([p.imag for p in bezier_points])
            elif segment.__class__.__name__ == 'QuadraticBezier':
                bezier_points = [segment.point(t) for t in np.linspace(0, 1, 100)]
                x_vals.extend([p.real for p in bezier_points])
                y_vals.extend([p.imag for p in bezier_points])
            elif segment.__class__.__name__ == 'Arc':
                arc_points = [segment.point(t) for t in np.linspace(0, 1, 100)]
                x_vals.extend([p.real for p in arc_points])
                y_vals.extend([p.imag for p in arc_points])

            # 绘制每个路径段
            ax.plot(x_vals, y_vals, color='blue', alpha=0.5)  # 动态绘制路径
            plt.pause(0.1)  # 暂停显示

        # 清空临时坐标
        x_vals.clear()
        y_vals.clear()

    plt.show()  # 展示最后的图形

    # 保存为 DXF 文件
    doc = ezdxf.new()
    msp = doc.modelspace()

    for path in paths:
        for segment in path:
            if segment.__class__.__name__ == 'Line':
                msp.add_line(
                    (segment.start.real, segment.start.imag),
                    (segment.end.real, segment.end.imag)
                )
            elif segment.__class__.__name__ == 'CubicBezier':
                bezier_points = [segment.point(t) for t in [i / 10 for i in range(11)]]
                for i in range(len(bezier_points) - 1):
                    msp.add_line(
                        (bezier_points[i].real, bezier_points[i].imag),
                        (bezier_points[i + 1].real, bezier_points[i + 1].imag)
                    )
            elif segment.__class__.__name__ == 'QuadraticBezier':
                bezier_points = [segment.point(t) for t in [i / 10 for i in range(11)]]
                for i in range(len(bezier_points) - 1):
                    msp.add_line(
                        (bezier_points[i].real, bezier_points[i].imag),
                        (bezier_points[i + 1].real, bezier_points[i + 1].imag)
                    )
            elif segment.__class__.__name__ == 'Arc':
                arc_points = [segment.point(t) for t in [i / 10 for i in range(11)]]
                for i in range(len(arc_points) - 1):
                    msp.add_line(
                        (arc_points[i].real, arc_points[i].imag),
                        (arc_points[i + 1].real, arc_points[i + 1].imag)
                    )

    doc.saveas(dxf_file)
    print(f"DXF 文件已保存到 {dxf_file}")


# 使用示例
svg_to_dxf_with_preview('D:\JCtestgit\Dome1\TEST-01.svg', 'cccc.dxf')
