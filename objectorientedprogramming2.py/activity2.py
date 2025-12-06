class employee():
    def __init__(self):
        print('employee is created')
    def __del__(self):
        print('employee destroyed')
def create_obj():
    print('Making object')
    obj=employee()
    print('function  end')
    return obj
print('calling create_obj fucntion')
obj=create_obj()
print('program end')