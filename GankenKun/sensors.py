import numpy as np
import pybullet as p

from scipy import signal


class PressureSensor:
    def __init__(self, name, joint_index, body_index, cutoff, order):
        self.joint_index = joint_index
        self.name = name
        self.body_index = body_index
        nyq = 1000 * 0.5  # nyquist frequency from simulation frequency
        normalized_cutoff = cutoff / nyq  # cutoff freq in hz
        self.filter_b, self.filter_a = signal.butter(
            order, normalized_cutoff, btype='low')
        self.filter_state = signal.lfilter_zi(self.filter_b, 1)
        self.unfiltered = 0
        self.filtered = [0]

    def filter_step(self):
        self.unfiltered = p.getJointState(
            self.body_index, self.joint_index)[2][2]
        self.filtered, self.filter_state = signal.lfilter(self.filter_b, self.filter_a, [self.unfiltered],
                                                          zi=self.filter_state)

    def get_force(self):
        return max(self.unfiltered, 0), max(self.filtered[0], 0)
