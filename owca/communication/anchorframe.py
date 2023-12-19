import json
from TagFrame import TagFrame


class AnchorFrame:
    def __init__(self, tagFrame, anchorID, rssi, tagID, ts):
        self.tagFrame = tagFrame
        self.anchorID = anchorID
        self.rssi = rssi
        self.tagID = tagID
        self.ts = ts
        
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=5)
        
    @staticmethod
    def from_json(jsonMessage):
        tagFrameFromJson = TagFrame(**json.loads(jsonMessage)['tagFrame'])
        anchorIDFromJson = json.loads(jsonMessage)['anchorID']
        rssiFromJson = json.loads(jsonMessage)['rssi']
        tagIDFromJson = json.loads(jsonMessage)['tagID']
        tsFromJson = json.loads(jsonMessage)['ts']
        return AnchorFrame(tagFrameFromJson,anchorIDFromJson,rssiFromJson,tagIDFromJson,tsFromJson)
    
    def to_csv_line(self):
        return f"{self.anchorID}, {self.rssi}, {self.tagID}, {self.ts}, " + self.tagFrame.to_csv_line()
        
        
       
