# 二叉树可视化
import networkx as nx
import matplotlib.pyplot as plt


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def visualize_tree(root):
    graph = nx.DiGraph()

    def add_nodes(node, parent=None):
        if node:
            graph.add_node(node.val)
            if parent:
                graph.add_edge(parent.val, node.val)
            add_nodes(node.left, node)
            add_nodes(node.right, node)

    add_nodes(root)
    pos = nx.nx_agraph.graphviz_layout(graph, prog='dot')
    nx.draw(graph, pos, with_labels=True, arrows=False)
    plt.show()


# 使用示例
root = TreeNode(1,
                TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3, TreeNode(6)))
visualize_tree(root)