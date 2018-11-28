#! /usr/bin/env python

from create_publication_list import output_formatted_entry, MDbold, MDheader, MDlink, MDstrikethrough

def test_list_entry_generation():
    assert output_formatted_entry('Vedder E, McCready MD, Gossard SC, Irons JS', 'Do The Evolution', 'Yield', '1998', '10.1371/epic.pj.0186', '0101100101') == ('1998', '**Do The Evolution**. Vedder et al. *Yield*. 10.1371/epic.pj.0186. [0101100101](https://www.ncbi.nlm.nih.gov/pubmed/?term=0101100101)')

def test_MDbold():
    assert MDbold('Something in bold') == '**Something in bold**'

def test_MDheader():
    assert MDheader('Top-level header', 1) == '# Top-level header'

def testMDlink():
    assert MDlink('link text', 'http://qwantz.com/index.php?comic=3371') == '[link text](http://qwantz.com/index.php?comic=3371)'

def testMDstrikethrough():
    assert MDstrikethrough('something no longer true') == '~~something no longer true~~'
