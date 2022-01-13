#duck typing is something similar to interfaces of java yet not exact same
#ide variable can act as object for any class provided that class have the driver class method
# if either pycharm or vscode dont have execute method then error arraises
#ide here is a parameter denoting a class

class pycharm:
    def execute(self):
        print("Im pycharm")
        print("I can compile")
    
class vscode:
    def execute(self):
        print("Im vscode")
        print("I can execute")

class laptop:               #driver class
    def code(self,ide):
        ide.execute()

ide=pycharm()
lap1=laptop()
lap1.code(ide)
ide=vscode()
lap2=laptop()
lap2.code(ide)