ZERO_LEN = len('abcefg')
ONE_LEN = len('cf')
TWO_LEN = len('acdeg')
FOUR_LEN = len('bcdf')
SEVEN_LEN = len('acf')
EIGHT_LEN = len('abcdefg')


total_output = 0
with open("input.txt") as f:
    for line in f:
        signals_and_outputs = line.rstrip().split(" | ")
        signals = signals_and_outputs[0].split()
        outputs = signals_and_outputs[1].split()

        digit_to_signal = {}
        signal_to_digit = {}
        zero_six_nine = []
        two_three_five = []
        for signal in signals:
            sorted_signal = "".join(sorted(signal))
            signal_length = len(sorted_signal)
            if signal_length == ONE_LEN:
                digit_to_signal[1] = sorted_signal
                signal_to_digit[sorted_signal] = 1
            elif signal_length == FOUR_LEN:
                digit_to_signal[4] = sorted_signal
                signal_to_digit[sorted_signal] = 4
            elif signal_length == SEVEN_LEN:
                digit_to_signal[7] = sorted_signal
                signal_to_digit[sorted_signal] = 7
            elif signal_length == EIGHT_LEN:
                digit_to_signal[8] = sorted_signal
                signal_to_digit[sorted_signal] = 8
            # Zero, six, and nine all have the same number of segments
            elif signal_length == ZERO_LEN:
                zero_six_nine.append(sorted_signal)
            # Two, three, and five all have the same number of segments
            elif signal_length == TWO_LEN:
                two_three_five.append(sorted_signal)

        for signal in zero_six_nine:
            sorted_signal = "".join(sorted(signal))
            # Nine is similar to four
            if digit_to_signal[4][0] in sorted_signal and digit_to_signal[4][1] in sorted_signal and digit_to_signal[4][2] in sorted_signal and digit_to_signal[4][3] in sorted_signal:
                digit_to_signal[9] = sorted_signal
                signal_to_digit[sorted_signal] = 9
            # Zero is similar to seven
            elif digit_to_signal[7][0] in sorted_signal and digit_to_signal[7][1] in sorted_signal and digit_to_signal[7][2] in sorted_signal:
                digit_to_signal[0] = sorted_signal
                signal_to_digit[sorted_signal] = 0
            # The other one must be six
            else:
                digit_to_signal[6] = sorted_signal
                signal_to_digit[sorted_signal] = 6

        for signal in two_three_five:
            sorted_signal = "".join(sorted(signal))
            # Three is similar to seven
            if digit_to_signal[7][0] in sorted_signal and digit_to_signal[7][1] in sorted_signal and digit_to_signal[7][2] in sorted_signal:
                digit_to_signal[3] = sorted_signal
                signal_to_digit[sorted_signal] = 3
            # Five is most similar to nine
            elif len(set(digit_to_signal[9]).symmetric_difference(set(sorted_signal))) == 1:
                digit_to_signal[5] = sorted_signal
                signal_to_digit[sorted_signal] = 5
            # Two is left over
            else:
                digit_to_signal[2] = sorted_signal
                signal_to_digit[sorted_signal] = 2

        output_str = ""
        for output in outputs:
            output_str += str(signal_to_digit["".join(sorted(output))])
        total_output += int(output_str)

print(total_output)

