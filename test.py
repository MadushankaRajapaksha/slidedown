from slidedown.core import slice_slides
import os

def test_slice_slide():
    slides = open("README.md", "r", encoding="utf-8").read()
    print(slice_slides(slides))

if __name__ == "__main__":
    test_slice_slide()
    