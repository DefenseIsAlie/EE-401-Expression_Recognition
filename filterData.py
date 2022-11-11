import os

def _filter_data():
    TEST_PATH = "data/validation/"
    cls  = os.listdir(TEST_PATH)
    for i in range(len(cls)):
        imgs = os.listdir(TEST_PATH+cls[i])
        l = len(imgs)
        print(l)
        if l > 100:
            for img in imgs[100:]:
                path = TEST_PATH + cls[i] + "/" + img
                #os.remove(path)


    TRAIN_PATH = "data/train/"

    cls  = os.listdir(TRAIN_PATH)

    for i in range(len(cls)):
        imgs = os.listdir(TRAIN_PATH+cls[i])
        l = len(imgs)
        print(l)
        if l > 100:
            for img in imgs[700:]:
                path = TRAIN_PATH + cls[i] + "/" + img
                #os.remove(path)

if __name__ == '__main__':
    _filter_data()