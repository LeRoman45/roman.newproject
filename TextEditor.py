class TextEditor():
    def __init__(self,text_file):
        self.text_file = text_file
        self.text=''
        self.count=1

    def read(self):
        with open(self.text_file+".txt", "r", encoding= "utf-8") as file:
            self.text= file.read()
            print(self.text)

    def copy(self):
        with open(self.text_file+str(self.count)+".txt", "w", encoding= "utf-8") as file:
            file.write(self.text)
            self.count+=1


text_name=input("Введіть назву файлу")


first = TextEditor(text_name)
first.read()
first.copy()