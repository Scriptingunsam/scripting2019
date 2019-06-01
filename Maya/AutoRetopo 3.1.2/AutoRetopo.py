#!/usr/bin/python
# -*- coding: latin-1 -*-
# C5-Scr Manuel Jofre Poza TP2

# Importar
import maya.cmds as cmds
import os

# definir 
winID = 'manuUI'
ver = '3.1.2'

estaCarpeta = os.path.abspath(__file__).split('.')[0] + '.png'

  
def defaultBooleanPush(*args):
    cmds.polyCBoolOp(op=1, n='result')    
    print 'boolean action'
    
def boolenUnionPush(*args):
    cmds.PolygonBooleanUnionOptions()
    print 'boolenUnionPush pushed.'

def boolenDiffPush(*args):
    cmds.PolygonBooleanDifferenceOptions()
    print 'boolenDiffPush pushed.'

def boolenInterPush(*args):
    cmds.PolygonBooleanIntersectionOptions()
    print 'boolenInterPush pushed.'
    
def reMeshPush(*args): 
    confirmA = cmds.confirmDialog( title='Re-Mesh', message='Re-Mesh reconstruye la geometria seleccionada en Triangulos\n\nesta acción puede tomar mucho tiempo en un mesh con errores o demasiados poligonos',  button=['Continuar','Detener'], defaultButton='Continuar', cancelButton='Detener', dismissString='No' )
    if confirmA == "Continuar":
        cmds.polyRemesh()        
    else:
        print "Re-Mesh cancelado"
        return() 
    
    print 'remeshPush pushed.'
    
def reTopoPush(*args):  
    confirmB = cmds.confirmDialog( title='Re-Topo', message='Re-Topo funciona mejor despues de hacer un Re-Mesh\n\nesta accion puede tomar mucho tiempo en un mesh con errores o demasiados poligonos', messageAlign='center',  button=['Continuar','Detener'], defaultButton='Continuar', cancelButton='Detener', dismissString='No' )
    if confirmB == "Continuar":
        cmds.polyRetopo()        
    else:
        print "Re-Topo cancelado"
        return() 
    
    print 'reTopoPush pushed.'
    
def borrarHistPush(*args):
    cmds.DeleteHistory(ch=True)
    print 'borrarHistPush pushed.'

# construir ventana
cmds.window(title='Auto Retopo v'+ver)

# elemento principal de ventana
columnMain = cmds.columnLayout()

# primer sub elemento de ventana
cmds.image(image=estaCarpeta, width=272, annotation='version '+ver, p=columnMain)

# segundo sub elemento de ventana
elementosBoo = cmds.rowLayout(numberOfColumns=4, p=columnMain)
cmds.button(label="Fusionar Elementos", align='center', width=160, command=defaultBooleanPush, annotation='Conbina elementos usando boleanos', p=elementosBoo)
cmds.iconTextButton( style='iconOnly', command=boolenUnionPush, image1='polyBooleansUnion.xpm', annotation='ver opciones de BooleanUnion', p=elementosBoo )
cmds.iconTextButton( style='iconOnly', command=boolenDiffPush, image1='polyBooleansDifference.xpm', annotation='ver opciones de BooleanDiference', p=elementosBoo )
cmds.iconTextButton( style='iconOnly', command=boolenInterPush, image1='polyBooleansIntersection.xpm', annotation='ver opciones de BooleanIntersection', p=elementosBoo )

# tercer sub elemento de ventana
elementosRe = cmds.rowLayout(numberOfColumns=2, p=columnMain)
cmds.button(label="Re-Mesh", height=50, width=134, command=reMeshPush, annotation='Genera nueva geometria en Triangulos', p=elementosRe)
cmds.separator(p=columnMain)
cmds.button(label="Re-Topo", height=50, width=134, command=reTopoPush, annotation='Regenera la topologia en Quads', p=elementosRe)
cmds.separator(p=columnMain)

# cuarto sub elemento de ventana
cmds.button(label="Borrar Historial", width=272, command=borrarHistPush, annotation='elimina el historial del elemento', p=columnMain)
cmds.helpLine(width=272, p=columnMain)

cmds.showWindow()