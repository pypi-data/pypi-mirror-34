# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.alphaLabel = QtWidgets.QLabel(self.groupBox)
        self.alphaLabel.setObjectName("alphaLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.alphaLabel)
        self.alpha_text = QtWidgets.QLineEdit(self.groupBox)
        self.alpha_text.setObjectName("alpha_text")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.alpha_text)
        self.maxNumOfIterationsLabel = QtWidgets.QLabel(self.groupBox)
        self.maxNumOfIterationsLabel.setObjectName("maxNumOfIterationsLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.maxNumOfIterationsLabel)
        self.maxNumOfIterationsSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.maxNumOfIterationsSpinBox.setMaximum(999999999)
        self.maxNumOfIterationsSpinBox.setProperty("value", 1000)
        self.maxNumOfIterationsSpinBox.setObjectName("maxNumOfIterationsSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.maxNumOfIterationsSpinBox)
        self.toleranceLabel = QtWidgets.QLabel(self.groupBox)
        self.toleranceLabel.setObjectName("toleranceLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.toleranceLabel)
        self.toleranceDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.toleranceDoubleSpinBox.setDecimals(5)
        self.toleranceDoubleSpinBox.setMaximum(999999999.0)
        self.toleranceDoubleSpinBox.setProperty("value", 0.0001)
        self.toleranceDoubleSpinBox.setObjectName("toleranceDoubleSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.toleranceDoubleSpinBox)
        self.fitInterceptLabel = QtWidgets.QLabel(self.groupBox)
        self.fitInterceptLabel.setObjectName("fitInterceptLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.fitInterceptLabel)
        self.fitInterceptCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.fitInterceptCheckBox.setChecked(True)
        self.fitInterceptCheckBox.setObjectName("fitInterceptCheckBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fitInterceptCheckBox)
        self.forcePositiveCoefficientsLabel = QtWidgets.QLabel(self.groupBox)
        self.forcePositiveCoefficientsLabel.setObjectName("forcePositiveCoefficientsLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.forcePositiveCoefficientsLabel)
        self.forcePositiveCoefficientsCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.forcePositiveCoefficientsCheckBox.setObjectName("forcePositiveCoefficientsCheckBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.forcePositiveCoefficientsCheckBox)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.maxNumOfIterationsSpinBox, self.toleranceDoubleSpinBox)
        Form.setTabOrder(self.toleranceDoubleSpinBox, self.fitInterceptCheckBox)
        Form.setTabOrder(self.fitInterceptCheckBox, self.forcePositiveCoefficientsCheckBox)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.groupBox.setTitle(("LASSO"))
        self.alphaLabel.setText(("Alpha"))
        self.maxNumOfIterationsLabel.setText(("Max # of iterations"))
        self.maxNumOfIterationsSpinBox.setToolTip(("The maximum number of iterations"))
        self.maxNumOfIterationsSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html"))
        self.toleranceLabel.setText(("Tolerance"))
        self.toleranceDoubleSpinBox.setToolTip(("The tolerance for the optimization"))
        self.toleranceDoubleSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html"))
        self.fitInterceptLabel.setText(("Fit Intercept"))
        self.fitInterceptCheckBox.setToolTip(_translate("Form", "whether to calculate the intercept for this model. If set to false,\n"
"no intercept will be used in calculations (e.g. data is expected to\n"
"be already centered)."))
        self.fitInterceptCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html"))
        self.forcePositiveCoefficientsLabel.setText(("Force positive coefficients"))
        self.forcePositiveCoefficientsCheckBox.setToolTip(("When set to True, forces the coefficients to be positive."))
        self.forcePositiveCoefficientsCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

