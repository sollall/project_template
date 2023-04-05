class MyClass:
    """A simple example class"""         # 三重クォートによるコメント

    def __init__(self):                  # コンストラクタ
        self.name = ""

    def getName(self):                   # getName()メソッド
        return self.name

    def setName(self, name):             # setName()メソッド
        self.name = name

def for_release_tag():
    return True