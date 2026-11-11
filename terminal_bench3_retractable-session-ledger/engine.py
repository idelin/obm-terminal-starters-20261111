class SessionEngine:
    def __init__(self, gap, lateness, partitions):
        self.gap, self.lateness = gap, lateness
        self.watermarks = dict.fromkeys(partitions, -1)
        self.events = {}
        self.revision = 0
    def apply(self, op):
        if op['op'] == 'put': self.events[op['id']] = dict(op)
        elif op['op'] == 'remove': self.events.pop(op['id'], None)
        elif op['op'] == 'advance': self.watermarks[op['partition']] = op['time']
        return {'emitted': []}
    def snapshot(self):
        return dict(gap=self.gap, lateness=self.lateness, watermarks=self.watermarks, events=self.events, revision=self.revision)
    @classmethod
    def restore(cls, state):
        obj = cls(state['gap'], state['lateness'], list(state['watermarks']))
        obj.watermarks, obj.events, obj.revision = state['watermarks'], state['events'], state['revision']
        return obj
    def view(self): return []
