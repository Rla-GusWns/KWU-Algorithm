def treeDelete(t, r, p):
    if r == t:
        t = deleteNode(r)
    elif r == p.left:
        p.left = deleteNode(r)
    else:
        p.right = deleteNode(r)

def deleteNode(r):
    if r.left == None and r.right == None:
        return None
    elif r.left != None and r.right == None:
        return r.left
    elif r.right != None and r.left == None:
        return r.right
    else:
        s = r.right
        while s.left != None:
            parent = s
            s = s.left
        r.key = s.key
        if s == r.right:
            r.right = s.right
        else:
            parent.left = s.right
        return r