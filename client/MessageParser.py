import json

class MessageParser():
    def __init__(self):

        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            'message': self.parse_message,
            'history': self.parse_history
        }   

    def parse(self, payload):
        payload = json.loads(payload)

        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            print "Invalid message from server: ",payload
    

    def parse_error(self, payload):
        print "Error from ", payload['sender'], " @ ",payload['timestamp'],": ", payload['content']
    
    def parse_info(self, payload):
        print "Info from ", payload['sender'], " @ ",payload['timestamp'],": ", payload['content']

    def parse_message(self, payload):
        print "Message from ", payload['sender'], " @ ",payload['timestamp'],": ", payload['content']

    def parse_history(self, payload):
        list_hist = payload.get('content')
        print "History of previous sent messages:\n"
        for n in list_hist:
            n = json.loads(list_hist)
            parse_message(n)

    def parse_send(self, request, content):
        if (request == "login") or (request == "msg") or (request == "names") or(request == "help"):        
            data = {'request':<request>,
                    'content':<content>
                    }
            return json.dumps(data)
        else:
            print "Invalid request!"


    
