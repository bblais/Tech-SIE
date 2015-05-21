
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

# ## Estimating the Ratio of Two Variances $\kappa\equiv \sigma_x^2/\sigma_y^2$
# 

# $\newcommand{\bvec}[1]{\mathbf{#1}}$
# 
# From *Estimating the Deviation* we have
# \begin{eqnarray}
# p(\sigma_x|\bvec{x},I)&\propto& \frac{1}{\sigma_x^{n}}e^{-V_x/2\sigma_x^2} 
# \end{eqnarray}
# For independent $\bvec{x}$ and $\bvec{y}$ we have
# \begin{eqnarray}
# p(\sigma_x,\sigma_y|\bvec{x},\bvec{y},I)&\propto& 
# \frac{1}{\sigma_x^{n}}\frac{1}{\sigma_y^{m}}
# e^{-V_x/2\sigma_x^2}e^{-V_y/2\sigma_y^2}
# \end{eqnarray}
# Changing variables to $\kappa\equiv \sigma_x^2/\sigma_y^2$, we have the
# following definitions
# \begin{eqnarray}
# \kappa&\equiv& \sigma_x^2/\sigma_y^2 \\\\
# \sigma_x&=&\sigma_y \kappa^{1/2} \\\\
# \sigma_y&=&\sigma_x \kappa^{-1/2}
# \end{eqnarray}
# and then transform the posterior
# \begin{eqnarray}
# p(\kappa,\sigma_x|\bvec{x},\bvec{y},I)&=&
#    p(\sigma_x,\sigma_y|\bvec{x},\bvec{y},I)\times
#    \left|\frac{\partial(\sigma_x,\sigma_y)}{\partial(\kappa,\sigma_x)}\right| \\\\
# &=&   p(\sigma_x,\sigma_y|\bvec{x},\bvec{y},I)\times
# \left| \begin{array}{cc}
#     \frac{\partial\sigma_x}{\partial \kappa} & \frac{\partial
# \sigma_x}{\partial \sigma_x}\\\\ 
#     \frac{\partial\sigma_y}{\partial \kappa} & \frac{\partial
# \sigma_y}{\partial \sigma_x} \\\\
#   \end{array}
#     \right|\\\\
# &=&   p(\sigma_x,\sigma_y|\bvec{x},\bvec{y},I)\times
# \left| \begin{array}{cc}
#     \frac{1}{2}\sigma_y \kappa^{-1/2} & 1 \\\\
#     -\frac{1}{2}\sigma_x \kappa^{-3/2} & 0 
#   \end{array}
#     \right|\\\\
# &\propto&\frac{1}{\sigma_x^{n}}\frac{\kappa^{m/2}}{\sigma_x^{m}}
# e^{-V_x/2\sigma_x^2}e^{-V_y\kappa/2\sigma_x^2} \sigma_x \kappa^{-3/2}
# \end{eqnarray}
# Now we integrate out the nuisance parameter, $\sigma_x$, to get
# 
# \begin{eqnarray}
# p(\kappa|\bvec{x},\bvec{y},I)&=&\int d\sigma_x
# p(\kappa,\sigma_x|\bvec{x},\bvec{y},I) \\\\
# &\propto& \kappa^{(m-3)/2} \int d\sigma_x \frac{1}{\sigma_x^{n+m-1}}
# e^{-(V_x+V_y\kappa)/2\sigma_x^2}
# \end{eqnarray}
# from the gaussian integral trick we get
# 
# \begin{eqnarray}
# p(\kappa|\bvec{x},\bvec{y},I)&\propto&\kappa^{(m-3)/2}
# (V_x+V_y\kappa)^{(n+m-2)/2}
# \end{eqnarray}
# 
# A more common form is found with the substitutions
# \begin{eqnarray}
# \eta &\equiv&\kappa\times \frac{(V_y/f_y)}{(V_x/f_x)} \\\\
# f_x&\equiv&n-1 \\\\
# f_y&\equiv&m-1
# \end{eqnarray}
# 
# from which it follows
# \begin{eqnarray}
# p(\eta|\bvec{x},\bvec{y},I)&\propto&
# \eta^{\frac{f_y}{2}-1} (f_x+f_y\eta)^{(f_x+f_y)/2}
# \end{eqnarray}
# which is the commonly used F distribution.
# 
# 
# 

# ---------------------

# In[8]:

from IPython.core.display import HTML


def css_styling():
    styles = open("../styles/custom.css", "r").read()
    return HTML(styles)
css_styling()

