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
# The purpose of this supplement is to provide a place where the comparison between the orthodox, *frequentist*, statistical approach and the current, *probability theory as logic*, approach is made explicit.  It is my contention that all of the typical examples covered in introductory statistics can be handled as equivalent examples in probability with uninformative prior probabilities on the parameters.  I want this supplement to provide all of the derivations for this claim.
# 
# Further, examples where the approaches are *different*, I plan I showing that the current approach is demonstrably superior.  I also want to include computer code and data to make clear how the current approach can be practically accomplished.
# 
# 
# [Statistical Inference for Everyone]: http://web.bryant.edu/~bblais/statistical-inference-for-everyone-sie.html
# 
# 
# Contents
# ------
# 
# 
# * [**Prologue:**](http://nbviewer.ipython.org/github/bblais/Tech-SIE/blob/master/Prologue/Prologue.ipynb) What is this document?
# * [**Introduction:**](http://nbviewer.ipython.org/github/bblais/Tech-SIE/blob/master/Introduction/Introduction.ipynb) A little history, and introduction to the perspective taken in the book.
# * [**Mean, Known Deviation:**](http://nbviewer.ipython.org/github/bblais/Tech-SIE/blob/master/Estimating_Mean_Known_Deviation/Estimating_Mean_Known_Deviation.ipynb) Where we estimate the mean (i.e. true value), knowing the deviation.
# * [**Mean and the Deviation:**](http://nbviewer.ipython.org/github/bblais/Tech-SIE/blob/master/Estimating_Mean_and_Deviation/Estimating_Mean_and_Deviation.ipynb) Where we estimate both the mean (i.e. true value) and the deviation (i.e. uncertainty).
# * [**Proportion:**](http://nbviewer.ipython.org/github/bblais/Tech-SIE/blob/master/Estimating_Proportion/Estimating_Proportion.ipynb) Where we estimate a proportion, couched in the iconic problem of $N$ coin flips where $h$ of the flips come up heads.
# * [**Difference Between Means:**](http://nbviewer.ipython.org/github/bblais/Tech-SIE/blob/master/Estimating_Difference_Between_Means/Estimating_Difference_Between_Means.ipynb) Where we look at the difference between means, both paired and unpaired.
# * [**Ratio of Variances:**](http://nbviewer.ipython.org/github/bblais/Tech-SIE/blob/master/Estimating_Ratio_Deviations/Estimating_Ratio_Deviations.ipynb) Where we look at the ratio of variances, or deviations.
# * **Difference Between Proportions**
# * **Goodness of Fit**
# * [**Linear Regresssion:**](http://nbviewer.ipython.org/github/bblais/Tech-SIE/blob/master/Linear_Regression/Linear_Regression.ipynb) Where we introduce the simple form of linear regression, and derive the posteriors for the slope and intercept.
# * **Objective Priors**

# <markdowncell>

# ---------------------

# <codecell>

from IPython.core.display import HTML


def css_styling():
    styles = open("../styles/custom.css", "r").read()
    return HTML(styles)
css_styling()

