def restore_bst(prefix_lst):
    bst = BinarySearchTreeMap()
    if len(prefix_lst) == 0:
        return bst
    bst[prefix_lst[0]] = None
    root_val = prefix_lst[0]
    if len(prefix_lst) == 1:
        return bst
    else:
        restore_bst_helper(bst, bst.root, root_val, prefix_lst[1:])
    return bst

def restore_bst_helper(tree, curr_root, data,lst):
    if len(lst) == 0:
        pass
    elif lst[0] < curr_root.item.key:
        new = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(lst[0]))
        curr_root.left = new
        new.parent = curr_root
        tree.size += 1
        restore_bst_helper(tree, new, data, lst[1:])
    else:
        new = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(lst[0]))
        if data is not None and lst[0] > data:
            tree.root.right = new
            new.parent = tree.root
            restore_bst_helper(tree, new, None, lst[1:])
        elif lst[0] > curr_root.parent.item.key:
            curr_root.parent.right = new
            new.parent = curr_root.parent
            restore_bst_helper(tree, new, data, lst[1:])
        else:
            curr_root.right = new
            new.parent = curr_root
            restore_bst_helper(tree, new, data, lst[1:])
        tree.size += 1
