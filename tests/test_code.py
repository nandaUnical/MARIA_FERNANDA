import pytest
#import code
import sys 
sys.path.insert(1,'C:/Users/hp/Documents/!Master/Agile/!!Second Apello/MARIA_FERNANDA\app_code')


def test_read_text_path_folder () :
    a = read_text (r"C:\Users\hp\Documents\!Master\Agile\!!Second Apello\ejemplos")
    assert a == {'hola': 4, 'mundo': 3, 'gente': 2, 'la': 1}

def test_read_text_list_files () :
    a = read_text ([r"C:\Users\hp\Documents\!Master\Agile\!!Second Apello\ejemplos\texto_1.txt", r"C:\Users\hp\Documents\!Master\Agile\!!Second Apello\ejemplos\texto_2.txt", r"C:\Users\hp\Documents\!Master\Agile\!!Second Apello\ejemplos\texto_3.txt"])
    assert a == {'hola': 4, 'mundo': 3, 'gente': 2, 'la': 1}