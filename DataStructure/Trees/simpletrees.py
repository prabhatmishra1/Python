class Treenode:
    ''' This class represents tree node information'''

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        return self.children

    def get_level(self):
        level = 0
        temp = self.parent
        while temp!=None:
            temp = temp.parent
            level += 1
        return level

    def print_tree(self):
        spaces=' '*self.get_level()*5
        prefix=spaces + '|__' if self.parent else ""
        print(prefix,self.data)
        for child in self.children:
            child.print_tree()

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


def build_product_tree():
    root = Treenode("Electronics")

    laptop = Treenode('laptop')
    laptop.add_child(Treenode('MAC'))
    laptop.add_child(Treenode('Thinkpad'))

    cell_phone = Treenode('cell phone')
    cell_phone.add_child(Treenode('iphone'))
    cell_phone.add_child(Treenode('android'))

    tv = Treenode('TV')
    tv.add_child(Treenode('one-pluse'))
    tv.add_child(Treenode('samsung'))

    root.add_child(laptop)
    root.add_child(cell_phone)
    root.add_child(tv)
    #print(laptop.get_level())
    return root


if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
