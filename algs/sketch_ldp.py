import abc


class SketchLDP(object):
    def __init__(self, data, error_p, confidence, privacy, att_num):
        self.data = data
        self.error_p = error_p
        self.confidence = confidence
        self.privacy = privacy
        self.att_num = att_num

    @abc.abstractmethod
    def get_frequency_estimation(self):
        pass
