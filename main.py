import os
from parser import Signal

"""
Main method.

Runs on startup
"""
if __name__ == "__main__":
    directory = 'test_signals'

    # iterate through example signals
    for filename in os.listdir(directory):
        filename = os.path.join(directory, filename)

        with open(filename, 'r') as f:
            # convert each signal to an object using the parser.Signal class.
            signal = Signal(f.read())
            print(signal.to_json()) # print json format.



