
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

# ## Simple Linear Regression, $y_k= m x_k + b + \epsilon$
# 

# $\newcommand{\bvec}[1]{\mathbf{#1}}$ 
# Given 
# \begin{eqnarray}
# y_k&=& m x_k + b + \epsilon
# \end{eqnarray}
# where the (known) noise term is 
# \begin{eqnarray}
# p(\epsilon|I) &=& \frac{1}{\sqrt{2\pi \sigma^2}}e^{-\epsilon}/2\sigma^2
# \end{eqnarray}
# then we have
# 
# \begin{eqnarray}
# p(m,b|\bvec{y},I)&=& \int_0^{\infty} p(m,b,\sigma|\bvec{y},I)d\sigma \\\\
# &=& \int_0^{\infty} p(\bvec{y}|m,b,\sigma,I)p(m,b,\sigma|I)d\sigma \\\\
# p(y_k|m,b,\sigma,I)&=& \frac{1}{\sqrt{2\pi \sigma^2}}e^{-(m
# x_k+b-y_k)/2\sigma^2}\\\\
# p(\bvec{y}|m,b,\sigma,I)&\propto& \frac{1}{\sigma^N}e^{-\sum (m
# x_k+b-y_k)^2/2\sigma^2}
# \end{eqnarray}
# 
# As before, with uniform priors, we get (assuming we know $\sigma$)
# \begin{eqnarray}
# p(m,b|\bvec{y},I)&\propto&\frac{1}{\sigma^N}e^{-\sum (m
# x_k+b-y_k)^2/2\sigma^2} \\\\
# L&=&{\rm constant} - \sum (m x_k+b-y_k)^2/2\sigma^2 \\\\
# \nabla_{m,b} L &=& 0 \mbox{ (maximum $p$ = maximum $L$ = minimum squares)}\\\\
# \end{eqnarray}
# Gives the two equations
# \begin{eqnarray}
# \sum (m x_k+b-y_k) x_k &=& 0 \\\\
# \sum (m x_k+b-y_k) &=& 0
# \end{eqnarray}
# Define
# \begin{eqnarray}
# v&=&\sum x_k^2 \\\\
# c&=&\sum x_k y_k \\\\
# \bar{x}&=&\frac{1}{N}\sum x_k \\\\
# \bar{y}&=&\frac{1}{N}\sum y_k
# \end{eqnarray}
# 
# and we have
# 
# \begin{eqnarray}
# \sum (m x_k+b-y_k) x_k &=& 0 \\\\
# vm + N\bar{x} b - c &=& 0 
# \end{eqnarray}
# and
# \begin{eqnarray}
# \sum (m x_k+b-y_k) &=& 0 \\\\
# N\bar{x}m + N b - N\bar{y} &=& 0
# \end{eqnarray}
# 

# ### Quick recipe for solving  $2\times 2$ equations
# A nice little trick I learned in high school for quickly solving $2\times 2$
# equations is to use the determinant.  It can be used for any size, but it is
# particularly expedient for  $2\times 2$ equations.  
# 
# 1. Write the equations in the following form:
#     \begin{eqnarray}
#     ax+by&=&c \\\\
#     dx+ey&=&f
#     \end{eqnarray}
# 2. Form the determinant of the left-hand side parameters like
#     \begin{eqnarray}
#     D&\equiv& \left|\begin{array}{cc}a & b \\\\ d & e\end{array} \right| \\\\
#     &=& ae - bd 
#     \end{eqnarray}
# 3. The solutions are formed by the following ratios
#     \begin{eqnarray}
#     x&=& \frac{\left|\begin{array}{cc}c & b \\\\ f & e\end{array} \right|}{D} \\\\
#     &=& \frac{ce-bf}{ae-bd} 
#     \end{eqnarray}
#     and
#     \begin{eqnarray}
#     y&=& \frac{\left|\begin{array}{cc}a & c \\\\ d & f\end{array} \right|}{D} \\\\
#     &=& \frac{af-cd}{ae-bd}
#     \end{eqnarray}
# 
#     Notice that the numerators are made in the same way as $D$, except that the
#     relevant column (1st column for $x$, 2nd for $y$) is replace with the
#     right-hand side parameters.
# 
# Why is this any better than solving for one, and plugging in?  I find that the
# arithmetic in this recipe to be more straightforward, and less prone to
# careless errors.
# 
# 

# ### Solution to the Simple Least Squares Problem
# 
# So we have
# \begin{eqnarray}
# vm + N\bar{x} b &=& c \\\\
# \bar{x}m + b =\bar{y}
# \end{eqnarray}
# 
# Solving we get
# 
# \begin{eqnarray}
# D&\equiv& \left|\begin{array}{cc}v & N\bar{x}  \\\\ \bar{x}  & 1\end{array} \right| \\\\
# &=& v - N (\bar{x})^2 \\\\
# m&=&  \frac{\left|\begin{array}{cc}c & N\bar{x} \\\\ \bar{y} & 1\end{array}
# \right|}{D} =
#  \frac{c-N\bar{x}\bar{y}}{v - N (\bar{x})^2} \\\\
# b&=&  \frac{\left|\begin{array}{cc}v & c \\\\ \bar{x} & \bar{y}\end{array}
# \right|}{D} = \frac{v\bar{y}-c\bar{x}}{v - N (\bar{x})^2} \\\\
# \end{eqnarray}
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

