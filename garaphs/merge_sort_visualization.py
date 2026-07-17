from graphviz import Digraph

def merge_sort_graph(arr):
    dot = Digraph()
    
    def helper(sub_arr):
        node_id = str(id(sub_arr))
        label = str(sub_arr)
        dot.node(node_id, label)

        if len(sub_arr) > 1:
            mid = len(sub_arr) // 2
            left = sub_arr[:mid]
            right = sub_arr[mid:]

            left_id = helper(left)
            right_id = helper(right)

            dot.edge(node_id, left_id, label="L")
            dot.edge(node_id, right_id, label="R")

        return node_id

    helper(arr)
    return dot


# Example
arr = [8, 3, 5, 2, 9, 1]
dot = merge_sort_graph(arr)
dot.render('merge_sort_tree', format='png', view=True)