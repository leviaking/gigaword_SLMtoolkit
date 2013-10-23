gigaword_SLMtoolkit
===================

These tools are for using the CMU SLM toolkit (Carnegie Mellon University Statistical Language Modeling toolkit) to train an ngram language model on the English Gigaword corpus.

You can download the SLM toolkit for free here: http://www.speech.cs.cmu.edu/SLM/toolkit.html

I used the English Gigaword Corpus, 3rd Edition, which can be found here: http://catalog.ldc.upenn.edu/LDC2007T07 . It's not free, but if you're interested in this you're probably part of a university or institution with access to it anyway.

I'm fairly confident this would work with other editions of the English Gigaword Corpus, too. However, if the format of the metadata/SGML tags varies in the other editions, that could pose a problem. If that's the case, the python script here called "gigaword_for_SLM_preprocess.py" would need to be modified, but that should be easy enough.
