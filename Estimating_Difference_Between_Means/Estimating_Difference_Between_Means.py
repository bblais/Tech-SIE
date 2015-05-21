
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

# ## Estimating the Paired-Data Difference Between Means, $\delta_k \equiv x_k-y_k$
# 

# $\newcommand{\bvec}[1]{\mathbf{#1}}$
# 
# We want
# \begin{eqnarray}
# p(\mu_\delta|\bvec{x},\bvec{y},\sigma_x,\sigma_y,I)
# \end{eqnarray}
# where  $\delta_k \equiv x_k-y_k$.
# 
# We have from the Normal model the following likelihoods for $x_k$ and
# $y_k$:
# \begin{eqnarray}
# p(x_k|\mu,\sigma_x,I)&=&\frac{1}{\sqrt{2\pi\sigma_x^2}}e^{-(x_k -
# \mu_x)^2/2\sigma_x^2}\\\\
# p(y_k|\mu,\sigma_y,I)&=&\frac{1}{\sqrt{2\pi\sigma_y^2}}e^{-(y_k -
# \mu_y)^2/2\sigma_y^2}
# \end{eqnarray}
# 
# Now we need to find the likelihood function for $\delta_k \equiv x_k-y_k$. 
# 

# ### Changing Variables
# 
# If we have $Z=f(X,Y)$, and we know about $X$ and $Y$, we can learn about $Z$.
# \begin{eqnarray}
# p(Z|I)&=&\int \int p(Z|X,Y,I) \times p(X,Y|I) dXdY \\\\
# &=&\int \int \delta(Z-f(X,Y)) \times p(X,Y|I) dXdY
# \end{eqnarray}
# 
# Say, $Z=X-Y$, and $X$ and $Y$ are independent, then $p(X,Y|I)=p(X|I)p(Y|I)$
# and we have 
# \begin{eqnarray}
# p(Z|I) &=& \int dX p(X,I) \int dY p(Y|I)\delta(Z-X+Y) \\\\
# &=&  \int dX p(X,I)p(Y=X-Z|I)
# \end{eqnarray}
# 
# Further, if the probabilities are Gaussian, then we have
# 
# \begin{eqnarray}
# p(Z|I) &=& \frac{1}{2\pi\sigma_x\sigma_y}\int_{-\infty}^{\infty} dX
# e^{-(X-\mu_x)^2/2\sigma_x^2}\times e^{-(X-Z-\mu_y)^2/2\sigma_y^2} 
# \end{eqnarray}
# One can do some pretty boring algebra at this point (factoring the exponents),
# or use a program like *xmaxima*:
# 
# 
# 

#     (C1) ASSUME_POS:TRUE;
#     (D1)                                 TRUE
#     (C2) 1/(2*%PI)/sx/sy*integrate(exp(-(x-xo)^2/(2*sx^2))*
#                exp(-(x-z-yo)^2/(2*sy^2)),x,-inf,inf);
# 
#                              2                       2               2
#                             z  + (2 yo - 2 xo) z + yo  - 2 xo yo + xo
#                           - ------------------------------------------
#                                               2       2
#                                           2 sy  + 2 sx
#                 SQRT(2) %E
#     (D2)        ------------------------------------------------------
#                                                 2     2
#                              2 SQRT(%PI) SQRT(sy  + sx )
# 
#     (C3) factor(z^2+(2*yo-2*xo)*z+yo^2-2*xo*yo+xo^2);
#                                                  2
#     (D3)                            (z + yo - xo)
# 

# 
# So we get
# 
# \begin{eqnarray}
# p(Z|I) &=&
# \frac{1}{\sqrt{2\pi(\sigma_x^2+\sigma_y^2)}}
# e^{-(z-(\mu_x-\mu_y))^2/2(\sigma_x^2+\sigma_y^2)} \\\\
# &=&\frac{1}{\sqrt{2\pi\sigma_z}}
# e^{-(z-\mu_z)^2/2\sigma_z} \\\\ \mbox{ where }
# \mu_z&\equiv& \mu_x-\mu_y \\\\
# \sigma_z^2&\equiv&\sigma_x^2+\sigma_y^2
# \end{eqnarray}
# 

# ### Continuing with Paired Data
# 
# Changing variables to $\delta_k$, it is clear that the likelihood for
# $\delta_k$ is the same form as $\delta_x$ and $\delta_y$.  Thus we have the
# *exact same* results on the paired difference, both for known and unknown
# $\sigma$, quoted in z-test and t-test sections.
# 
# 

# ## Difference of Means, $\delta\equiv \mu_x - \mu_y$, known $\sigma_x$ and $\sigma_y$

