from PyQt5 import QtWidgets
from sklearn.linear_model.omp import OrthogonalMatchingPursuit
from sklearn.linear_model.omp import OrthogonalMatchingPursuitCV

from point_spectra_gui.ui.OMP import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, OrthogonalMatchingPursuit, OrthogonalMatchingPursuitCV, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.fitInterceptCheckBox.setChecked(self.fit_intercept)
        self.normalizeCheckBox.setChecked(self.normalize)

    def run(self):
        params = {'n_nonzero_coefs': self.n_coef_spin.value(),
                  'fit_intercept': self.fitInterceptCheckBox.isChecked(),
                  'normalize': self.normalizeCheckBox.isChecked(),
                  'precompute': True}

        return params, self.getChangedValues(params, OrthogonalMatchingPursuit())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
