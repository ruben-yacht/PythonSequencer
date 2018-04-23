from SoundFile import SoundFile
from Sequencer import Sequencer

if __name__ == "__main__":
    # the path to your sound file
    sound = SoundFile("hello-world.wav")

    # sequencer takes a SoundFile as an argument; a list with the sequence; and the tempo in beats per minute (default 120)
    seq = Sequencer(sound,[1])

    # number of times to play. 0 = infinite. CTRL+C to quit program.
    seq.play(3)
