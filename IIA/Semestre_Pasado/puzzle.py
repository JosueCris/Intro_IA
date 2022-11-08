import copy

done = []
way = []
class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.branches = []

    def is_goal(self, goal):
        return self.data == goal

    def get_position(self):
        count = 0
        pos_x = -1
        pos_y = -1
        for row in self.data:
            try:
                pos_y = row.index("_")
                pos_x = count
            except Exception as e:
                pass
            count += 1
        return pos_x, pos_y         
    
    def move_up(self, pos_x, pos_y):
        if pos_x == 0:
            return None
        branch = copy.deepcopy(self.data)
        tmp = branch[pos_x - 1][pos_y]
        branch[pos_x - 1][pos_y] = "_"
        branch[pos_x][pos_y] = tmp
        self.branches.append(TreeNode(branch))

    def move_right(self, pos_x, pos_y):
        if pos_y == 2:
            return None
        branch = copy.deepcopy(self.data)
        tmp = branch[pos_x][pos_y + 1]
        branch[pos_x][pos_y + 1] = "_"
        branch[pos_x][pos_y] = tmp
        self.branches.append(TreeNode(branch))

    def move_down(self, pos_x, pos_y):
        if pos_x == 2:
            return None
        branch = copy.deepcopy(self.data)
        tmp = branch[pos_x + 1][pos_y]
        branch[pos_x + 1][pos_y] = "_"
        branch[pos_x][pos_y] = tmp
        self.branches.append(TreeNode(branch))

    def move_left(self, pos_x, pos_y):
        if pos_y == 0:
            return None
        branch = copy.deepcopy(self.data)
        tmp = branch[pos_x][pos_y - 1]
        branch[pos_x][pos_y - 1] = "_"
        branch[pos_x][pos_y] = tmp
        self.branches.append(TreeNode(branch))

    def gen_branches(self):
        pos_x, pos_y = self.get_position()
        if pos_x == -1 or pos_y == -1:
            return None
        self.move_up(pos_x, pos_y)
        self.move_right(pos_x, pos_y)
        self.move_down(pos_x, pos_y)
        self.move_left(pos_x, pos_y)        
    
    def is_done(self):
        for element in done:
            if element == self.data:
                return True
        return False

    def DFS(self, goal):
        if not self.data:
            return False
        if self.is_goal(goal):
            way.append(self.data)
            return True
        if self.is_done():#self.data in done:
            return False
        done.append(self.data)
        self.gen_branches()
        for branch in self.branches:
            if branch.DFS(goal):
                way.append(self.data)
                return True
        return False

    def BFS(self):
         pass   



goal = [
       [1, 2, 3],
       [8, "_", 4],
       [7, 6, 5]
       ]

test_state = [
             [5, 4, 1],
             [6, "_", 8],
             [7, 3 , 2]
]

test_state2 = goal = [
                     [1, 2, "_"],
                     [8, 3, 4],
                     [7, 6, 5]
]
root = TreeNode(test_state)
#root.gen_branches()
#print(root.data)
#for l in root.branches:
#    print(l.data)
#
#r = []
#for i in range(10):
#    r.insert(0, i)
#print(r)        
root.DFS(goal)
for l in way:
    print(l)
