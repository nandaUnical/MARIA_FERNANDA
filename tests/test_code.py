import pytest
import code

def test_read_text_path_folder () :
    a = code.read_text (r"C:\Users\hp\Documents\!Master\Agile\!!Second Apello\ejemplos")
    assert a == {}

def test_read_text_list_files ()
    a = code.read_text ([r"C:\Users\hp\Documents\!Master\Agile\!!Second Apello\ejemplos\texto_1.txt", r"C:\Users\hp\Documents\!Master\Agile\!!Second Apello\ejemplos\texto_2.txt", r"C:\Users\hp\Documents\!Master\Agile\!!Second Apello\ejemplos\texto_3.txt"])
    assert a == {}