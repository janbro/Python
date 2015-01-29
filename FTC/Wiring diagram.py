inp = """#pragma config(Hubs,  S1, HTMotor,  HTServo,  HTMotor,  HTMotor)
#pragma config(Motor,  mtr_S1_C1_1,     driveRight,    tmotorTetrix, openLoop)
#pragma config(Motor,  mtr_S1_C1_2,     lift,          tmotorTetrix, openLoop)
#pragma config(Motor,  mtr_S1_C3_1,     driveLeft,     tmotorTetrix, openLoop)
#pragma config(Motor,  mtr_S1_C3_2,     intake,        tmotorTetrix, openLoop)
#pragma config(Motor,  mtr_S1_C4_1,     liftMotor3,    tmotorTetrix, openLoop)
#pragma config(Servo,  srvo_S1_C2_1,    fieldGrabberRight,    tServoStandard)
#pragma config(Servo,  srvo_S1_C2_2,    fieldGrabberLeft,     tServoStandard)
#pragma config(Servo,  srvo_S1_C2_3,    scoopBridge,          tServoStandard)
#pragma config(Servo,  srvo_S1_C2_4,    rampBridge,          tServoStandard)
"""

class Controller:
    def __init__(self,module,port,appendages):
        self.type = module
        self.port = port
        self.appendages = appendages

class Appendage:
    def __init__(self,module,port,name):
        self.type = module
        self.port = port
        self.name = name

pragmas = inp.split("\n")
hubs = []
    
for line in pragmas:
    if len(line) == 0:
        continue
    whatIs = line.split("(")[1]


    if whatIs.startswith("Hubs"):
        port = whatIs.split(",")[1]
        for cont in whatIs.split(","):
            cont = cont.strip(" ")
            if cont.startswith("HTMotor") or cont.startswith("HTServo"):
                hubs.append(Controller(cont.strip(" ").strip(")"),port,list()))


    if whatIs.startswith("Motor") or whatIs.startswith("Servo") or whatIs.startswith("Sensor"):
        print "Attachment"
        
print pragmas

for g in hubs:
    print g.type
    print g.appendages