# Again, the change of variables trick works, but since we are given the means
# ($\mu_x$ and $\mu_y$) we need to use the posterior distributions,
# $p(\mu_x|\bvec{x},\sigma_x,I)$ and $p(\mu_y|\bvec{y},\sigma_y,I)$.
# 
# \begin{eqnarray}
# p(\mu_x|\bvec{x},\sigma_x,I)&=& 
# \sqrt{\frac{n}{2\pi \sigma_x^2}}e^{-n(\bar{x}-\mu_x)^2/2\sigma_x^2} \\\\
# p(\mu_y|\bvec{y},\sigma_y,I)&=& 
# \sqrt{\frac{m}{2\pi \sigma_y^2}}e^{-n(\bar{y}-\mu_y)^2/2\sigma_y^2}
# \end{eqnarray}
# 
# Performing the change of variables to $\delta \equiv \mu_x-\mu_y$ we get
# 
# \begin{eqnarray}
# p(\delta|\bvec{x},\bvec{y},\sigma_x,\sigma_y,I)&=&
# \frac{\sqrt{nm}}{2\pi\sigma_x\sigma_y}\int d\mu_y
# e^{-n(\bar{x}-\delta-\mu_y)^2/2\sigma_x^2}
# e^{-m(\bar{y}-\mu_y)^2/2\sigma_y^2} 
# \end{eqnarray}
# 
# Again, using *xmaxima*,
# 

#     (C1) ASSUME_POS:TRUE;
# 
#     (D1)                                 TRUE
#     (C2) f(d):=sqrt(n*m)/(2*%PI*sx*sy)*integrate(exp(-n*(xbar-d-my)^2/(2*sx^2))*
#                       exp(-m*(ybar-my)^2/(2*sy^2)),my,-inf,inf);
#     f(d);
# 
#                                                                 2
#                   SQRT(n m)                (- n) (xbar - d - my)
#     (D2) f(d) := ----------- INTEGRATE(EXP(----------------------)
#                  2 %PI sx sy                           2
#                                                    2 sx
# 
#                                                                 2
#                                                (- m) (ybar - my)
#                                            EXP(------------------), my, - INF, INF)
#                                                          2
#                                                      2 sy
#     (C3) 
#                                                      2
#     (D3) SQRT(2) SQRT(m) SQRT(n) EXPT(%E, - (m n ybar
# 
#                                                2                   2
#      + (- 2 m n xbar + 2 d m n) ybar + m n xbar  - 2 d m n xbar + d  m n)
# 
#             2         2                         2       2
#     /(2 n sy  + 2 m sx ))/(2 SQRT(%PI) SQRT(n sy  + m sx ))
#     (C4) factor((m*n)*ybar^2+(-2*m*n*xbar+2*d*m*n)*ybar+m*n*xbar^2-2*d*m*n*xbar+m*n*d^2);
# 
#                                                      2
#     (D4)                        m n (ybar - xbar + d)
# 

# Rewritten, this is
# 
# \begin{eqnarray}
# p(\delta|\bvec{x},\bvec{y},\sigma_x,\sigma_y,I)&=&
# \sqrt{\frac{nm}{2\pi(n\sigma_x^2+m\sigma_y^2)}}
#     e^{-mn(\delta-(\bar{x}-\bar{y}))^2/2(n\sigma_x^2+m\sigma_y^2)}
# \end{eqnarray}
# 
# or
# 
# \begin{eqnarray}
# \mu_\delta &\equiv& \mu_x-\mu_y \\
# \sigma_\delta &\equiv& \frac{\sigma_x^2}{n}+\frac{\sigma_y^2}{m}\\
# p(\delta|\bvec{x},\bvec{y},\sigma_x,\sigma_y,I)&=&
# \frac{1}{\sqrt{2\pi\sigma_\delta^2}}
#     e^{-(\delta-\mu_\delta)^2/2\sigma_\delta^2}
# \end{eqnarray}
# 

# ## Difference of Means, $\delta\equiv \mu_x - \mu_y$, unknown $\sigma_x$ and $\sigma_y$

# Making definitions as before for the $t$ distribution for each variable
# 
# \begin{eqnarray}
# t_x&\equiv&\frac{\mu_x-\bar{x}}{S_x/\sqrt{n}} \\\\
# t_y&\equiv&\frac{\mu_y-\bar{y}}{S_y/\sqrt{n}} \\\\
# S_x^2&\equiv&\frac{1}{(n-1)}\sum_{k=1}^{n} (x_k-\mu_x)^2 \\\\
# S_y^2&\equiv&\frac{1}{(m-1)}\sum_{k=1}^{m} (y_k-\mu_y)^2
# \end{eqnarray}
# From the addition of variables we get
# \begin{eqnarray}
# t&\equiv&\frac{\delta-(\bar{x}-\bar{y})}{\sqrt{S_x^2/m+S_y^2/n}} \\\\
# \tan \theta &\equiv& \frac{S_x/\sqrt{n}}{S_y/\sqrt{m}}
# \end{eqnarray}
# 
# $\tan \theta$ depends on the data, and $t_x$, and $t_y$ are known, so the
# distribution for $t$ should be known.  It is named the Behren's distribution.
# 
# 

# In[1]:




# ---------------------

# In[2]:

from IPython.core.display import HTML


def css_styling():
    styles = open("../styles/custom.css", "r").read()
    return HTML(styles)
css_styling()

