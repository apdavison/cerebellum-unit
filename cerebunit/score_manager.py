# ============================================================================
# score_manager.py
#
# created 21 September 2017 Lungsi
# modified
#
# This py-file contains custum score functions initiated by
#
# from cerebuint import score_manager
# ============================================================================

import sciunit


# ==========================BinaryScore=======================================
# created 21 September 2017 Lungsi
class BinaryScore(sciunit.Score):
    '''
    A Binary Score.
    0 if the prediction is not in the interval of the measurement within a margin of error (epsilon).
    '''

    #def __init__(self):
    #    pass

    @classmethod
    def compute(self, prediction=None, measurement=None, epsilon=10**(-3)):
        # mesurement is in dictionary form whose value has
        # magnitude and python quantity
        # default epsilon = 10**(-3)
        if len(measurement.keys()) > 1:
            for key in measurement:
                if key=="error":
                    epsilon = measurement[key]
                else:
                    amount = measurement[key]
            # Then
            if amount-epsilon <= prediction <= amount+epsilon:
                self.score = 1
            else:
                self.score = 0
        else:
            # For only one key
            for key in measurement:
                if measurement[key]-epsilon <= prediction \
                        <= measurement[key]+epsilon:
                    self.score = 1
                else:
                    self.score = 0
        return self.score

    _description = ( "The BinaryScore gives a score of 0 or 1 based on the comparison between prediction vs. measurement. "
                   + "The prediction is a python quantities, i.e, it is in the form of array(x.x) * <some_unit>. "
                   + "The measurement is also a python quantity, but in dictionary form. "
                   + "If the measurement has only 1-key, its value is the one that is the reference. "
                   + "The predicted value is then compared against the measurement with margin of error given by a default epsilon value. "
                   + "Therefore, BinaryScore checks that the predicted value is inside the interval. "
                   + "If it is not it, a score-0 is given. "
                   + "If the measurement has an addition error-key its value is the epsilon.")

    @property
    def sort_key(self):
        return self.score

    def __str__(self):
        return "BinaryScore is " + str(self.score)
# ============================================================================
#
# ==========================Score=============================================
class NameHereScore(sciunit.Score):
    '''
    text
    '''

    def __init__(self):
        pass
# ============================================================================