from SoundFile import SoundFile
from Sequencer import Sequencer

if __name__ == "__main__":

    # in simplified music notation, usually x = sound, o = no sound
    x = 1
    o = 0

    # the path to your sound file
    sf1 = SoundFile("../sound/drums/1-kick/kick-allaboutyou-1.wav")

    # sequencer takes a SoundFile as an argument; a list with the sequence; and the tempo in beats per minute (default 120)
    sq1 = Sequencer(sf1,[x,o,o,o,x,o,o,o],9.4)

    # number of times to play. 0 = infinite
    sq1.play(10)

    # have fun!
