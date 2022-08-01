import os
from parser import Signal

if __name__ == "__main__":
    directory = 'test_signals'

    for filename in os.listdir(directory):
        filename = os.path.join(directory, filename)

        with open(filename, 'r') as f:
            signal = Signal(f.read())
            print(signal.to_json())



