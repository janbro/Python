import sys
sys.path.insert(0, "../lib")
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class SampleListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE); 


    def on_frame(self, controller):
        frame = controller.frame()

        if len(frame.gestures()):
            print "Gesture recognized"
        #print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

def main():
    #while True:
    listener = SampleListener()
    controller =  Leap.Controller()

    controller.add_listener(listener)
    while True:
        continue
        

if __name__ == "__main__":
    main()
