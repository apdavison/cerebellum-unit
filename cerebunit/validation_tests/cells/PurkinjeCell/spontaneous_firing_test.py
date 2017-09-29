# ============================================================================
# spontaneous_firing_test.py
#
# created  14 August 2017 Lungsi
# modified 31 August 2017 Lungsi
#
# ============================================================================

import os

import sciunit
import quantities as pq
from elephant.statistics import mean_firing_rate as mfr
from cerebunit.file_manager import get_folder_path_and_name as gfpan
from cerebunit.score_manager import BinaryScore
from cerebunit.capabilities.cells.response import ProducesSpikeTrain


class SpontaneousFiringTest(sciunit.Test, BinaryScore):
    '''
    The Spontaneous Firing Test is a test comparing the observed spiking frequency in real animal to those generated by the model. This is done by comparing the mean spike frequencies.
    '''
    required_capabilities = (ProducesSpikeTrain,)
    score_type = BinaryScore

    #def __init__(self):
    #    path_to_folder, folder_name = gfpan()
    #    # as inherited from sciunit by default name is the class name
    #    self.name = "Spontaneous Firing Test for " + folder_name
    #    self.description = "This tests the spontaneous firing test observed in real adult " + folder_name + ". This is done by comparing the mean spike frequency of the model against experimentally observed levels."
    #    # also inherited from sciunit but assuming observation is in json
    #    self.observation = {"mean":None, "error":None}

    def generate_prediction(self, model, verbose=False):
        '''
        fdf
        '''
        setup_parameters = { "dt": 0.025,   "celsius": 37,
                             "tstop": 100, "v_init": -65 }
        model.set_simulation_properties(setup_parameters)
        model.produce_spike_train()
        self.process_prediction(model)
        return model

    def process_prediction(self, model):
        '''
        afd
        '''
        model_mean_firing_rates = {}
        for cell_region in model.cell_regions:
            x = mfr(model.predictions["spike_train"][cell_region])
            a_firing_rate = {cell_region: [x, x.rescale(pq.Hz)]}
            model_mean_firing_rates.update(a_firing_rate)
        #
        self.processed_prediction = model_mean_firing_rates
        #self.prediction = self.processed_prediction["vm_soma"][1]


    def validate_observation(self, observation, first_try=True):
        '''
        fdfd
        '''
        pass

    def compute_score(self, observation, model, verbose=False):
        '''
        fdfd
        '''
        a_prediction = self.processed_prediction["vm_soma"][1]
        x = BinaryScore.compute( observation,
                                 a_prediction  )
        score = BinaryScore(x)
        score.description = "The spontaneous firing test defined by the mean firing rate of the model = " + str(a_prediction) + " compared against the observed experimental data " + str(observation) + " has the BinaryScore = " + str(score)
        return score
        #computed_scores = {}
        #for cell_region in model.cell_regions:
        #    a_prediction = self.processed_prediction[cell_region][1]
        #    a_binary = BinaryScore.compute( a_prediction,
        #                                    observation )
        #    a_score = {cell_region: BinaryScore(a_binary.score)}
        #    computed_scores.update(a_score)


