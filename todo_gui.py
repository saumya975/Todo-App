import PySimpleGUI as sg
import todoFunctions

label=sg.Text("Type in a To-do")
input_box=sg.InputText(tooltip="Enter Todo")
add_btn=sg.Button("Add")
window=sg.Window("My To-do App", layout=[[label],[input_box,add_btn ]])
window.read()
window.close()