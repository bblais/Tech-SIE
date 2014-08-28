# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Statistical Inference for Everyone: Technical Supplement
# 
# 
# 
# This document is the technical supplement, for instructors, for [Statistical Inference for Everyone], the introductory statistical inference textbook from the perspective of "probability theory as logic".
# 
# <img  src="http://web.bryant.edu/~bblais/images/Saturn_with_Dice.png" align=center width = 250px />
# 
# [Statistical Inference for Everyone]: http://web.bryant.edu/~bblais/statistical-inference-for-everyone-sie.html

# <markdowncell>

# The purpose of this supplement is to provide a place where the comparison between the orthodox, *frequentist*, statistical approach and the current, *probability theory as logic*, approach is made explicit.  It is my contention that all of the typical examples covered in introductory statistics can be handled as equivalent examples in probability with uninformative prior probabilities on the parameters.  I want this supplement to provide all of the derivations for this claim.
# 
# Further, examples where the approaches are *different*, I plan I showing that the current approach is demonstrably superior.  I also want to include computer code and data to make clear how the current approach can be practically accomplished.

# <codecell>


# <markdowncell>

# ---------------------

# <codecell>

from IPython.core.display import HTML


def css_styling():
    styles = open("../styles/custom.css", "r").read()
    return HTML(styles)
css_styling()

