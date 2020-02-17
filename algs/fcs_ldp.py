from algs.sketch_ldp import SketchLDP


class FCSLDP(SketchLDP):
    def __init__(self, data, error_p, confidence, privacy):
        super(FCSLDP, self).__init__(data, error_p, confidence, privacy)

    def get_frequency_estimation(self):
        pass
