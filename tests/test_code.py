import pytest
import code

def test_read_text_path_folder () :
    a = read_text (r"C:\Users\hp\Documents\!Master\Agile\!!Second Apello\ejemplos")
    assert if a , 'Diccionary is empty'