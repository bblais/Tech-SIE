
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

# ## Estimating the mean and standard deviation
# 
# This derivation is taken directly from (Sivia, 1996), with some of the steps filled in and elaborated by me.

# ### Setting up the Problem
# 
# $\newcommand{\bvec}[1]{\mathbf{#1}}$
# 
# If both $\mu$ and $\sigma$ are unknown, then the procedure is as follows.  We
# will need the joint distribution of both variables
# \begin{eqnarray}
# p(\mu,\sigma|\bvec{x},I)
# \end{eqnarray}
# and then integrate the ``nuisance'' parameter, to get the posterior for the
# parameter we are interested in.  If we are estimating the mean, we need to
# integrate out the standard deviation, and vice versa:
# \begin{eqnarray}
# p(\mu|\bvec{x},I)&=&\int_0^{\infty} p(\mu,\sigma|\bvec{x},I) d\sigma \\\\
# p(\sigma|\bvec{x},I)&=&\int_{-\infty}^{\infty} p(\mu,\sigma|\bvec{x},I) d\mu 
# \end{eqnarray}
# 
# The joint distribution can be found using Bayes rule, Gaussian likelihoods,
# and simple flat priors.  We will see how using the correct (Jeffrey's) prior
# for $\sigma$ will slightly modify our results.  
# \begin{eqnarray} 
# p(\mu,\sigma|\bvec{x},I) &\propto& p(\bvec{x}|\mu,\sigma,I) p(\mu,\sigma|I) \\\\
# p(\bvec{x}|\mu,\sigma,I)&=&\left(\frac{1}{\sqrt{2\pi\sigma^2}}\right)^N
# e^{\frac{1}{-2\sigma^2}\sum_{k=1}^{N} (x_k-\mu)^2}\\\\
# p(\mu,\sigma|I)&=&{\rm constant} \mbox{ for } \sigma>0 
# \end{eqnarray}
# 
# Plugging into the posterior for the mean we get
# \begin{eqnarray}
# p(\mu|\bvec{x},I)&=&\int_0^{\infty} p(\mu,\sigma|\bvec{x},I) d\sigma \\\\
# &\propto&\int_0^{\infty} d\sigma
# \frac{1}{\sigma^N}e^{\frac{1}{-2\sigma^2}\sum_{k=1}^{N} (x_k-\mu)^2}
# \end{eqnarray}
# For convenience, make the substitution $\sigma=1/t$, which implies
# $d\sigma=-dt/t^2$, and we have
# \begin{eqnarray}
# p(\mu|\bvec{x},I)&\propto&\int_0^{\infty} 
# t^{N-2}e^{\frac{t^2}{2}\sum_{k=1}^{N} (x_k-\mu)^2} dt\\\\
# &\propto& \left[\sum_{k=1}^{N} (x_k-\mu)^2 \right]^{(N-1)/2}
# \end{eqnarray}
# 
# The last step of the analysis was obtained by noticing that 
# \begin{eqnarray}
# \int_0^{\infty} 
# t^{N-2}e^{\frac{t^2}{2}\sum_{k=1}^{N} (x_k-\mu)^2} dt
# \end{eqnarray}
# is of the form of a simple power ($t^{N-2}$) multiplied by a Gaussian:
# \begin{eqnarray}
# \int_0^{\infty} t^{n}e^{-at^2} dt &\equiv& I_{n}
# \end{eqnarray}
# and the Gaussian integral tricks.
# 
# 

