import os
import numpy
import matplotlib.pyplot as plt

from PIL import Image

class Img_transforms:
    def __fft_edge_detector():
        pass

    def __circular_section():
        pass




class Face_Img:

    def __init__(self, path:str, model_params: list) -> None:
        img_path: str = path
        img_as_array: numpy.ndarray = self._get_image_as_array(self.img_path)
        transformed_img: numpy.ndarray = self._apply_transformation()
        image_FV: numpy.ndarray = self.transformed_img.flatten()

    def _get_image_as_array(self, pth: str) -> numpy.ndarray:
        im = Image.open(pth)
        im = im.convert(mode="L")
    
        arr = numpy.asarray(im)

        return arr

    def _apply_transformation(self) -> numpy.ndarray:
        arr = []
        return arr

