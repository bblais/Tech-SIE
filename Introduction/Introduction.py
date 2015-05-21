
# coding: utf-8

# #Statistical Inference for Everyone: Technical Supplement
# 
# 
# 
# This document is the technical supplement, for instructors, for [Statistical Inference for Everyone], the introductory statistical inference textbook from the perspective of "probability theory as logic".
# 
# <img  src="http://web.bryant.edu/~bblais/images/Saturn_with_Dice.png" align=center width = 250px />
# 
# [Statistical Inference for Everyone]: http://web.bryant.edu/~bblais/statistical-inference-for-everyone-sie.html
# 

# ## Chapter 1
# 
# ## Introduction

# ### History
# 
# For a much more detailed account, please see (Loredo, 1990; Jaynes, 2003)
# 
# First formal account of the calculation of probabilities from Bernoulli(Bernoulli, 1713), who defined probability as a “degree of certainty”. His theorem states that, if the probability of an event is $p$ then the limiting frequency of that event converges to $p$. It was later, by Bayes and Laplace that the inverse problem was solved: given n occurrences out of $N$ trials, what is the probability $p$ of a single occurrence?
# 
# The solution was published posthumously by Rev. Thomas Bayes (1763), and soon redis- covered, generalized, and applied to astrophysics by Laplace. It is Laplace who really brought probability theory to a mature state, applying it to problems in astrophysics, geology, meteo- rology, and others. One famous application was the determination of the masses of Jupiter and Saturn and the quantification of the uncertainties.
# 
# ### Derivation of Bayes' Rule (aka Bayes' Theorem)
# 
# Laplace took as axioms the sum and product rules for probability:
# 
# 
# \begin{eqnarray}
# p(A|C) + p(\bar{A}|C) &=& 1 \\\\
# p(AB|C) &=& p(A|BC)p(B|C)
# \end{eqnarray}
# 
# from there, given the obvious symmetry $p(AB|C)=p(BA|C)$ we get 
# 
# \begin{eqnarray}
# p(A|BC)p(B) &=& p(B|AC)p(A) \\\\
# p(A|BC) &=& \frac{p(B|AC)p(A)}{p(B)}
# \end{eqnarray}
# 
# which is Bayes' Theorem.
# 
# ### Further History
# After Laplace's death, his ideas came under attack by mathematicians.  They
# criticized two aspects of the theory:
# 
# 1. The axioms, although *reasonable*, were not clearly unique for 
# a definition of probability as vague as ``degrees of plausibility''.  The
# definition seemed vague, and thus the axioms which support the theory seemed
# arbitrary.  If one defines probabilities as limiting frequencies of events,
# then these axioms are justified.
# 2. It was unclear how to assign the prior probabilities in the first place.
# Bernoulli introduced the *Principle of Insufficient Reason*, which states
# that if the evidence does not provide any reason to choose $A_1$ or $A_2$,
# then one assigns equal probability to both.  If there are $N$ such
# propositions, then the probability is assigned $1/N$ for each.  Although
# again, reasonable, it was not clear how to generalize it to a continuous
# variable.  
# 
# If one defines probabilities as limiting frequencies of events,
# this problem disappears, because the notion of prior probabilities
# disappeared, as well as the probability of an hypothesis.  Hypotheses are true
# or false (1 or 0) for *all* elements of an ensemble or repeated
# experiment, and thus does not have a limiting frequency other than 0 or 1.
# 
# 
# 

# ### Response
# 
# Shifting to a limiting frequency definition, researchers avoided the issues
# above, and did not pursue their direct solution vigorously.  The solutions did
# come, however. 
# 
# In the mid-1900's, R. T. Cox (1946, 1961) and E. T. Jaynes (1957, 1958)
# demonstrated that, from a small collection of reasonable "desiderata" (aka
# axioms), one could develop a complete and rigorous mathematical theory from
# "degrees of plausibility".  These "desiderata" are:
# * Degrees of plausibility are represented by real numbers
# * Qualitative correspondence with common sense.  Consistent with deductive
# logic in the limit of true and false propositions.
# * Consistency
#     1. If a conclusion can be reasoned out in more than one way, every possible
#     way must lead to the same result
#     2. The theory must use all of the information provided
#     3. Equivalent states of knowledge must be represented by equivalent
#     plausibility assignments
# 
# With just these it is shown that the original, Laplace, methods of using Bayes'
# theorem were the correct ones.  It is also shown that **any theory of
# probability is either Bayesian, or violates one of the above desiderata**.   
# 
# The concern about assigning prior probabilities was answered in the work of
# Shannon and Jaynes, with the advent of maximum entropy methods and the methods
# of transformation groups.  
# 
# As a note, it is worth quoting Loredo, 1990: 
# 
# > It is worth emphasizing that probabilities are *assigned*, not *measured*.  This is because probabilities are measures of plausibilities of propositions; they thus reflect whatever information one may have bearing on the truth of propositions, and are not properties of the propositions themselves.
# 
# > ...
# 
# > In this sense, Bayesian Probability Theory is 'subjective,' it describes
# states of knowledge, not states of nature.  But it is `objective' in that we
# insist that equivalent states of knowledge be represented by equal
# probabilities, and that problems be well-posed: enough information must be
# provided to allow unique, unambiguous probability assignments.
# 
# Although there isn't a unique solution for converting verbal descriptions into
# prior probabilities in *every* case, the current methods allow this
# translation in many very useful cases.
# 
# 
# 

