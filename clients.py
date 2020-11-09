import var
from PyQt5 import QtWidgets

class Clientes():

    def validarDni(dni):

        '''código que controla si el dni o nif es correcto'''

        try:
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "0123456789"
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control
            return False

        except:
            print('Error módulo validar DNI')
            return None

    def validoDni():

        '''muestra mensaje de dni válido'''

        try:
            dni = var.ui.editDni.text()
            if Clientes.validarDni(dni):
                var.ui.lblValidar.setStyleSheet('QLabel {color: green}')
                var.ui.lblValidar.setText('V')
                var.ui.editDni.setText(dni.upper())
            else:
                var.ui.lblValidar.setStyleSheet('QLabel {color: red}')
                var.ui.lblValidar.setText('X')
                var.ui.editDni.setText(dni.upper())

        except:
            print('Error módulo escribir valido DNI')
            return None

    def selSexo():
        try:
            if var.ui.rbtFem.isChecked():
                var.sex = 'Mujer'
            if var.ui.rbtMasc.isChecked():
                var.sex = 'Hombre'
        except Exception as error:
            print('Error: %s ' % str(error))

    def selPago():
        try:
            if var.ui.chkEfec.isChecked():
                var.pay.append('Efectivo')
            if var.ui.chkTarj.isChecked():
                var.pay.append('Tarjeta')
            if var.ui.chkTrans.isChecked():
                var.pay.append('Transferencia')
        except Exception as error:
            print('Error: %s ' % str(error))

    def cargarProv():
        '''
        carga las provincias al iniciar el programa
        '''
        '''
        esta solución es provisional en su momento lo hremos de otra forna
        cargando los registros desde una base de datos
        '''
        try:
            prov = ['','A Coruña','Lugo','Ourense','Pontevedra']
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error: %s ' % str(error))

    def selProv(prov):
        try:
            var.vpro = prov
            return prov
        except Exception as error:
            print('Error: %s' % str(error))

    '''
        Abrir la ventana calendario
    '''
    def abrirCalendar(self):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error: %s ' % str(error))

    '''
        Este módulo se ejecuta cuando clickeamos en un día del calendar, es decir, clicked.connect de calendar
    '''

    def cargarFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.editCliAlta.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error cargar fecha: %s ' % str(error))

    def showClientes(self):
        #cargará los clientes de la tabla
        try:
            #preparamos el registro
            newcli = []
            clitab = [] #será lo que carguemos en la tabla
            client = [var.ui.editDni, var.ui.editCliAlta, var.ui.editApel, var.ui.editNombre, var.ui.editDireccion]
            k = 0
            for i in client:
                newcli.append(i.text()) #cargamos los valores que hay en los editline
                if k < 3:
                    clitab.append(i.text)
                    k += 1
            newcli.append(var.vpro)
            var.pay = set(var.pay) #elimina duplicados
            for j in var.py:
                newcli.append(j)
            newcli.append(var.sex)
            print(newcli)
            print(clitab)
            #aqui empieza como trabajar con la TableWidget
            row = 0
            column = 0
            var.ui.tablaCli.insertrow(row)
            for registro in clitab:
                cell = QtWidgets.QTableWidgetItem(registro)
                var.ui.tablaCli.setItem(row, column, cell)
                column += 1
        except Exception as error:
            print('Error cargar fecha: %s ' % str(error))