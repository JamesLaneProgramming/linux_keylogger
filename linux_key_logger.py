import pyxhook
import time

class event_log:
    '''
    Description
    -----------
    This class contains all information about the event that is recorded.
    
    Methods
    -------
    __init__:
    getEventInfo:
    isRepeat:
    isMistake:
    '''
    def __init__(self, event, **optional_parameters):
        '''
        Initialses the keyPress class with
        Arguments
        ---------
        event:
            The event that requires logging.
        last_event:
            Optional argument for use in a linked list or other linked data
            structures.
        repress_messages:
            Optional argument determining whether this class throws messages to stdout.
        '''
        self.event = event
        self.time_of_event = time.time()
        for each_optional_parameter in optional_parameters:
            if each_optional_parameter == 'repress_messages':
                self.repress_messages = optional_parameters['repress_messages']
            if each_optional_parameter == 'last_event':
                self.last_event = optional_parameters['last_event']
    def __str__(self):
        return self.event

    def get_event_info():
        return self

    def is_repeat(self):
        try:
            return True if self.event == self.last_event.event else False
        except:
            print """last_event was not given as a paramenter. Although
            optional, last_event is required for this method to work as
            expected"""
    def is_mistake(self):
        pass

log_file='/root/projects/KeyLoggerGraphs/logs/keysLoggerResults.log'

programStartTime = time.time()
print('program initiated at {0}'.format(programStartTime))

keyStats = list()

def OnKeyPress(event):
    event_log_instance = None
    if len(keyStats) == 0:
        event_log_instance = event_log(event)
    else:
        event_log_instance = event_log(event, keyStats[-1])
    keyStats.append(event_log)
    #print(str(event_log_instance.isRepeat()))
    fob=open(log_file,'a')
    
    fob.write(event_log_instance.__str__())
    fob.write('[delimeter]')
    if event.Ascii==96: #96 is the ascii value of the grave key (`)   
        fob.close()
        new_hook.cancel()

def main():
    new_hook=pyxhook.HookManager()

    new_hook.KeyDown=OnKeyPress

    new_hook.HookKeyboard()

    new_hook.start()

if __name__ == '__main__':
    main()

