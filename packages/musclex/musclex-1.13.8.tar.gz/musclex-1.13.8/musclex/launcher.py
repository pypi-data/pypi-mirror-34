from musclex.ui.ui_launcherform import *
import sys, subprocess, os.path
from musclex.utils.exception_handler import handlers

if sys.platform in handlers:
    sys.excepthook = handlers[sys.platform]

class LauncherForm(QWidget):

    programs = ['eq', 'qf', 'pt', 'di', 'im', 'dc', 'ddf']

    def __init__(self):
        super(QWidget, self).__init__()
        
        # Set up the user interface from Designer.
        self.ui = Ui_LauncherForm()
        self.ui.setupUi(self)
        
        # Make some local initializations.
        self.program_idx = 0
        self.ui.runButton.clicked.connect(self.launch)
        self.ui.stackedWidget.currentChanged['int'].connect(self.select)
        
    def select(self, idx):
        self.program_idx = idx

    def launch(self):
        prog = LauncherForm.programs[self.program_idx]
        try:
            path = os.path.dirname(sys.argv[0])
            path = '.' if path == '' else path
            subprocess.Popen([os.path.join(path, 'musclex'), prog])
        except FileNotFoundError:
            subprocess.Popen(['musclex', prog])

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.launch()
    
    @staticmethod
    def main():
        app = QApplication(sys.argv)
        window = LauncherForm()
        window.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    LauncherForm.main()
    
