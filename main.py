from pozzoli import Metronome


from pozzoli import Metronome

rhythm_sequence = ['♩', '♪', '♪', '♩', '♪', '♪']
metronome = Metronome(bpm=120, time_signature='6/8')
metronome.start(rhythm_sequence, repetitions=3)



rhythm_sequence2 = ['♩', '♩', '♪', '♪', '♩', '♩']
metronome2 = Metronome(bpm=90, time_signature='4/4')
metronome2.start(rhythm_sequence2, repetitions=5)
