class Logger:
    def __init__(self):
        self.default_timestamp_duration = 10
        self.message_dict = {} # {[message: string]: number}

    def message_exists(self, message):
        return message in self.message_dict
    
    def get_timestamp(self, message):
        return self.message_dict[message] if self.message_exists(message) else -1
    
    def set_message(self, msg, ts):
        self.message_dict[msg] = ts + self.default_timestamp_duration

    def add_message(self, msg, ts):
        if self.get_timestamp(msg) <= ts:
            self.set_message(msg, ts)
            return True
        return False


    def shouldPrintMessage(self, timestamp: int, message: str):
        ans  =self.add_message(message, timestamp)
        print('Success --> ', ans)
        return ans
    

################### test


"""
foo, 1



foo 3
"""


logger = Logger()
logger.shouldPrintMessage(1, 'foo')
logger.shouldPrintMessage(2, 'abc')
logger.shouldPrintMessage(2, 'foo')
logger.shouldPrintMessage(11, 'foo')