# ### Estimating the Mean
# 
# We finished the previous section with the tools to determine the posterior
# for the mean:
# \begin{eqnarray}
# p(\mu|\bvec{x},I)&\propto&\int_0^{\infty} 
# t^{N-2}e^{\frac{t^2}{2}\sum_{k=1}^{N} (x_k-\mu)^2} dt\\
# &\propto& \left[\sum_{k=1}^{N} (x_k-\mu)^2 \right]^{(N-1)/2}
# \end{eqnarray}
# 
# Now, with the standard trick used before (assuming a Gaussian posterior
# distribution), we look at the derivatives of the log-posterior.  Setting the
# first derivative to zero gives us our estimate, 
# 
# \begin{eqnarray}
# L(\mu)&=& {\rm constant}-\frac{(N-1)}{2}\log \sum_{k=1}^{N} (x_k-\mu)^2  \\
# \frac{dL}{d\mu} &=&\frac{(N-1)  \sum_{k=1}^{N} (x_k-\mu)}{\sum_{k=1}^{N}
# (x_k-\mu)^2} = 0 \\
# &=&\frac{(N-1)  \left(\sum_{k=1}^{N} x_k-N\mu\right)}{\sum_{k=1}^{N}
# (x_k-\mu)^2} = 0 \\
# \Rightarrow \hat{\mu} &=&\frac{1}{N} \sum_{k=1}^{N} x_k
# \end{eqnarray}
# 
# Calculating the second derivative allows us to determine confidence intervals.
# 
# \begin{eqnarray}
# \left.\frac{d^2L}{d\mu^2}\right|_{\hat{\mu}}&=& \left.-\frac{N (N-1)}{\sum_{k=1}^{N}
# (x_k-\mu)^2}\right|_{\hat{\mu}} + \underbrace{\left.\frac{(N-1)  \sum_{k=1}^{N} (x_k-\mu)\cdot 2 \sum_{k=1}^{N} (x_k-\mu)}{\sum_{k=1}^{N}
# (x_k-\mu)^3}\right|_{\hat{\mu}}}_{=0}\\
# {\rm width}&=&-\left[\left.\frac{d^2L}{d\mu^2}\right|_{\hat{\mu}}\right]^{-1/2} \\
# &=&\frac{1}{\sqrt{N(N-1)}}\sum_{k=1}^{N} (x_k-\mu)
# \end{eqnarray}
# 
# So our final estimate is
# 
# \begin{eqnarray}
# \mu&=&\bar{x} \pm \frac{S}{\sqrt{N}} \\
# \bar{x}&=& \frac{1}{N} \sum_{k=1}^{N} x_k \\
# S^2&=& \frac{1}{(N-1)}\sum_{k=1}^{N} (x_k-\mu)^2 
# \end{eqnarray}
# 

# ### A More Convenient Form
# 
# If we rewrite the sum $\sum_{k=1}^{N} (x_k-\mu)^2$ as 
# \begin{eqnarray}
# \sum_{k=1}^{N} (x_k-\mu)^2 &\equiv&N(\bar{x}-\mu)^2+V \\\\
# V&\equiv& \sum_{k=1}^{N} (x_k-\bar{x})^2
# \end{eqnarray}
# 
# Then the posterior is 
# 
# \begin{eqnarray}
# p(\mu|\bvec{x},I)&\propto& \left[N(\bar{x}-\mu)^2+V\right]^{(N-1)/2}
# \end{eqnarray}
# 
# which is the Student-t distribution with $N-2$ degrees of freedom.  Had we
# used the suggested (Jeffreys) prior for the scale parameter, $\sigma$, 
# 
# \begin{eqnarray}
# p(\mu,\sigma|I)&=&\left\{\begin{array}{cc}\frac{1}{\sigma} & \sigma>0 \\\\
# 0 & \mbox{otherwise}\end{array}\right.
# \end{eqnarray}
# 
# which simply adds a factor $t$ to the posterior integral, and the result is
# 
# \begin{eqnarray}
# p(\mu|\bvec{x},I)&\propto& \left[N(\bar{x}-\mu)^2+V\right]^{N/2}
# \end{eqnarray}
# again, the Student-t distribution but with $N-1$ degrees of freedom.
# 
# We now define
# \begin{eqnarray}
# t&\equiv&\frac{\mu-\bar{x}}{S/\sqrt{N}}
# \end{eqnarray}
# 
# This variable $t$ has exactly the standard t-distribution with $N-1$ degrees
# of freedom, in a form which can be readily looked up.
# 
# 

