import contextlib
import sys
from pyke import knowledge_engine
from pyke import krb_traceback
import PySimpleGUI as sg
sg.theme("LightBlue7")
anemia= [

    [sg.Text("Are you suffering from fatigue? (y/n)")],
    [sg.InputText(key="fatigue")],
    
    [sg.Text("Do you have pallor? (y/n)")],
    [sg.InputText(key = "pallor")],
    
        [sg.Text("Do you have any of the following symptoms?\n\n1:Desire for non edible material \
        2:Suffer from lack of concentration \
        3:Have dry skin \
        4:Thin hair \
        5:Suffer from poor weight gain \
        6:All of the above \
        7:None of the above")],
    [sg.InputText(key = "iron")],
    
    [sg.Text("Do you consume iron rich food (liver) less than 4 times per month? (y/n)")],
    [sg.InputText(key = "liver")],
    

      [sg.Text("Do you have any of the following symptoms?\n\n1:Do you have diarrhea?\
        2:Do you have tongue redness or hotness or pain? \
        3:Do you experience tingling sensations in your hands or legs?\
        \n\n4:Do you consume goats' milk frequently ? \
        5:All of the above \
        6:None of the above")],
      [sg.InputText(key = "Folic")],
        #---------------------------------------
        [sg.Text("Do you have any of the following symptoms?\n\n1:Do you have an enlarged liver or spleen or both? \
        2:Do you have yellowish discoloration of your skin? \
        3:Do you have leg ulcers? \
        \n\n4:Do you require frequent blood transfusion? \
        5:Was any of your family members diagnosed with thalassemia? \
        6:All of the above \
        7:None of the above ")],
    [sg.InputText(key = "Thalassemia")],
                #---------------------------------------

        [sg.Text("Do you have any of the following symptoms?\n\n    1:Do you have a history of frequent repeated infections within a short period of time ?\
        2:Did you recently suffer from any form of bleeding following a minor incident?\
        3:Do you have thumb anomalies since birth? \
        \n\n4:Do you have drooping eyelids? \
        5:Do you suffer from hearing loss and/or any ear anomalies?\
        6:All of the above\
        7:None of the above")],
    [sg.InputText(key = "Fanconi")],
    
    [sg.Submit(),sg.Cancel()]
]

window = sg.Window("anemia",anemia,resizable=True)

event,value = window.read()
file = open("A&A.txt","w")
print(value)
for i in value:
    file.write(str(value[i])+'\n')

file.close()
window.close()
engine = knowledge_engine.engine(__file__)



def bc_test_questions():

    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('rules') #STUDENTS: you will need to edit the name of your rule file here
    print("Please Answer The Following Questions :) ")
    lst=list()
    try:
        with engine.prove_goal('rules.what_to_bring($bring)') as gen: #STUDENTS: you will need to edit this line
            for vars, plan in gen:
                lst.append(("Report: %s" % (vars['bring']))) #STUDENTS: you will need to edit this line

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("Done!")
    return lst



sys.stdin=open("A&A.txt")
x = bc_test_questions()
s=""
for i in x:
    s += str(i)+'\n\n'
sg.popup(s)