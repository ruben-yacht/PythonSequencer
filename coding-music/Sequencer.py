from RepeatedTimer import RepeatedTimer
import time

class SequencerException(BaseException):
    pass

class Sequencer:
    def __init__(self, sound, sequence=[0], bpm=120):
        self._sound = sound
        if len(sequence) > 0:
            self._sequence = sequence
        else:
            raise SequencerException("please provide a sequence as a list with length > 0.")
        self._repetitions = 0
        self._sequence_index = 0
        self._repetitions_played = 0
        self._bpm = bpm
        self._interval = self.bpm_to_interval(self.bpm)
        self._timer = RepeatedTimer(self._interval, self.execute_sequence_index)

    @property
    def sound(self):
        return self._sound

    @sound.setter
    def sound(self, sound):
        self._sound = sound

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        if len(sequence) > 0:
            self._sequence = sequence
        else:
            raise SequencerException("please provide a sequence as a list with length > 0.")

    @property
    def bpm(self):
        return self._bpm

    @bpm.setter
    def bpm(self,bpm):
        self._bpm = bpm

    def bpm_to_interval(self, bpm):
        # translates to 1/16th notes
        return 15/bpm

    def play(self,repetitions):
        self._repetitions = repetitions
        self._timer.start()
        print(self._sound.path, "started")

    def stop(self):
        self._timer.stop()

    def execute_sequence_index(self):
        if(self.sequence[self._sequence_index] == 1):
            self._sound.play()
            print(self._sound.path,1)
        else:
            print(self._sound.path,0)

        self._sequence_index += 1
        if self._sequence_index >= len(self._sequence):
            self._sequence_index = 0
            self._repetitions_played += 1
            if(self._repetitions_played == self._repetitions and self._repetitions != 0):
                print(self._sound.path, "ended")
                self.stop()
                self._sound.wait_done()
