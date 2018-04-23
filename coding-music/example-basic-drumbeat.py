from SoundFile import SoundFile
from Sequencer import Sequencer

if __name__ == "__main__":
    x = 1
    o = 0

    sf1 = SoundFile("../sound/drums/1-kick/kick-allaboutyou-1.wav")
    sq1 = Sequencer(sf1,[x,o,o,o,x,o,o,o])
    sq1.play(10)

    sf2 = SoundFile("../sound/drums/4-hihat/closedhh-allaboutyou.wav")
    sq2 = Sequencer(sf2,[x,o,x,o,x,o,x,o])

    sq2.play(10)

    sf3 = SoundFile("../sound/drums/3-snare/snare-allaboutyou.wav")
    sq3 = Sequencer(sf3,[o,o,o,o,x,o,o,o])
    sq3.play(10)
