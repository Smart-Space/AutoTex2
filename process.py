import torch
import numpy as np
from PIL import ImageStat, ImageOps

from texteller import load_model, load_tokenizer, img2latex

import data

device=None
model=None
tokenizer=None

# !!!write your own model_dir here!!!
model_dir = './model'

def _load_model():
    global device, model, tokenizer
    device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
    data.device=device
    model = load_model(model_dir)
    model = model.to(device)
    tokenizer = load_tokenizer(model_dir)
    data.root.event_generate("<<ModelLoaded>>")

def process_img():
    if model is None or tokenizer is None:
        return
    img=data.orimg.convert("RGB")
    if data.reverse == 0:
        # 自动判断
        image=img.convert("L")
        mean_pixel=int(ImageStat.Stat(image).mean[0])
        histogram=image.histogram()
        dark_pixels=sum(histogram[:mean_pixel])
        light_pixels=sum(histogram[mean_pixel:])
        if dark_pixels > light_pixels:
            img=ImageOps.invert(img)
            data.root.event_generate("<<ImageInverted>>")
        else:
            data.root.event_generate("<<ImageNotInverted>>")
    elif data.reverse == 1:
        img=ImageOps.invert(img)
    img = np.array(img)
    data.latexstring=img2latex(model, tokenizer, [img,], device, 'katex')[0]
    data.root.event_generate("<<ImageProcessed>>")
