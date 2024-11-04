from random_string_detector import RandomStringDetector

detector = RandomStringDetector(allow_numbers=True,uncommon_bigrams_threshold=0.3,common_bigrams_threshold=0.2)

def detect_in_line(line):
    try:
        if detector(line):
            return True
        else:
            return False
    except:
        return False

detection_message = "WARNING : Possible API_key detected ->"