# ### Estimating $\sigma$
# 
# With the Jeffrey's prior,
# \begin{eqnarray}
# p(\sigma|\bvec{x},I)&=&\int_{-\infty}^{\infty} p(\mu,\sigma|\bvec{x},I) d\mu \\\\
# &\propto& \frac{1}{\sigma^{N+1}} e^{-V/2\sigma^2}\underbrace{\int_{-\infty}^{\infty}
# e^{-\frac{N(\bar{x}-\mu)^2}{2\sigma^2}}d\mu}_{\propto \sigma} \\\\
# &\propto& \frac{1}{\sigma^{N}} e^{-V/2\sigma^2}
# \end{eqnarray}
# 
# If we change variables to $\xi\equiv V/\sigma^2$, then this is the $\chi^2$
# distribution with $f\equiv N-1$ degrees of freedom:
# \begin{eqnarray}
# d\sigma &\propto& \xi^{-3/2} \\\\
# p(\xi|\bvec{x},I)&=&p(\sigma|\bvec{x},I)\times
# \left|\frac{d\sigma}{d\xi}\right| \\\\
# &\propto& \xi^{\frac{N}{2}} e^{-\xi/2}\times \xi^{-3/2} \\\\
# &\propto& \xi^{\frac{N-1}{2}-1} e^{-\xi/2} \\\\
# &\propto& \xi^{\frac{f}{2}-1} e^{-\xi/2} 
# \end{eqnarray}
# 
# If we used the uniform prior, then this would be $f=N-2$ degrees of freedom.
# 
# With the uniform prior,
# \begin{eqnarray}
# p(\sigma|\bvec{x},I)&=&\int_{-\infty}^{\infty} p(\mu,\sigma|\bvec{x},I) d\mu \\\\
# &\propto& \frac{1}{\sigma^{N}} e^{-V/2\sigma^2}\underbrace{\int_{-\infty}^{\infty}
# e^{-\frac{N(\bar{x}-\mu)^2}{2\sigma^2}}d\mu}_{\propto \sigma} \\\\
# &\propto& \frac{1}{\sigma^{N-1}} e^{-V/2\sigma^2}
# \end{eqnarray}
# 
# \begin{eqnarray}
# L(\sigma) &=& {\rm constant}-(N-1)\log \sigma - \frac{V}{2\sigma^2} \\\\
# \frac{dL}{d\sigma} &=& -\frac{N-1}{\sigma}+\frac{V}{\sigma^3} = 0 \\\\
# \Rightarrow \hat{\sigma^2} &=& \frac{V}{N-1} \\\\
# \left.\frac{d^2L}{d\sigma^2}\right|_{\hat{\sigma}} &=&
# \frac{N-1}{\hat{\sigma}^2}-\frac{3V}{\hat{\sigma}^4} \\\\
# &=&\frac{N-1}{\hat{\sigma}^2}-\frac{3(N-1)}{\hat{\sigma}^2} \\\\
# &=&-\frac{2(N-1)}{\hat{\sigma}^2} \\\\
# {\rm width}&=&-\left[\left.\frac{d^2L}{d\sigma^2}\right|_{\hat{\sigma}}\right]^{-1/2} \\\\
# &=& \frac{\hat{\sigma}}{\sqrt{2(N-1)}}
# \end{eqnarray}
# 

# ### Summary
# 
# So our final estimate for the mean and standard deviation is
# 
# \begin{eqnarray}
# \mu&=&\bar{x} \pm \frac{S}{\sqrt{N}} \\\\
# \bar{x}&=& \frac{1}{N} \sum_{k=1}^{N} x_k \\\\
# S^2&=& \frac{1}{(N-1)}\sum_{k=1}^{N} (x_k-\bar{x})^2 \\\\
# \sigma&=& S^2 \pm \frac{S^2}{\sqrt{2(N-1)}}
# \end{eqnarray}
# 
# 

# In[11]:




# ---------------------

# In[8]:

from IPython.core.display import HTML


def css_styling():
    styles = open("../styles/custom.css", "r").read()
    return HTML(styles)
css_styling()

