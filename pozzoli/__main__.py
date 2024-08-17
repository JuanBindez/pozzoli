import time
import pygame

class Metronome:
    def __init__(self, bpm=60, time_signature='4/4', sound_file='click.wav'):
        """
        Initializes the metronome with BPM (beats per minute), time signature, and a sound file.
        
        :param bpm: Beats per minute (default: 60)
        :param time_signature: Time signature in the format '4/4'
        :param sound_file: Path to the sound file that will be played on each beat
        """
        self.bpm = bpm
        self.time_signature = self.parse_time_signature(time_signature)
        self.beats_per_bar = self.time_signature[0]
        self.beat_note = self.time_signature[1]
        self.sound_file = sound_file
        self.rhythm_patterns = {
            '♩': 1,        # Quarter note
            '♪': 0.5,      # Eighth note
            '♫': 2,        # Half note
            '𝅝': 4,        # Whole note
            ' ': 0         # Rest
        }
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(self.sound_file)

    def parse_time_signature(self, time_signature):
        """
        Converts the time signature string in the format '4/4' to a tuple (beats_per_bar, beat_note).
        
        :param time_signature: String in the format '4/4'
        :return: Tuple with beats_per_bar and beat_note
        """
        try:
            beats_per_bar, beat_note = map(int, time_signature.split('/'))
            return (beats_per_bar, beat_note)
        except ValueError:
            raise ValueError("Invalid time signature format. Use '4/4', '3/4', '6/8', etc.")

    def play_sound(self):
        """
        Plays the metronome sound.
        """
        self.sound.play()

    def play_rhythm(self, rhythm_sequence):
        """
        Executes a rhythm sequence based on the time signature and BPM.

        :param rhythm_sequence: List of rhythm patterns (e.g., ['♩', '♩', '♪', '♪', '♩'])
        """
        tempo_per_beat = 60 / self.bpm  # Duration of each beat in seconds
        
        for rhythm in rhythm_sequence:
            duration_factor = self.rhythm_patterns.get(rhythm, None)
            if duration_factor is None:
                raise ValueError(f"Invalid rhythm pattern '{rhythm}'.")
            
            if duration_factor > 0:
                self.play_sound()

            note_duration = tempo_per_beat * duration_factor
            time.sleep(note_duration)

    def display_rhythm_sequence(self, rhythm_sequence):
        """
        Displays the rhythm sequence in the terminal, with rhythm symbols.

        :param rhythm_sequence: List of rhythm patterns
        """
        rhythm_line = ""
        for rhythm in rhythm_sequence:
            rhythm_line += f"{rhythm} "
        
        print(rhythm_line.strip())
        print('---' * len(rhythm_sequence))  # Visual separator for clarity

    def start(self, rhythm_sequence, repetitions=1):
        """
        Starts the metronome with a defined rhythm sequence and repeats it a specified number of times.

        :param rhythm_sequence: List of rhythm patterns to be played
        :param repetitions: Number of times to repeat the sequence (default: 1)
        """
        try:
            for _ in range(repetitions):
                self.display_rhythm_sequence(rhythm_sequence)
                self.play_rhythm(rhythm_sequence)
        except KeyboardInterrupt:
            print("Metronome stopped.")
