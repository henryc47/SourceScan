from random_string_detector import RandomStringDetector

detector = RandomStringDetector(allow_numbers=True,uncommon_bigrams_threshold=0.3,common_bigrams_threshold=0.2)
sample_API_key = "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"

def detect_in_line(line):
    try:
        if detector(line):
            return True
        else:
            return False
    except:
        return False

detection_message = "WARNING : Possible API_key detected ->"