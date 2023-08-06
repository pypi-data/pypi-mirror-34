from PyQt5 import QtWidgets, QtCore
from sklearn.kernel_ridge import KernelRidge

from point_spectra_gui.ui.cv_KRR import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, KernelRidge, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        print("alpha", self.alpha)
        print("kernel", self.kernel)
        print("gamma", self.gamma)
        print("degree", self.degree)
        print("coef0", self.coef0)
        print("kernel_params", self.kernel_params)
        self.alphaLineEdit.setText(str(self.alpha))
        self.kernelParametersLineEdit.setText(str(self.kernel_params))
        self.gammaLineEdit.setText(str(self.gamma))
        self.degreeLineEdit.setText(str(self.degree))
        self.coeff0LineEdit.setText(str(self.coef0))
        self.kernel_list.setCurrentItem(self.kernel_list.findItems('Radial Basis Function', QtCore.Qt.MatchExactly)[0])

    def run(self):
        k_attrib = {'None': None}
        params = {'alpha': [float(i) for i in self.alphaLineEdit.text().split(',')],
                  'kernel': self.kernel_list.selectedItems(),
                  'gamma': [float(i) for i in self.gammaLineEdit.text().split(',')],
                  'degree': [float(i) for i in self.degreeLineEdit.text().split(',')],
                  'coef0': [float(i) for i in self.coeff0LineEdit.text().split(',')],
                  'kernel_params': [float(i) for i in self.kernelParametersLineEdit.text().split(',')]}
        modelkey = str(params)
        return params, modelkey


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
