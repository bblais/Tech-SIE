
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

# ## Estimating a Proportion
# 

# $$\newcommand{\twocvec}[2]{\left(\begin{array}{c}
#         #1 \\\\ #2
#         \end{array}\right)}
# \newcommand{\nchoosek}[2]{\twocvec{#1}{#2}}
# $$
# 
# If $\theta$ is the model representing the probability, $\theta$, of the coin
# landing on heads (and $1-\theta$ is the probability of landing on tails), we
# need to make an estimate of probability of model $\theta$ being true given the
# data, which will consist of $N$ flips of which $h$ are heads.  
# 
# Bayes rule is:
# \begin{eqnarray}
# p(\theta|D,I) &=& \frac{p(D|\theta,I)p(\theta|I)}{p(D|I)} = 
# \frac{p(D|\theta,I)p(\theta,I)}{\sum_\theta p(D|\theta,I)p(\theta|I)}
# \end{eqnarray}
# 
# Thus, the probability of a particular model $\theta$ being true is the product
# of the probability of the observed data ($h$ heads in $N$ flips) given the
# model $\theta$ and the prior probability of the model $\theta$ being true
# before we even look at the data, divided by the probability of the data itself
# over all models.
# 
# The prior probability of model $\theta$ will be assumed to be uniform (from
# maximum entropy considerations).  The probability, $\theta$, ranges from 0 to
# 1, to the prior is
# \begin{eqnarray}
# p(\theta|I) = 1
# \end{eqnarray}
# 
# The probability of the data given the random model, is just the binomial
# distribution:
# 
# \begin{eqnarray}
# p(D|\theta)=\nchoosek{N}{h} \theta^h (1-\theta)^{N-h}
# \end{eqnarray}
# 
# The probability of the data, $p(D|I)$, is found by summing (or in this case
# integrating) $p(D|\theta,I)p(\theta|I)$ for all $\theta$:
# 
# \begin{eqnarray}
# p(D|I) &=& \int_0^1 \nchoosek{N}{h} \theta^h (1-\theta)^{N-h} \cdot 1 d\theta
# \\\\
# &=&\frac{N!}{h!(N-h)!} \frac{h!(N-h)!}{(N+1)!} = \frac{1}{N+1}
# \end{eqnarray}
# 
# Now the probability of model $\theta$ being true, given the data, is just
# 
# \begin{eqnarray}
# p(\theta|D,I)&=& (N+1) \cdot \nchoosek{N}{h} \theta^h (1-\theta)^{N-h} \\
# &=& \frac{(N+1)!}{h!(N-h)!} \theta^h (1-\theta)^{N-h} 
# \end{eqnarray}
# 
# 

# ### Max, Mean, Variance
# 
# The model with the maximum probability is found by maximizing $p(\theta|D,I)$
# w.r.t. $\theta$:
# 
# \begin{eqnarray}
# \frac{dP(\theta|D,I)}{d\theta} &=& 0 = \frac{(N+1)!}{h!(N-h)!} \left( 
#        -(N-h) \theta^h (1-\theta)^{N-h-1} + h \theta^{h-1} (1-\theta)^{N-h} \right) \\\\
# (N-h) \theta^h (1-\theta)^{N-h-1} &=&  h \theta^{h-1} (1-\theta)^{N-h} \\\\
# \theta(N-h) &=& (1-\theta) h = h-\theta h = N\theta-\theta h \\\\
# \theta&=&\frac{h}{N} \;\;\;\;\;\surd
# \end{eqnarray}
# 
# The average and the standard deviation is also straightforward.
# 
# 
# \begin{eqnarray}
# \bar{\theta} &=& \int_0^1 \theta \cdot \frac{(N+1)!}{h!(N-h)!} \theta^h (1-\theta)^{N-h} \\\\
#  &=& \frac{(N+1)!}{h!(N-h)!} \int_0^1 \theta^{h+1} (1-\theta)^{N-h} \\\\
#  &=&\frac{(N+1)!}{h!(N-h)!} \frac{(h+1)!(N-h)!}{(N+2)!} \\\\
#  &=&\frac{h+1}{N+2} \\\\
# \bar{\theta^2} &=& \int_0^1 \theta^2 \cdot \frac{(N+1)!}{h!(N-h)!} \theta^h (1-\theta)^{N-h} \\\\
#  &=&\frac{(N+1)!}{h!(N-h)!} \frac{(h+2)!(N-h)!}{(N+3)!} \\\\
#  &=&\frac{(h+1)(h+2)}{(N+2)(N+3)} \\\\
# \sigma^2 &=& \bar{\theta^2} - \bar{\theta}^2 =  \frac{(h+1)(h+2)}{(N+2)(N+3)} -
#                               \frac{(h+1)(h+1)}{(N+2)(N+2)} \\\\
# &=&\frac{(h+1)(N-h+1)}{(N+2)^2(N+3)} \\\\
# &=& \frac{(h+1)}{(N+2)}\left( \frac{n+2}{n+2} - \frac{h+1}{N+2}\right)
# \frac{1}{N+3} \\\\
# &=& \bar{\theta}(1-\bar{\theta})\frac{1}{N+3}
# \end{eqnarray}
# 
# ### An Approximation for the Variance
# 
# If $f=h/N$ is the actual fraction of heads observed, then the variance above
# can be written as
# \begin{eqnarray}
# \sigma^2 &=&\frac{(fN+1)(N-fN+1)}{(N+2)^2(N+3)} \\\\
# \mbox{(for large $N$)}&\approx& \frac{(fN+1)(N-fN)}{N^3}
#                        =\frac{(fN+1)(1-f)}{N^2} \\\\
# \mbox{(for large $fN$)}&\approx& \frac{(fN)(N-fN)}{N^2} = \frac{f(1-f)}{N} \\\\
# \sigma^2&\approx& \frac{f(1-f)}{N}
# \end{eqnarray}
# 
# In this limit, the distribution (beta distribution) can be approximated with a
# Gaussian.
# 

# In[11]:




# ---------------------

# In[8]:

from IPython.core.display import HTML


def css_styling():
    styles = open("../styles/custom.css", "r").read()
    return HTML(styles)
css_styling()

