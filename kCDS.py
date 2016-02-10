import krpc
import serial
import time
SerialPort='COM4'
conn = krpc.connect(name='Example')
vessel=conn.space_center.active_vessel

port=serial.Serial(SerialPort,115200)

value = port.readline()
deBounce={}
deBounce['stage']=1
stageDebounceT=time.time()
def handleRawReads(raw):
    value=raw.replace('\r\n','').split(',')
    if len(value) == 18:
        retVal={}
        retVal['pitch']=(float(value[-1])-512)/1024
        retVal['yaw']=(float(value[-2])-512)/1024
        retVal['stage']=int(value[11])
        #print retVal
        return retVal
while True:
    try:
        vessel=conn.space_center.active_vessel
        value = port.readline()
        control=handleRawReads(value)
        if control!=None:
            if control['stage'] and deBounce['stage']:
                vessel.control.activate_next_stage()#stage
                deBounce['stage']=False
            elif not control['stage']:
                if stageDebounceT==0:
                    stageDebounceT=time.time()+.2
                elif time.time()>stageDebounceT:
                    stageDebounceT=0
                    deBounce['stage']=1
            vessel.control.pitch=(control['pitch'])
            vessel.control.yaw=(control['yaw'])
        time.sleep(.001)
    except:
        print 'not able to control'
        time.sleep(.2)
    
