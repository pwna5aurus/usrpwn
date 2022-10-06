#This is the NiceGUI frontend to USRPwn, a portable touch-screen friendly interface for GNURadio python scripts
#Inputs: none
#Returns: none

from nicegui import ui

def usrp_function(fn_name):
    if fn_name == "Jammers":
        select2 = ui.select(["Wifi 2.4ghz", "Bluetooth","Wifi 5ghz"])
    if fn_name == "Capture":
        select2 = ui.select(["Capture stuff","capture other stuff"])
    if fn_name == "Replay":
        select2 = ui.select(["Replay farts", "Replay shid", "Replay piss"])
    return



ui.label('Welcome to USRPwn').style('font-size: x-large')
select1 = ui.select({1: "Jammers", 2: "Capture", 3: "Replay"}, value=1).style('font-size: x-large')
#select2 = ui.select({1: 'One', 2: 'Two', 3: 'Three'}).bind_value(select1, 'value')
select2 = ui.select({1:["1","2","3"], 2:[4,5,6]}, value=1).bind_visibility_from(select1, 'value')


ui.run()
