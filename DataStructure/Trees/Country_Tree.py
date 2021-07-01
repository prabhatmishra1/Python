class Treenode:
    ''' This class represents tree node information'''

    def __init__(self, name):
        self.data = name
        self.children = []
        self.parent = None

    def __str__(self):
        return self.data

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

    def print_tree(self, level):
        if self.get_level()>level:
            return
        spaces = ' '*self.get_level()*5
        prefix = spaces + '|__' if self.parent else ""
        print(prefix, self.data)
        for child in self.children:
            child.print_tree(level)


def build_country_tree():
    Global = Treenode("Global")
    '''creating country herarchy'''
    india = Treenode('India')
    usa = Treenode('USA')
    gujarat = Treenode("Gujarat")
    Karnatak = Treenode("Karnatak")
    new_jersey = Treenode("New Jersey")
    california = Treenode("California")
    ahmedabad = Treenode("Ahmedabad")
    baroda = Treenode("Baroda")
    bangluru = Treenode("Bangluru")
    Mysore = Treenode("Mysore")
    princeton = Treenode("Princeton")
    trenton = Treenode("Trenton")
    San_Francisco = Treenode("San Francisco")
    Mountain_View = Treenode("Mountain View")
    palo_alto = Treenode("Palao Alto")

    Global.add_child(india)
    Global.add_child(usa)
    india.add_child(gujarat)
    india.add_child(Karnatak)
    usa.add_child(new_jersey)
    usa.add_child(california)

    gujarat.add_child(ahmedabad)
    gujarat.add_child(baroda)
    Karnatak.add_child(bangluru)
    Karnatak.add_child(Mysore)

    new_jersey.add_child(princeton)
    new_jersey.add_child(trenton)
    california.add_child(San_Francisco)
    california.add_child(Mountain_View)
    california.add_child(palo_alto)

    return Global


if __name__ == "__main__":
    Global = build_country_tree()
    # print(root)
    # print(root.get_level())
    # print(root.children)

    Global.print_tree(3)
