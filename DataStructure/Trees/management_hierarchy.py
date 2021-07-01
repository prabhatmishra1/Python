class Treenode:
    ''' This class represents tree node information'''

    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def __str__(self):
        return self.name

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        return self.children

    def get_level(self):
        level = 0
        temp = self.parent
        while temp != None:
            temp = temp.parent
            level += 1
        return level

    def print_tree(self, option=None):
        spaces = ' '*self.get_level()*5
        prefix = spaces + '|__' if self.parent else ""
        if option is "name":
            print(prefix, self.name)
        elif option is "designation":
            print(prefix, self.designation)
        elif option is "both":
            print(prefix, self.name, self.designation)
        else:
            print("Enter valid option please")
            return
        for child in self.children:
            child.print_tree(option)

        # for child in self.children:
        #     print("   |--", child.data)
        #     for value in child.children:
        #         print("        |--", value.data)

        #     temp = []
        #     for value in child.children:
        #         temp.append(value.data)
        #     product[child.data] = temp
        # print({self.data:product})
        # pass


def build_employee_tree():
    root = Treenode("Nilpul", "(CEO)")
    '''creating employee'''
    cto = Treenode('Chinmay', "(CTO)")
    Vishwa = Treenode("Vishwa", "(Infrastructure Head)")
    Dhawal = Treenode('Dhawal', "(Cloud Manager)")
    Abijit = Treenode('Abijit', "(App Manager)")
    Aamir = Treenode('Aamir', "(App Head)")
    gels = Treenode('Gels', "(HR Head)")
    Peter = Treenode('Peter', "(Requirement Manager)")
    waqas = Treenode('Waqas', "(Policy Manager)")

    root.add_child(cto)
    root.add_child(gels)
    cto.add_child(Vishwa)
    cto.add_child(Aamir)
    Vishwa.add_child(Dhawal)
    Vishwa.add_child(Abijit)
    gels.add_child(Peter)
    gels.add_child(waqas)
    # print(laptop.get_level())
    return root


if __name__ == "__main__":
    root = build_employee_tree()
    # print(root)
    # print(root.get_level())
    # print(root.children)

    root.print_tree("both")
