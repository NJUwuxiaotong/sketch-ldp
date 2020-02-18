from algs.sketch_ldp import SketchLDP


class FASLDP(SketchLDP):
    def __init__(self, data, error_p, confidence, privacy, att_num):
        super(FASLDP, self).__init__(data, error_p, confidence, privacy,
                                     att_num)

    def get_frequency_estimation(self):
        pass
