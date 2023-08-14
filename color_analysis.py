import pandas as pd
from PIL import Image
from collections import Counter


def analyze_colors(image):
    img = Image.open(image)
    img = img.convert('RGB')
    img_data = list(img.getdata())

    color_counter = Counter(img_data)
    sorted_colors = color_counter.most_common()

    colors_df = pd.DataFrame(sorted_colors, columns=['color', 'count'])
    return colors_df.to_dict(orient='records')
