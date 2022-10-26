from volo import volo_d1
import numpy as np
import mindspore
from mindspore import Tensor

# mindspore.set_context(mode=mindspore.PYNATIVE_MODE)
def test():
    net = volo_d1()
    # print(net)
    print("\n")

    input = Tensor(np.random.rand(5, 3, 224, 224), dtype=mindspore.float32)
    print("input shape:", input.shape)
    print("\n")
    output = net(input)
    return output

if __name__ == '__main__':
    output = test()
    print("output shape:", output.shape)