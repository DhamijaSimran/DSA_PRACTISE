from flexx import flx

class Example(flx.Widget):

    def init(self):
        flx.Button(text="hello")
        flx.Button(text="world")

if __name__=="__main__":
    flx.launch(Example)
    flx.run()
