
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

# ## Estimating Mean, Known Deviation
# 

# This derivation is taken directly from (Sivia, 1996), with some of the steps
# filled in and elaborated by me.

# ### Introducing the Distributions
# 
# $\newcommand{\bvec}[1]{\mathbf{#1}}$
# 
# We want to estimate the mean of data, given the standard deviation. Here we
# want 
# 
# 
# \begin{eqnarray}
# p(\mu|\bvec{x},\sigma,I)
# \end{eqnarray}
# 
# where $\mu$ is the parameter we want to estimate, $x_k$ are the data (the full
# vector abbreviated as $\bvec{x}$), $\sigma$
# is the (known) standard deviation of the distribution, and $I$ is any other
# background information.  In other words, we would like the probability of the
# parameter ($\mu$) given the data ($\bvec{x}$).  From Bayes' theorem
# we get the *posterior* probability distribution for $\mu$:
# 
# \begin{eqnarray}
# p(\mu|\bvec{x},\sigma,I) \propto p(\bvec{x}|\mu,\sigma,I) \cdot
# p(\mu|\sigma,I)
# \end{eqnarray}
# 
# The *prior* information, $p(\mu|\sigma,I)$, about the value we want to
# estimate, $\mu$, will be as non-informative as possible (we are really ignorant
# of its value).  Thus, we use a uniform distribution:
# \begin{eqnarray}
# p(\mu|\sigma,I)= p(\mu|I)&=&\left[\begin{array}{cc}A & \mu_{\rm min}\le \mu \le
# \mu_{\rm max} \\
# 0 & \mbox{otherwise}\end{array}\right.
# \end{eqnarray}
# 
# The *likelihood*, also known as the generative probability because it is
# the probability that the data would be generated from the model, is
# \begin{eqnarray}
# p(\bvec{x}|\mu,\sigma,I)
# \end{eqnarray}
# 
# If we assume *independent*, *Gaussian* distributions
# for each data point, with a {\em known} $\sigma$, then we have
# \begin{eqnarray}
# p(x_k|\mu,\sigma,I)&=&\frac{1}{\sqrt{2\pi\sigma^2}}e^{-(x_k -
# \mu)^2/2\sigma^2}\\
# p(\bvec{x}|\mu,\sigma,I)&=&\prod_{k=1}^{N}
# \frac{1}{\sqrt{2\pi\sigma^2}}e^{-(x_k - \mu)^2/2\sigma^2} 
# \end{eqnarray}
# 
# The Gaussian, or Normal distribution, is justified from maximum entropy arguments.
# 

# ## An Aside on Log Posterior
# 
# It is often convenient to use the log of the posterior distribution, rather
# than the posterior distribution itself.  It has the same maxima, but is easier
# to analyze in many cases, especially with Gaussian assumptions.
# 
# If, for example, the posterior has a Gaussian form:
# \begin{eqnarray}
# p(y)&=&\frac{1}{\sqrt{2\pi\sigma^2}}e^{-y^2/2\sigma^2} 
# \end{eqnarray}
# then the log posterior is 
# \begin{eqnarray}
# L(y)&=&\log\left(\frac{1}{\sqrt{2\pi\sigma^2}}\right) - \frac{y^2}{2\sigma^2}
# \end{eqnarray}
# The maximum is found by setting the first derivative to zero, getting the
# obvious result.
# \begin{eqnarray}
# \frac{dL(y)}{dy}&=&-y/\sigma^2 = 0 \\
# \Rightarrow y&=& 0 
# \end{eqnarray}
# If we look at the second derivative, we get
# \begin{eqnarray}
# \frac{d^2L(y)}{dy^2}&=&-\frac{1}{\sigma^2} \\
# \Rightarrow \sigma&=& \left(-\frac{d^2L(y)}{dy^2}\right)^{-1/2}
# \end{eqnarray}
# 
# So, under the Gaussian posterior assumption, then the width of the posterior
# distribution is related to the second derivative of the log posterior.  
# 
# 

# ## Continuing
# 
# Now we are in a position to calculate the probability distribution for our
# parameter, $\mu$, obtain the best estimate and the confidence intervals.
# 
# \begin{eqnarray}
# p(\mu|\bvec{x},\sigma,I) &\propto& p(\{x_{k}\}|\mu,\sigma,I) \cdot
# p(\mu|\sigma,I) \\
# &\propto& \prod_{k=1}^{N} \frac{1}{\sqrt{2\pi\sigma^2}}e^{-(x_k -
# \mu)^2/2\sigma^2} \\
# L(\mu|x_1,x_2,\cdots,x_n,\sigma,I) &=&{\rm constant} - \sum_{k=1}^{N} (x_k -
# \mu)^2/2\sigma^2
# \end{eqnarray}
# The best estimate, $\hat{\mu}$, is that which maximizes $L$
# \begin{eqnarray}
# \left.\frac{dL}{d\mu}\right|_{\hat{\mu}} &=& + \frac{1}{\sigma^2}\sum_{k=1}^{N} (x_k -
# \mu)|_{\hat{\mu}} =0\\
# \sum_{k=1}^{N} x_k - \sum_{k=1}^{N} \hat{\mu} &=&0 \\
# \hat{\mu}&=&\frac{\sum_{k=1}^{N} x_k}{N} 
# \end{eqnarray}
# which is just the sample mean.  If we denote 1 standard deviation confidence
# intervals in our estimate of $\mu$, then our best estimate is $\mu=\hat{\mu} \pm
# \sigma_{\mu}$.  The width of the distribution, which gives us
# the confidence interval, is related to the second derivative of $L$.
# \begin{eqnarray}
# \sigma_{\mu}&=&
# \left(-\left.\frac{d^2L(y)}{d\mu^2}\right|_{\hat{\mu}}\right)^{-1/2} \\ 
# \left.\frac{d^2L(y)}{d\mu^2}\right|_{\hat{\mu}} &=& -\frac{N}{\sigma^2} \\
# \sigma_{\mu}&=&\frac{\sigma}{\sqrt{N}}
# \end{eqnarray}
# 
# ## Summary
# 
# In summary, our best estimate of the value of a parameter, $\mu$, given the data
# $\bvec{x}\equiv \left\{x_k\right\}$ and the standard deviation of the likelihood, $\sigma$, is 
# 
# \begin{eqnarray}
# \mu &=& \frac{\sum_{k=1}^{N} x_k}{N} \pm \frac{\sigma}{\sqrt{N}} \\
# &\equiv& \bar{x}\pm \frac{\sigma}{\sqrt{N}}
# \end{eqnarray}
#     
#     
# Our posterior probability distribution for $\mu$ is 
# \begin{eqnarray}
# p(\mu|\bvec{x},\sigma,I)=\sqrt{\frac{N}{2\pi \sigma^2}}e^{-N(\bar{x}-\mu)^2/2\sigma^2}
# \end{eqnarray}
# 
# 
# 

# In[7]:




# ---------------------

# In[8]:

from IPython.core.display import HTML


def css_styling():
    styles = open("../styles/custom.css", "r").read()
    return HTML(styles)
css_styling()


# In[8]:



