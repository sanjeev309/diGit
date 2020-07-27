import pickle
import numpy as np
from PIL import Image


class digit:

    def __init__(self):
        self.digits = np.load('data/digits.npy')
        self.symbols = np.load('data/symbols.npy')
        self.symbol_dict = pickle.load(open('data/symbol_dict.pkl', "rb"))

    def digitize(self, s, scale = 1):
        digit_group = s.split('.')

        if len(digit_group) > 1:
            digit_group.insert(1, str('.'))
            # digit_group.insert({i for i in range(1,len(digit_group),2)}, str('.'))

        print(digit_group)
        digitised = np.empty([5, 0], dtype=np.uint8)

        for chunk in digit_group:
            print("Chunk:", chunk)
            digitised = np.hstack([digitised, self.get_digit(chunk)])

            # if len(digit_group) > 1:
            #     digitised = np.hstack([digitised, self.get_symbols('.')])
        digitised = digitised.resize((digitised.shape[0] * scale,digitised.shape[1] * scale))

        digitised = (digitised * 255).astype(np.uint8)



        digitised = Image.fromarray(digitised, 'L')

        return digitised

    def get_digit(self, n):

        result_frame = np.empty([5, 0], dtype=np.uint8)

        if n in self.symbol_dict:
            return self.get_symbols(n)


        if n is 0:
            return np.repeat(self.digits[:, :, 0], len(str(n)))

        if isinstance(n, str):
            n = int(n)

        negative = False

        if n < 0:
            negative = True
            # result_frame.show()
            n = n * -1

        num_digit = len(str(n))

        n = int(n)

        for i in range(num_digit):
            digit = n % 10
            print(digit)
            result_frame = np.hstack([self.digits[:, :, digit], result_frame])
            n = n // 10

        if negative:
            result_frame = np.hstack([self.get_symbols('-'), result_frame])

        # img = Image.fromarray(result_frame, 'L')
        return result_frame

    def get_symbols(self, sym):
        if sym in self.symbol_dict:
            print("Sym: ", sym)

            symbol = self.symbols[:, :, self.symbol_dict[sym]]
            return symbol

        else:
            print("Spacer")
            return self.get_spacer()

    def get_spacer(self, width=2):
        spacer = np.zeros([5, width], dtype=np.uint8)
        spacer = (spacer * 255).astype(np.uint8)
        spacer_img = Image.fromarray(spacer, 'L')
        return spacer_img

    def __del__(self):
        del self.digits
        del self.symbols
        del self.symbol_dict


if __name__ == '__main__':
    d = digit()
    res = d.digitize('-1234.4')
    res.show()
