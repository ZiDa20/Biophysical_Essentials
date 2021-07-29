


class KonsoleCompile():
    """Start a compiler for the functions that are interpreted in python code"""

    def __init__(self):
        self.text = None
        self.dictionary = {"ChangePlotAxis": self.change_plot_axis, "ChangePlotColor": self.change_plot_color}
        self.answer = None

    def set_text(self,text):
        "gets the text from the command line console"
        text = text.split(" ")[0]
        
        
    def get_function_from_text(self, color):
        func = self.dictionary.get(self.text)
        self.answer = "starting function: " + str(func)
        func(color)
        return self.answer

    def change_plot_color(color):
