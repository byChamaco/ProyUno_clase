from PyQt5 import QtSql
import pymongo, var
from ventana import *

class Conexion():
    def db_connect(filename):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(str(filename))
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'No se puede establecer conexión, \n'
                                           'Haz click para Cancelar', QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexión establecida')
        return True

    def altaCli(cliente):
        query = QtSql.QSqlQuery()
        query.prepare(
            'insert into clientes (dni, apellidos, nombre, fechalta, direccion, provincia, sexo, formaspago, edad)'
            'VALUES (:dni, :apellidos, :nombre, :fechalta, :direccion, :provincia, :sexo, :formaspago, :edad)')
        query.bindValue(':dni', str(cliente[0]))
        query.bindValue(':apellidos', str(cliente[1]))
        query.bindValue(':nombre', str(cliente[2]))
        query.bindValue(':fechalta', str(cliente[3]))
        query.bindValue(':direccion', str(cliente[4]))
        query.bindValue(':provincia', str(cliente[5]))
        query.bindValue(':sexo', str(cliente[6]))
        # pagos = ' '.join(cliente[7]) si quiesesemos un texto, pero nos viene mejor meterlo como una lista
        query.bindValue(':formaspago', str(cliente[7]))
        query.bindValue(':edad', int(cliente[8]))
        if query.exec_():
            print("Inserción Correcta")
            var.ui.lblstatus.setText('Alta Cliente con dni ' + str(cliente[0]))
            Conexion.mostrarClientes(None)
        else:
            print("Error: ", query.lastError().text())

    def cargarCliente():
        '''
        Módulo que carga el resto de widgets con los datos del cliente dni
        :return: None
        '''
        dni = var.ui.editDni.text()
        query = QtSql.QSqlQuery()
        query.prepare('select * from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            while query.next():
                var.ui.lblCodcli.setText(str(query.value(0)))
                var.ui.editClialta.setText( query.value(4))
                var.ui.editDir.setText(query.value(5))
                var.ui.cmbProv.setCurrentText(str(query.value(6)))
                if str(query.value(7)) == 'Mujer':
                    var.ui.rbtFem.setChecked(True)
                    var.ui.rbtMasc.setChecked(False)
                else:
                    var.ui.rbtMasc.setChecked(True)
                    var.ui.rbtFem.setChecked(False)
                for data in var.chkpago:
                    data.setChecked(False)
                if 'Efectivo' in query.value(8):
                    var.chkpago[0].setChecked(True)
                if 'Tarjeta' in query.value(8):
                    var.chkpago[1].setChecked(True)
                if 'Transferencia' in query.value(8):
                    var.chkpago[2].setChecked(True)
                var.ui.spinEdad.setValue(int(query.value(9)))

    def mostrarClientes(self):
        '''
        Carga los datos principales del cliente en la tabla
        se ejecuta cuando lanzamos el programa, actualizamos, insertamos y borramos un cliente
        :return: None
        '''
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre from clientes')
        if query.exec_():
            while query.next():
                #cojo los valores
                dni = query.value(0)
                apellidos = query.value(1)
                nombre = query.value(2)
                # crea la fila
                var.ui.tablaCli.setRowCount(index+1)
                #voy metiendo los datos en cada celda de la fila
                var.ui.tablaCli.setItem(index,0, QtWidgets.QTableWidgetItem(dni))
                var.ui.tablaCli.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tablaCli.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                index += 1
        else:
            print("Error mostrar clientes: ", query.lastError().text())

    def bajaCli(dni):
        ''''
        modulo para eliminar cliente. se llama desde fichero clientes.py
        :return None
        '''
        query = QtSql.QSqlQuery()
        query.prepare('delete from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            print('Baja cliente')
            var.ui.lblstatus.setText('Cliente con dni '+ dni + ' dado de baja')
        else:
            print("Error mostrar clientes: ", query.lastError().text())


    def modifCli(codigo, newdata):
           ''''
           modulo para modificar cliente. se llama desde fichero clientes.py
           :return None
           '''
           query = QtSql.QSqlQuery()
           codigo = int(codigo)
           query.prepare('update clientes set dni=:dni, apellidos=:apellidos, nombre=:nombre, fechalta=:fechalta, '
                         'direccion=:direccion, provincia=:provincia, sexo=:sexo, formaspago=:formaspago, edad=:edad where codigo=:codigo')
           query.bindValue(':codigo', int(codigo))
           query.bindValue(':dni', str(newdata[0]))
           query.bindValue(':apellidos', str(newdata[1]))
           query.bindValue(':nombre', str(newdata[2]))
           query.bindValue(':fechalta', str(newdata[3]))
           query.bindValue(':direccion', str(newdata[4]))
           query.bindValue(':provincia', str(newdata[5]))
           query.bindValue(':sexo', str(newdata[6]))
           query.bindValue(':formaspago', str(newdata[7]))
           query.bindValue(':edad', int(newdata[8]))

           if query.exec_():
               print('Cliente modificado')
               var.ui.lblstatus.setText('Cliente con dni '+ str(newdata[0]) + ' modificado')
           else:
               print("Error modificar cliente: ", query.lastError().text())

    def buscaCli(dni):
        """
        select un cliente a partir de su dni.
        :return:
        """
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select * from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            while query.next():
                var.ui.lblCodcli.setText(str(query.value(0)))
                var.ui.editApel.setText(str(query.value(1)))
                var.ui.editNombre.setText(str(query.value(2)))
                var.ui.editClialta.setText(query.value(4))
                var.ui.editDir.setText(query.value(5))
                var.ui.cmbProv.setCurrentText(str(query.value(6)))
                if str(query.value(7)) == 'Mujer':
                    var.ui.rbtFem.setChecked(True)
                    var.ui.rbtMasc.setChecked(False)
                else:
                    var.ui.rbtMasc.setChecked(True)
                    var.ui.rbtFem.setChecked(False)
                for data in var.chkpago:
                    data.setChecked(False)
                if 'Efectivo' in query.value(8):
                    var.chkpago[0].setChecked(True)
                if 'Tarjeta' in query.value(8):
                    var.chkpago[1].setChecked(True)
                if 'Transferencia' in query.value(8):
                    var.chkpago[2].setChecked(True)
                var.ui.spinEdad.setValue(query.value(9))

                var.ui.tablaCli.setRowCount(index + 1)
                    # voy metiendo los datos en cada celda de la fila
                var.ui.tablaCli.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(1))))
                var.ui.tablaCli.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(2))))
                var.ui.tablaCli.setItem(index, 2, QtWidgets.QTableWidgetItem(str(query.value(3))))


    #Conexión de los PRODUCTOS con la base de datos

    def altaPro(producto):
        query = QtSql.QSqlQuery()
        query.prepare(
            'insert into articulos (nombre, precio_unidad,stock)'
            'VALUES (:nombre, :precio_unidad, :stock)')
        query.bindValue(':nombre', str(producto[0]))
        producto[1] = producto[1].replace(',',',')
        query.bindValue(':precio_unidad', round(float(producto[1]),2))
        query.bindValue(':stock', int(producto[2]))
        if query.exec_():
            print("Inserción Correcta")
            var.ui.lblstatus.setText('Alta Producto con nombre ' + str(producto[0]))
            Conexion.mostrarProductos(None)
        else:
            print("Error conexion alta: ", query.lastError().text())

    def cargarProducto(cod):

        query = QtSql.QSqlQuery()
        query.prepare('select nombre, precio-unidad, stock from articulos where codigo = :cod')
        query.bindValue(':cod', cod)
        if query.exec_():
            while query.next():
                var.ui.lblCodPro.setText(str(cod))
                var.ui.editNomPro.setText(str(query.value(0)))
                var.ui.editPreUni.setText(str(query.value(1)))
                var.ui.editStock.setText(str(query.value(2)))

    def mostrarProductos():
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select codigo, nombre, precio_unidad from articulos')
        if query.exec_():
            while query.next():
                codigo = query.value(0)
                nombre = query.value(1)
                precio_unidad = query.value(2)
                var.ui.tablaPro.setRowCount(index+1)
                var.ui.tablaPro.setItem(index, 0, QtWidgets.QTableWidgetItem(codigo))
                var.ui.tablaPro.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                var.ui.tablaPro.setItem(index, 2, QtWidgets.QTableWidgetItem(precio_unidad))
                index += 1
        else:
            print("Error mostrar productos: ", query.lastError().text())

    def bajaProd(cod):
        query = QtSql.QSqlQuery()
        query.prepare('delete from articulos where codigo = :cod')
        query.bindValue(':cod', cod)
        if query.exec_():
            print('Baja producto')
            var.ui.lblstatus.setText('Producto con nombre '+ cod + ' dado de baja')
        else:
            print("Error baja conexion productos: ", query.lastError().text())
        Conexion.mostrarProductos()

    def modifProd(cod, newdataprod):
        cod = int(cod)
        query = QtSql.QSqlQuery()
        query.prepare('update articulos set nombre=:nombre, precio_unidad=:precio_unidad, stock=:stock where codigo=:cod')
        query.bindValue(':cod', int(cod))
        query.bindValue(':nombre', str(newdataprod[0]))
        newdataprod[1] = newdataprod[1].replace(',',',')
        query.bindValue(':precio_unidad', round(float(newdataprod(1)),2))
        query.bindValue(':stock', int(newdataprod[2]))
        if query.exec_():
            print('Producto modificado')
            var.ui.lblstatus.setText('Producto con código '+ str(cod) + ' modificado')
        else:
            print("Error modificar producto: ", query.lastError().text())

'''
conexión base de datos MongoDB
'''
# class Conexion():
#     HOST = 'localhost'
#     PORT =  '27017'
#     URI_CONNECTION = 'mongodb://' + HOST + ':' + PORT + '/'
#     var.DATABASE = 'empresa'
#     try:
#         print('Conexion realizada al servidor %s' %HOST)
#     except:
#         print('Error conexión')