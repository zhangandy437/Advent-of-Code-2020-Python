class Solution:
    def input(self, path):
        f = open(path, "r")
        lines = f.read().splitlines()
        f.close()
        return lines

    def p1(self, arr, find):
        d = {}
        for bag in arr:
            bags = bag.split("contain ")
            outer = bags[0][:-6]
            for inner in bags[1][:-1].split(", "):
                if inner[0:2] != "no":
                    color = None
                    if inner[0] == "1":
                        color = inner[2:-4]
                    else:
                        color = inner[2:-5]
                    if color in d:
                        d[color].append(outer)
                    else:
                        d[color] = [outer]
        q = []
        s = set()
        for i in d[find]: q.append(i)
        while q:
            cur = q.pop()
            s.add(cur)
            if cur in d:
                for i in d[cur]:
                    q.append(i)
        return len(s)
    
    
    
    def p2(self, arr, find):
        d = {}
        for bag in arr:
            bags = bag.split("contain ")
            outer = bags[0][:-6]
            cur = []
            for inner in bags[1][:-1].split(", "):
                if inner[0:2] != "no":
                    if inner[0] == "1":
                        cur.append(inner[0:-4])
                    else:
                        cur.append(inner[0:-5])
            if cur:
                d[outer] = cur

        num = 1
        return self.bt(d, find)
            
    # return num in 1 of this col
    def bt(self, d, col):
        if col in d:
            summ = 0
            for inner in d[col]:
                e = self.bt(d, inner[2:])
                summ += int(inner[0]) * e + int(inner[0])
            return summ
        else:
            return 0


test = Solution()
print(test.p2(test.input("Day7/input.txt"), "shiny gold"))

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        queue = collections.deque()
        queue.append(root)
        while queue:
            length = len(queue)
            pre = None
            for _ in range(length):
                node = queue.popleft()
                if pre is not None:
                    pre.next = node
                pre = node
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                    
        return root