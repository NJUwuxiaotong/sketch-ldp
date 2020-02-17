import abc


class SketchLDP(object):
    def __init__(self, data, error_p, confidence, privacy):
        self.data = data
        self.error_p = error_p
        self.confidence = confidence
        self.privacy = privacy

    @abc.abstractmethod
    def get_frequency_estimation(self):
        pass
