class parent_1:
    def parent_info(self):
        print("This is first parent information")
class parent_2:
    def parent_info_2(self):
        print("This is second parent information")
class child(parent_1,parent_2):
    pass

child_obj = child()
child_obj.parent_info()
child_obj.parent_info_2()