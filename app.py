import numpy as np


class digit:

    def __init__(self):
        self.frames = np.load('data/digits.npy')

    def get_digit(self, n):

        if n is 0:
            return np.repeat(self.frames[:, :, 0], len(str(n)))

        num_digit = len(str(n))
        print(n)
        print("NUM Digits: ", num_digit)

        result_frame = np.empty([5, 0], dtype=np.int8)

        n = int(n)

        for i in range(num_digit):
            digit = n % 10
            print(digit)
            result_frame = np.hstack([self.frames[:, :, digit], result_frame])
            n = n // 10

        return result_frame

    def get_spacer(self, width=2):
        spacer = np.zeros([5, width], dtype=np.int8)
        return spacer

    def __del__(self):
        del self.frames
