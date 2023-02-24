import random
import streamlit as st
import pandas as pd
import numpy as np
import csv
from PIL import Image

st.title("Category 12")

 # Load the data from the CSV file
with open('merged_dataset.csv', 'r') as csv_file:
    data_reader = csv.reader(csv_file)
    next(data_reader, None)  # Skip header row
    category = []
    for row in data_reader:
        if row[0] == '12':
            category.append(row[1:])


def generate_image(row_num, data):
    # Set the size of the image
    image_size = (28, 28)

    # Create a new image for the selected row
    image = Image.new('L', image_size)

    # Set the pixel values for the image
    pixels = image.load()
    for i in range(image_size[0]):
        for j in range(image_size[1]):
            pixel_value = int(data[row_num][i*image_size[0]+j])
            pixels[j, i] = pixel_value

    # Return the image
    return image

def four_image_gen():
    # Select 4 random rows from the data
    num_images = 4
    random_rows = random.sample(category, num_images)

    # Create columns in Streamlit
    cols = st.columns(num_images)

    # Display an image in each column for each random row
    for i, row in enumerate(random_rows):
        image = generate_image(i, random_rows)
        cols[i].image(image, width=150)

four_image_gen()
if st.button("Display other products like this"):
    four_image_gen()