# ### Procedure
# 
# In all of the cases that follow, there is a common procedure.  We want to
# estimate parameters in a model, so we write down a probability distribution
# for those parameters dependent on the data, and any available information,
# $I$.  If we have one parameter in the model, then the form is like:
# 
# \begin{eqnarray}
# p({\rm parameter}|{\rm data},I)
# \end{eqnarray}
# 
# We apply Bayes' theorem/rule to write it in terms of things we have a handle on:
# 
# \begin{eqnarray}
# p({\rm parameter}|{\rm data},I) &=& \frac{p({\rm data}|{\rm
# parameter},I)p({\rm parameter}|I)}{p({\rm data}|I)}
# \end{eqnarray}
# 
# The left-hand side and the top two terms have names, and the bottom term is a
# normalization constant (which we will often omit, and work in proportions).
# 
# \begin{eqnarray}
# \overbrace{p({\rm parameter}|{\rm data},I)}^{\rm posterior} &=& \frac{\overbrace{p({\rm data}|{\rm
# parameter},I)}^{\rm likelihood}\overbrace{p({\rm parameter}|I)}^{\rm
# prior}}{\underbrace{p({\rm data}|I)}_{\rm normalization}} \\\\
# &\propto& \overbrace{p({\rm data}|{\rm
# parameter},I)}^{\rm likelihood}\overbrace{p({\rm parameter}|I)}^{\rm
# prior}
# \end{eqnarray}
# 
# The likelihood is how the data could be generated from the model. The prior is
# a weighting of the parameter possibilities, before we see the data.  
# 
# All of the information in the problem is complete once the posterior is
# written down.  After that, it is a matter of working with that distribution to
# obtain the estimate.  Often, we take the maximum posterior, but we can also
# take the mean, median or any other central measure.  We can look at standard
# deviations to determine confidence intervals, but we can also look at
# quartiles.  We will often look at the log of the posterior, as an analytical
# trick.  When all else fails, we can find the estimate numerically from the
# posterior. 
# 
# 

# ### Orthodox Hypothesis Tests
# 
# 

# Much of orthodox hypothesis testing can be interpreted in a much more
# straightforward way with the Bayesian approach.  For example, the $p$ value
# calculated in the orthodox fashion is *"the probability, computed assuming
# that the null hypothesis $H_o$ is true, of observing a value of the test
# statistic that is at least as extreme as the value actually computed from the
# data"* (Bowerman and O'Connell, 2003).  In the orthodox method, if you want to
# infer from the data that the mean value is, say, greater than zero you set up
# the null with $H_o: \mu\le 0$ and the alternate with $H_a: \mu>0$, select the
# appropriate statistic ($z$, $t$, etc$\ldots$), calculate the $p$-value of the
# null, where you use hypothetical data and look for the frequency that $H_o$ is
# true.  Finally, you reject the null at the level of significance, usually at
# the 5% level.  No wonder students get confused!
# 
# In the Bayesian way, we take the posterior distribution for the parameter,
# $\mu$, and then ask *"what is the probability that $\mu$ is greater than 0?"*,
# integrate the posterior probability distribution from 0 to infinity and get
# that probability directly.  In many applications, *they both give
# identical numerical results!* 
# 
# (Jeffreys, 1939) put it in the following way:
# >    What the use of $p$ implies, therefore, is that a hypothesis that may be
# true may be rejected because is has not predicted observable results that have
# not occurred.  This seems a remarkable procedure.  On the face of it the fact
# that such results have not occurred might be more reasonably be taken as
# evidence for the law, not against it.
# 
# 
# Another comment, this time from Jaynes is that
# 
# >If
# we reject $H_o$, then we should reject probabilities conditional on $H_o$
# being true.  The $p$-value is such a probability, so the procedure invalidates
# itself.  
# 
# 
# 
# 

# In[ ]:




# ---------------------

# In[8]:

from IPython.core.display import HTML


def css_styling():
    styles = open("../styles/custom.css", "r").read()
    return HTML(styles)
css_styling()


# In[ ]:



