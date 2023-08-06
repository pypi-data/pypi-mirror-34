import pandas as pd
from PyQt5 import QtWidgets
from point_spectra_gui.util.spectral_data import spectral_data

from point_spectra_gui.ui.LoadData import Ui_loadData
from point_spectra_gui.util.Modules import Modules


class LoadData(Ui_loadData, Modules):
    """
    Loads the data into the UI.
    The data needs to be a *.csv in order for this application to work
    """
    count = -1

    def __init__(self):
        LoadData.count += 1
        self.curr_count = LoadData.count
        #print('Added LoadData with ID {}'.format(self.curr_count))

    def delete(self):
        try:
            LoadData.count -= 1
            del self.data[self.datakeys[-1]]
            del self.datakeys[-1]
        except IndexError:
            pass

    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.newFilePushButton.clicked.connect(lambda: self.getDataButton_clicked(self.fileNameLineEdit))

    def getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Data File", self.outpath, "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")

    def setup(self):
        """
        The setup here is only doing the first 2 rows of our dataset
        This will cut down on time to load.

        :return:
        """
        try:
            filename = self.fileNameLineEdit.text()
            keyname = self.dataSetNameLineEdit.text()
            self.data[keyname] = spectral_data(pd.read_csv(filename, header=[0, 1], verbose=False, nrows=2))
            self.list_amend(self.datakeys, self.curr_count, keyname)
        except:
            pass

    def run(self, filename = None, keyname = None):
        if filename == None:
            filename = self.fileNameLineEdit.text()
        if keyname == None:
            keyname = self.dataSetNameLineEdit.text()
        print('Loading data file: ' + str(filename))
        self.data[keyname] = spectral_data(pd.read_csv(filename, header=[0, 1], verbose=False))
        self.list_amend(self.datakeys, self.curr_count, keyname)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = LoadData()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
