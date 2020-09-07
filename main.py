#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import sys
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

class Book:
    book = None
    book_lines = 0
    now_line = 0
    is_read_finished = False
    def __init__(self, path):
        with open(path, "r") as f:
            self.book = f.read()
            self.book = self.book.splitlines()
            self.book_lines = len(self.book)
        print("Conplete Reading file, line_len:{}".format(self.book_lines))
        print(self.book)
    def update_line(self):
        if self.now_line >= self.book_lines - 1:
            self.is_read_finished = True
        else:
            self.now_line += 1
    def get_text(self):
        if not self.is_read_finished:
            return [self.book[self.now_line], False]
        else:
            return ["Finished Reading text.\n prease finish program", True]

    def make_image(self, font_path="./font.ttf"):
        text, is_finished = self.get_text()
        if is_finished:
            print(text)
            exit(0)
        image = np.zeros((400, 400))
        font = ImageFont.truetype(font_path, 48)
        pil_image = Image.fromarray(image)
        draw = ImageDraw.Draw(pil_image)
        draw.text((50, 100), text, fill=(255), font=font)
        image= np.asarray(pil_image)
        #image = cv2.putText(image, text, (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255), thickness=2)
        return image
    def print_image(self):
        image = self.make_image()


def main(file_name, update_time):
    book = Book(file_name)
    UPDATE_TIME = update_time
    cv2.startWindowThread()
    print("Opening Window...")
    time.sleep(1)
    last_time = time.time() + 1
    while True:
        now = time.time()
        if now - last_time > UPDATE_TIME:
            book.update_line()
            last_time = now
        image = book.make_image()
        cv2.imshow("Text Window", image)
        cv2.imwrite("image.jpg", image)
        cv2.waitKey(1)
        #cv2.destroyAllWindows()


if __name__ == '__main__':
    if len(sys.argv) > 2:
        file_name = sys.argv[1]
        update_time = float(sys.argv[2])
    else:
        print("usage: python main.py \"path_to_textfile\" UPDATE_TIME")
        exit(1)
    main(file_name, update_time)
