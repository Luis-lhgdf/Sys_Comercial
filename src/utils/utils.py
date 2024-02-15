import ctypes

class Utilities:

    def __init__(self) -> None:
        pass

    def msgbox(self, title, text, style):
        #  Styles:
        #  0 : OK
        #  1 : OK | Cancel
        #  2 : Abort | Retry | Ignore
        #  3 : Yes | No | Cancel 6, 7, 2
        #  4 : Yes | No
        #  5 : Retry | Cancel
        #  6 : Cancel | Try Again | Continue 

        return ctypes.windll.user32.MessageBoxW(0, text, title, style)
       

