import tkinter
import webbrowser

class Click(tkinter.Button):
    def __init__(self, title, url, master = None):
        super().__init__(master, text = title, width = 15, command = self.click_button)
        self.url = url
    def click_button(self):
        return webbrowser.open(self.url)

if __name__ == '__main__':
    list = [
        ['Arsenal', 'https://www.arsenal.com'], 
        ['Barcelona', 'https://www.fcbarcelona.jp/ja/']
    ]

root = tkinter.Tk()
for i in list:
    btn = Click(*i)
    btn.pack()
root.mainloop()


