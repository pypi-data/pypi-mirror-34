__author__ = 'Xsank'
from thinkutils_plus.eventbus.listener import Listener
from thinkutils_plus.eventbus.listener import add_event

from myevent import GreetEvent
from myevent import ByeEvent

class MyListener(Listener):
    @add_event(GreetEvent)
    def greet(self,event=None):
        print 'hello',event.name

    @add_event(GreetEvent)
    def greet2(self,event=None):
        print 'hi',event.name

    @add_event(ByeEvent)
    def goodbye(self,event=None):
        print 'bye',event.name


