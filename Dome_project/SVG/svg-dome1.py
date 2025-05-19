from lxml import etree

def merge_svgs(svgs, output_file):
    # 创建主SVG根元素
    svg_ns = "http://www.w3.org/2000/svg"
    namespaces = {'svg': svg_ns}
    root = etree.Element("{http://www.w3.org/2000/svg}svg", nsmap={None: svg_ns}, width="800", height="600")

    x_offset = 0  # 初始化x轴偏移量
    for svg_file in svgs:
        tree = etree.parse(svg_file)
        svg_elem = tree.getroot()

        # 创建一个 <g> 元素，将其内容复制到主 SVG 中，并设置偏移
        g = etree.Element("{http://www.w3.org/2000/svg}g", transform=f"translate({x_offset}, 0)")
        for elem in svg_elem:
            g.append(elem)

        root.append(g)

        # 更新 x_offset，使下一个 SVG 文件平移到右侧
        width = svg_elem.attrib.get('width', '100')
        x_offset += int(width)

    # 将合并后的SVG文件保存
    tree = etree.ElementTree(root)
    tree.write(output_file, xml_declaration=True, encoding="utf-8", pretty_print=True)

    print(f"SVG saved as {output_file}")

# 使用示例
merge_svgs(
    [r'D:\JCtestgit\Dome project\SVG\shang.svg', r'D:\JCtestgit\Dome project\SVG\xia.svg'],
    r'D:\JCtestgit\Dome project\SVG\output2.svg'
)
