# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sm_cipher_tools.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sm_cipher_tools(object):
    def setupUi(self, sm_cipher_tools):
        sm_cipher_tools.setObjectName("sm_cipher_tools")
        sm_cipher_tools.resize(652, 734)
        icon = QtGui.QIcon.fromTheme("ahdms")
        sm_cipher_tools.setWindowIcon(icon)
        sm_cipher_tools.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(sm_cipher_tools)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.pubky_LE = QtWidgets.QLineEdit(sm_cipher_tools)
        self.pubky_LE.setText("")
        self.pubky_LE.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pubky_LE.setObjectName("pubky_LE")
        self.gridLayout.addWidget(self.pubky_LE, 2, 1, 1, 10)
        self.plaintext_hex = QtWidgets.QLineEdit(sm_cipher_tools)
        self.plaintext_hex.setText("")
        self.plaintext_hex.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.plaintext_hex.setObjectName("plaintext_hex")
        self.gridLayout.addWidget(self.plaintext_hex, 6, 1, 1, 10)
        self.label_8 = QtWidgets.QLabel(sm_cipher_tools)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1, QtCore.Qt.AlignRight)
        self.sm2_encrypt_Button = QtWidgets.QPushButton(sm_cipher_tools)
        self.sm2_encrypt_Button.setObjectName("sm2_encrypt_Button")
        self.gridLayout.addWidget(self.sm2_encrypt_Button, 27, 2, 1, 1)
        self.decrypt_result = QtWidgets.QLineEdit(sm_cipher_tools)
        self.decrypt_result.setText("")
        self.decrypt_result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.decrypt_result.setObjectName("decrypt_result")
        self.gridLayout.addWidget(self.decrypt_result, 22, 1, 1, 10)
        self.label_symm_key = QtWidgets.QLabel(sm_cipher_tools)
        self.label_symm_key.setObjectName("label_symm_key")
        self.gridLayout.addWidget(self.label_symm_key, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.sm4_encrypt_Button = QtWidgets.QPushButton(sm_cipher_tools)
        self.sm4_encrypt_Button.setObjectName("sm4_encrypt_Button")
        self.gridLayout.addWidget(self.sm4_encrypt_Button, 26, 4, 1, 1)
        self.e_LE = QtWidgets.QLineEdit(sm_cipher_tools)
        self.e_LE.setText("")
        self.e_LE.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.e_LE.setObjectName("e_LE")
        self.gridLayout.addWidget(self.e_LE, 9, 1, 1, 10)
        self.id_iv = QtWidgets.QLineEdit(sm_cipher_tools)
        self.id_iv.setText("")
        self.id_iv.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.id_iv.setObjectName("id_iv")
        self.gridLayout.addWidget(self.id_iv, 8, 1, 1, 10)
        self.sm2_sign_Button = QtWidgets.QPushButton(sm_cipher_tools)
        self.sm2_sign_Button.setObjectName("sm2_sign_Button")
        self.gridLayout.addWidget(self.sm2_sign_Button, 27, 4, 1, 1)
        self.sm3_hash = QtWidgets.QLineEdit(sm_cipher_tools)
        self.sm3_hash.setText("")
        self.sm3_hash.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sm3_hash.setObjectName("sm3_hash")
        self.gridLayout.addWidget(self.sm3_hash, 7, 1, 1, 10)
        self.label_11 = QtWidgets.QLabel(sm_cipher_tools)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 22, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label = QtWidgets.QLabel(sm_cipher_tools)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_5 = QtWidgets.QLabel(sm_cipher_tools)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1, QtCore.Qt.AlignRight)
        self.S = QtWidgets.QLineEdit(sm_cipher_tools)
        self.S.setObjectName("S")
        self.gridLayout.addWidget(self.S, 16, 1, 1, 10)
        self.label_4 = QtWidgets.QLabel(sm_cipher_tools)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1, QtCore.Qt.AlignRight)
        self.plaintext = QtWidgets.QLineEdit(sm_cipher_tools)
        self.plaintext.setText("")
        self.plaintext.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.plaintext.setObjectName("plaintext")
        self.gridLayout.addWidget(self.plaintext, 5, 1, 1, 10)
        self.result_textEdit = QtWidgets.QTextEdit(sm_cipher_tools)
        self.result_textEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.result_textEdit.setObjectName("result_textEdit")
        self.gridLayout.addWidget(self.result_textEdit, 34, 0, 1, 11)
        self.privkey = QtWidgets.QLineEdit(sm_cipher_tools)
        self.privkey.setText("")
        self.privkey.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.privkey.setObjectName("privkey")
        self.gridLayout.addWidget(self.privkey, 0, 1, 1, 10)
        self.gen_keypair_Button = QtWidgets.QPushButton(sm_cipher_tools)
        self.gen_keypair_Button.setObjectName("gen_keypair_Button")
        self.gridLayout.addWidget(self.gen_keypair_Button, 27, 1, 1, 1)
        self.sm2_verify_Button = QtWidgets.QPushButton(sm_cipher_tools)
        self.sm2_verify_Button.setObjectName("sm2_verify_Button")
        self.gridLayout.addWidget(self.sm2_verify_Button, 27, 5, 1, 1)
        self.label_s = QtWidgets.QLabel(sm_cipher_tools)
        self.label_s.setObjectName("label_s")
        self.gridLayout.addWidget(self.label_s, 16, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_C2 = QtWidgets.QLabel(sm_cipher_tools)
        self.label_C2.setObjectName("label_C2")
        self.gridLayout.addWidget(self.label_C2, 20, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_6 = QtWidgets.QLabel(sm_cipher_tools)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1, QtCore.Qt.AlignRight)
        self.sm3_Button = QtWidgets.QPushButton(sm_cipher_tools)
        self.sm3_Button.setObjectName("sm3_Button")
        self.gridLayout.addWidget(self.sm3_Button, 24, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(sm_cipher_tools)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.symm_key = QtWidgets.QLineEdit(sm_cipher_tools)
        self.symm_key.setObjectName("symm_key")
        self.gridLayout.addWidget(self.symm_key, 4, 1, 1, 10)
        self.label_10 = QtWidgets.QLabel(sm_cipher_tools)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_C3 = QtWidgets.QLabel(sm_cipher_tools)
        self.label_C3.setObjectName("label_C3")
        self.gridLayout.addWidget(self.label_C3, 19, 0, 1, 1, QtCore.Qt.AlignRight)
        self.encrypt_result = QtWidgets.QLineEdit(sm_cipher_tools)
        self.encrypt_result.setObjectName("encrypt_result")
        self.gridLayout.addWidget(self.encrypt_result, 21, 1, 1, 10)
        self.label_2 = QtWidgets.QLabel(sm_cipher_tools)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.sm2_decrypt_Button = QtWidgets.QPushButton(sm_cipher_tools)
        self.sm2_decrypt_Button.setSizeIncrement(QtCore.QSize(0, 0))
        self.sm2_decrypt_Button.setObjectName("sm2_decrypt_Button")
        self.gridLayout.addWidget(self.sm2_decrypt_Button, 27, 3, 1, 1)
        self.clear_input_Button = QtWidgets.QPushButton(sm_cipher_tools)
        self.clear_input_Button.setObjectName("clear_input_Button")
        self.gridLayout.addWidget(self.clear_input_Button, 24, 5, 1, 1)
        self.pubkall_LE = QtWidgets.QLineEdit(sm_cipher_tools)
        self.pubkall_LE.setText("")
        self.pubkall_LE.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pubkall_LE.setObjectName("pubkall_LE")
        self.gridLayout.addWidget(self.pubkall_LE, 3, 1, 1, 10)
        self.mode_comboBox = QtWidgets.QComboBox(sm_cipher_tools)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mode_comboBox.sizePolicy().hasHeightForWidth())
        self.mode_comboBox.setSizePolicy(sizePolicy)
        self.mode_comboBox.setObjectName("mode_comboBox")
        self.mode_comboBox.addItem("")
        self.mode_comboBox.addItem("")
        self.mode_comboBox.addItem("")
        self.mode_comboBox.addItem("")
        self.gridLayout.addWidget(self.mode_comboBox, 26, 1, 1, 1)
        self.R = QtWidgets.QLineEdit(sm_cipher_tools)
        self.R.setObjectName("R")
        self.gridLayout.addWidget(self.R, 15, 1, 1, 10)
        self.label_C1 = QtWidgets.QLabel(sm_cipher_tools)
        self.label_C1.setObjectName("label_C1")
        self.gridLayout.addWidget(self.label_C1, 18, 0, 1, 1, QtCore.Qt.AlignRight)
        self.pubkx_LE = QtWidgets.QLineEdit(sm_cipher_tools)
        self.pubkx_LE.setText("")
        self.pubkx_LE.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pubkx_LE.setObjectName("pubkx_LE")
        self.gridLayout.addWidget(self.pubkx_LE, 1, 1, 1, 10)
        self.label_9 = QtWidgets.QLabel(sm_cipher_tools)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 21, 0, 1, 1, QtCore.Qt.AlignRight)
        self.C1 = QtWidgets.QLineEdit(sm_cipher_tools)
        self.C1.setText("")
        self.C1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.C1.setObjectName("C1")
        self.gridLayout.addWidget(self.C1, 18, 1, 1, 10)
        self.pad_checkBox = QtWidgets.QCheckBox(sm_cipher_tools)
        self.pad_checkBox.setObjectName("pad_checkBox")
        self.gridLayout.addWidget(self.pad_checkBox, 26, 2, 1, 1)
        self.sm4_decrypt_Button = QtWidgets.QPushButton(sm_cipher_tools)
        self.sm4_decrypt_Button.setObjectName("sm4_decrypt_Button")
        self.gridLayout.addWidget(self.sm4_decrypt_Button, 26, 5, 1, 1)
        self.label_12 = QtWidgets.QLabel(sm_cipher_tools)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1, QtCore.Qt.AlignRight)
        self.C2 = QtWidgets.QLineEdit(sm_cipher_tools)
        self.C2.setObjectName("C2")
        self.gridLayout.addWidget(self.C2, 20, 1, 1, 10)
        self.C3 = QtWidgets.QLineEdit(sm_cipher_tools)
        self.C3.setEnabled(True)
        self.C3.setText("")
        self.C3.setFrame(True)
        self.C3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.C3.setDragEnabled(False)
        self.C3.setObjectName("C3")
        self.gridLayout.addWidget(self.C3, 19, 1, 1, 10)
        self.label_r = QtWidgets.QLabel(sm_cipher_tools)
        self.label_r.setObjectName("label_r")
        self.gridLayout.addWidget(self.label_r, 15, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_7 = QtWidgets.QLabel(sm_cipher_tools)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 17, 0, 1, 1, QtCore.Qt.AlignRight)
        self.signature_value = QtWidgets.QLineEdit(sm_cipher_tools)
        self.signature_value.setText("")
        self.signature_value.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.signature_value.setObjectName("signature_value")
        self.gridLayout.addWidget(self.signature_value, 17, 1, 1, 10)
        self.result_textEdit.raise_()
        self.label_8.raise_()
        self.label_3.raise_()
        self.pubkall_LE.raise_()
        self.label_6.raise_()
        self.pubky_LE.raise_()
        self.label_5.raise_()
        self.decrypt_result.raise_()
        self.label_4.raise_()
        self.pubkx_LE.raise_()
        self.label_12.raise_()
        self.plaintext_hex.raise_()
        self.label_10.raise_()
        self.id_iv.raise_()
        self.label_11.raise_()
        self.e_LE.raise_()
        self.sm3_hash.raise_()
        self.privkey.raise_()
        self.plaintext.raise_()
        self.label_2.raise_()
        self.C1.raise_()
        self.label.raise_()
        self.C2.raise_()
        self.encrypt_result.raise_()
        self.C3.raise_()
        self.label_9.raise_()
        self.label_C2.raise_()
        self.label_C3.raise_()
        self.label_C1.raise_()
        self.symm_key.raise_()
        self.label_symm_key.raise_()
        self.sm2_encrypt_Button.raise_()
        self.sm2_decrypt_Button.raise_()
        self.sm2_sign_Button.raise_()
        self.sm2_verify_Button.raise_()
        self.gen_keypair_Button.raise_()
        self.sm3_Button.raise_()
        self.clear_input_Button.raise_()
        self.sm4_decrypt_Button.raise_()
        self.sm4_encrypt_Button.raise_()
        self.mode_comboBox.raise_()
        self.pad_checkBox.raise_()
        self.label_r.raise_()
        self.R.raise_()
        self.label_s.raise_()
        self.S.raise_()
        self.label_7.raise_()
        self.signature_value.raise_()

        self.retranslateUi(sm_cipher_tools)
        QtCore.QMetaObject.connectSlotsByName(sm_cipher_tools)

    def retranslateUi(self, sm_cipher_tools):
        _translate = QtCore.QCoreApplication.translate
        sm_cipher_tools.setWindowTitle(_translate("sm_cipher_tools", "sm_cipher_tools"))
        self.label_8.setText(_translate("sm_cipher_tools", "ID/IV(HEX)："))
        self.sm2_encrypt_Button.setText(_translate("sm_cipher_tools", "SM2加密"))
        self.label_symm_key.setText(_translate("sm_cipher_tools", "对称密钥(HEX)："))
        self.sm4_encrypt_Button.setText(_translate("sm_cipher_tools", "SM4加密"))
        self.sm2_sign_Button.setText(_translate("sm_cipher_tools", "SM2签名"))
        self.label_11.setText(_translate("sm_cipher_tools", "解密结果(HEX)："))
        self.label.setText(_translate("sm_cipher_tools", "私钥(HEX)："))
        self.label_5.setText(_translate("sm_cipher_tools", "原文："))
        self.label_4.setText(_translate("sm_cipher_tools", "原文(HEX)："))
        self.gen_keypair_Button.setText(_translate("sm_cipher_tools", "密钥对生成"))
        self.sm2_verify_Button.setText(_translate("sm_cipher_tools", "SM2验签"))
        self.label_s.setText(_translate("sm_cipher_tools", "S(HEX)："))
        self.label_C2.setText(_translate("sm_cipher_tools", "C2(M^t)："))
        self.label_6.setText(_translate("sm_cipher_tools", "SM3哈希(HEX)："))
        self.sm3_Button.setText(_translate("sm_cipher_tools", "SM3摘要"))
        self.label_3.setText(_translate("sm_cipher_tools", "Y(HEX)："))
        self.label_10.setText(_translate("sm_cipher_tools", "公钥(HEX)："))
        self.label_C3.setText(_translate("sm_cipher_tools", "C3(hash)："))
        self.label_2.setText(_translate("sm_cipher_tools", "X(HEX)："))
        self.sm2_decrypt_Button.setText(_translate("sm_cipher_tools", "SM2解密"))
        self.clear_input_Button.setText(_translate("sm_cipher_tools", "清空数据"))
        self.mode_comboBox.setItemText(0, _translate("sm_cipher_tools", "ECB"))
        self.mode_comboBox.setItemText(1, _translate("sm_cipher_tools", "CBC"))
        self.mode_comboBox.setItemText(2, _translate("sm_cipher_tools", "CFB"))
        self.mode_comboBox.setItemText(3, _translate("sm_cipher_tools", "OFB"))
        self.label_C1.setText(_translate("sm_cipher_tools", "C1(x,y)："))
        self.label_9.setText(_translate("sm_cipher_tools", "加密结果(HEX)："))
        self.pad_checkBox.setText(_translate("sm_cipher_tools", "PAD"))
        self.sm4_decrypt_Button.setText(_translate("sm_cipher_tools", "SM4解密"))
        self.label_12.setText(_translate("sm_cipher_tools", "e值(HEX)："))
        self.label_r.setText(_translate("sm_cipher_tools", "R(HEX)："))
        self.label_7.setText(_translate("sm_cipher_tools", "签名值(HEX)："))
