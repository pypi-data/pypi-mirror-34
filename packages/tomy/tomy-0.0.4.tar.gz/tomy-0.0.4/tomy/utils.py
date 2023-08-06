
# common error parsing in drf
class TResp(object):
    data = {}
    def __init__(self, status,message):
        self.status_code = status
        self.message     = message
    def gen_resp(self):
        re = {
            "message" : self.message,
            "status"  : self.status_code
        }
        resp = {
            "err" : re,
            "data" : self.data
        }
        return resp