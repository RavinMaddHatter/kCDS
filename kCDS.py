import krpc
import serial
import time
import thread
import Queue 
SerialPort='COM3'
baude=115200
conn = krpc.connect(name='Example')
vessel=conn.space_center.active_vessel




deBounce={}
deBounce['stage']=1
stageDebounceT=time.time()
def handleRawReads(raw):
    value=raw.replace('\r\n','').split(',')
    if len(value) == 25:
        retVal={}
        retVal['digital']=map(int,value[0:14])
        
        for line in value[14:]:
            line=line.split(':')
            retVal[line[0]]=(float(line[1])-512)/1024
        retVal['Stage']=retVal['digital'][13]
        #print retVal['Yaw']
        return retVal
    else:
        print 'fail'
def accessControls(portNo,Baude,controlQue,dataQue):
    running=True
    port=serial.Serial(portNo,Baude)
    value = port.readline()
    while running:
        value = port.readline()
        control=handleRawReads(value)
        dataQue.put(control)
        if not controlQue.empty():
            command= controlQue.get()
            controlQue.put(command)
            running=False
        time.sleep(.001)
def controlLoop(controlQue,dataQue):
    running=True
    deBounce['Stage']=True
    while running:
        control=dataQue.get()
        vessel.control.pitch=(control['Pitch'])
        vessel.control.yaw=(control['Yaw'])
        if control['Stage'] and deBounce['Stage']:
            vessel.control.activate_next_stage()#stage
            deBounce['Stage']=False
        elif not control['Stage']:
            deBounce['Stage']=True
        if not controlQue.empty():
            command= controlQue.get()
            controlQue.put(command)
            running=False
controlQue=Queue.Queue()
dataQue=Queue.Queue()
thread.start_new_thread( accessControls, (SerialPort,baude,controlQue,dataQue) )
thread.start_new_thread( controlLoop, (controlQue,dataQue) )
while True:
    try:
        val='true'
    except KeyboardInterrupt:
        controlQue.put('quit')
        vessel=conn.space_center.active_vessel
        print 'not able to control'
        time.sleep(.2)
port.close()
