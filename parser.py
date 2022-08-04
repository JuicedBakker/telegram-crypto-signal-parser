import re
import requests
regex_number_filter = r"\s([+-]?[0-9]*[.]?[0-9]{2,})\s"

tickers = requests.get("https://api.binance.com/api/v1/exchangeInfo").json()
symbols = []
[symbols.append(x["symbol"]) for x in tickers['symbols']]

class Signal:
    # constructor
    def __init__(self, signal):
        self.signal = signal
        self.is_valid = True
        self.entries = []
        self.targets = []
        self.stop_loss = []
        self.symbol = ''

    def get_symbol(self):
        return self.symbol

    def get_entry(self):
        return self.entries

    def get_stop_loss(self):
        return self.stop_loss

    def get_targets(self):
        return self.targets

    # translates class attributes into json format.
    def to_json(self):
        signal_json = {}
        signal_json['symbol'] = self.symbol
        signal_json['entry'] = self.entries
        signal_json['targets'] = self.targets
        signal_json['stop_loss'] = self.stop_loss
        return signal_json

    # parses the signal to find entry, target and stop loss values.
    def parse_signal(self):
        filtered_signal = self.signal.replace(' ','').replace('/','').upper()

        # abstract the symbol from the signal.
        first_3_lines = filtered_signal.split('\n')[:3]
        string_to_parse = ''.join(first_3_lines)
        self.symbol = ""
        for symbol in symbols: # check whether a known symbol exists in signal.
            if symbol in string_to_parse:
                self.symbol = symbol

        if self.symbol == "":
            self.is_valid = False
            return

        # split the signal on blank lines
        new_signal = self.signal.split('\n\n')
        if len(new_signal) == 1:
            # if no blank lines exist, split single lines
            new_signal = self.signal.split('\n')

        # container for stop loss, entry and targets.
        group = []
        for section in new_signal:
            # blank character at end of section to aid regex pattern matches.
            section += " "

            cleaned_section = section.replace("$", " ").replace("-", "  ")
            r1 = re.findall(
                regex_number_filter,
                cleaned_section,
                flags=re.MULTILINE
                )
            if len(r1):
                # container for one of the 3 subgroups
                subgroup = []
                for x in r1:
                    subgroup.append(float(x))
                group.append(subgroup)
        group = sorted(group, key=sum)
        self.entries = group[1]
        self.targets = group[2]
        self.stop_loss = group[0]