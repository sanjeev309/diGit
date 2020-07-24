import numpy as np
from PIL import Image


class digit:

    def __init__(self):
        self.frames = np.load('data/digits.npy')

    def get_digit(self, n):

        if n is 0:
            return np.repeat(self.frames[:, :, 0], len(str(n)))

        num_digit = len(str(n))

        result_frame = np.empty([5, 0], dtype=np.uint8)

        n = int(n)

        for i in range(num_digit):
            digit = n % 10
            result_frame = np.hstack([self.frames[:, :, digit], result_frame])
            n = n // 10

        result_frame = (result_frame * 255).astype(np.uint8)

        img = Image.fromarray(result_frame, 'L')
        return img

    def get_spacer(self, width=2):
        spacer = np.zeros([5, width], dtype=np.uint8)
        spacer = (spacer * 255).astype(np.uint8)
        spacer_img = Image.fromarray(spacer, 'L')
        return spacer_img

    def __del__(self):
        del self.frames

if __name__ == '__main__':
    d = digit()
    res = d.get_digit(1234)
    res.show()
