import pytest
from basic_filter import Filter
filter = Filter()

def test_same_place():
    assert filter.Do_it_close('https://www.sefaria.org.il/Ruth.3.9',
                              'https://www.sefaria.org.il/Ruth.3.8') == True
    assert filter.Do_it_close('https://www.sefaria.org.il/Ruth.3.9',
                              'https://www.sefaria.org.il/Ruth.2.8') == False
    assert filter.Do_it_close('https://www.sefaria.org.il/genesis.3.9',
                              'https://www.sefaria.org.il/Ruth.3.9') == False

def test_pirush_on_text():
    assert filter.Do_it_close('https://www.sefaria.org.il/Rashi_on_Genesis.2.2.1',
                              'https://www.sefaria.org.il/Genesis.2.2') == True
    assert filter.Do_it_close('https://www.sefaria.org.il/Genesis.2.2',
                              'https://www.sefaria.org.il/Rashi_on_Genesis.2.2.1') == True
    assert filter.Do_it_close('https://www.sefaria.org.il/Rashi_on_Genesis.2.2.1',
                              'https://www.sefaria.org.il/Genesis.2.3') == False
    assert filter.Do_it_close('https://www.sefaria.org.il/Rashi_on_Genesis.2.2.1',
                              'https://www.sefaria.org.il/Genesis.3.2') == False
    assert filter.Do_it_close('https://www.sefaria.org.il/Rashi_on_Genesis.2.2.1',
                              'https://www.sefaria.org.il/devarim.3.2') == False

