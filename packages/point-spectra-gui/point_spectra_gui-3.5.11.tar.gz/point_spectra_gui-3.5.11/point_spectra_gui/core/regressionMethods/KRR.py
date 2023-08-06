from PyQt5 import QtWidgets
from sklearn.kernel_ridge import KernelRidge

from point_spectra_gui.ui.KRR import Ui_Form
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
        # print("alpha", self.alpha)
        # print("kernel", self.kernel)
        # print("gamma", self.gamma)
        # print("degree", self.degree)
        # print("coef0", self.coef0)
        # print("kernel_params", self.kernel_params)
        self.alphaSpinBox.setValue(self.alpha)
        self.kernelParametersLineEdit.setText(str(self.kernel_params))
        self.gammaLineEdit.setText(str(self.gamma))
        self.degreeDoubleSpinBox.setValue(self.degree)
        self.coeff0DoubleSpinBox.setValue(self.coef0)
        self.kernelLineEdit.setText(str(self.kernel))

    def run(self):
        k_attrib = {'None': None}
        params = {'alpha': self.alphaSpinBox.value(),
                  'kernel': self.kernelLineEdit.text(),
                  'gamma': self.gammaLineEdit.text(),
                  'degree': self.degreeDoubleSpinBox.value(),
                  'coef0': self.coeff0DoubleSpinBox.value(),
                  'kernel_params': k_attrib[self.kernelParametersLineEdit.text()]}
        return params, self.getChangedValues(params, KernelRidge())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
