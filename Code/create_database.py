import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

def make_img_same_dimension(dimx, dimy):
    acipenseridae_imgs = os.fsencode("../Fish Photos/Actinopterygii/Acipenseriformes/Acipenseridae (Sturgeons)/")
    polyodontidae_imgs = os.fsencode("../Fish Photos/Actinopterygii/Acipenseriformes/Polyodontidae (Paddlefishes)/")
    albulidae_imgs = os.fsencode("../Fish Photos/Actinopterygii/Albuliformes/Albulidae (Bonefish)/")
    amiidae_imgs = os.fsencode("../Fish Photos/Actinopterygii/Amiiformes/Amiidae (Bowfins)/")
    ateleopodidae_imgs = os.fsencode("../Fish Photos/Actinopterygii/Ateleopodiformes/Ateleopodidae (Jellynose Fishes)/")
    atherinopsidae_imgs = os.fsencode("../Fish Photos/Actinopterygii/Atheriniformes/Atherinopsidae (Silversides)/")
    alepisauridae_imgs = os.fsencode("../Fish Photos/Actinopterygii/Aulopiformes/Alepisauridae (Lancetfish)/")
    aulopidae_imgs = os.fsencode("../Fish Photos/Actinopterygii/Aulopiformes/Aulopidae (Flagfish)/")
    synodontidae_imgs = os.fsencode("../Fish Photos/Actinopterygii/Aulopiformes/Synodontidae (Lizardfish)/")
    batrachoididae_imgs = os.fsencode("../Fish Photos/Actinopterygii/Batrachoidiformes/Batrachoididae (Toadfish)/")
    belonidae_imgs = os.fsencode("../Fish Photos/Actinopterygii/Beloniformes/Belonidae (Needlefish)/")
    exocoetidae_imgs = os.fsencode("../Fish Photos/Actinopterygii/Beloniformes/Exocoetidae (Flyingfish)/")
    anoplogastridae_imgs = os.fsencode("../Fish Photos/Actinopterygii/Bercyiformes/Anoplogastridae (Fangtooth)/")
    proscyllidae_imgs = os.fsencode("../Fish Photos/Chondrichthyes/Carcharhiniformes/Proscyllidae (Finback Catshark)/")
    ceratodontidae_imgs = os.fsencode("../Fish Photos/Chondrichthyes/Ceratodontiformes/Ceratodontidae (Australian Lungfish)/")
    chimaeridae_imgs = os.fsencode("../Fish Photos/Chondrichthyes/Chimaeriformes/Chimaeridae (Shortnose chimaeras)/")

    for file in os.listdir(acipenseridae_imgs):
        filename = os.fsdecode(file)
        image = cv2.imread("../Fish Photos/Actinopterygii/Acipenseriformes/Acipenseridae (Sturgeons)/" + filename)
        print(filename)
        b, g, r = cv2.split(image)
        print(filename)
        rgb_img = cv2.merge([r,g,b])
        resized_img = cv2.resize(rgb_img, (dimx, dimy))
        plt.imshow(resized_img)
        plt.show()
    return
make_img_same_dimension(150,150)

        