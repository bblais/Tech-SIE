
#Statistical Inference for Everyone: Technical Supplement



This document is the technical supplement, for instructors, for [Statistical
Inference for Everyone], the introductory statistical inference textbook from
the perspective of "probability theory as logic".

<img  src="http://web.bryant.edu/~bblais/images/Saturn_with_Dice.png"
align=center width = 250px />

The purpose of this supplement is to provide a place where the comparison
between the orthodox, *frequentist*, statistical approach and the current,
*probability theory as logic*, approach is made explicit.  It is my contention
that all of the typical examples covered in introductory statistics can be
handled as equivalent examples in probability with uninformative prior
probabilities on the parameters.  I want this supplement to provide all of the
derivations for this claim.

Further, examples where the approaches are *different*, I plan I showing that
the current approach is demonstrably superior.  I also want to include computer
code and data to make clear how the current approach can be practically
accomplished.


[Statistical Inference for Everyone]: http://web.bryant.edu/~bblais/statistical-
inference-for-everyone-sie.html


Contents
------


* [**Prologue:**](http://nbviewer.ipython.org/github/bblais/Tech-
SIE/blob/master/Prologue/Prologue.ipynb) What is this document?
* [**Introduction:**](http://nbviewer.ipython.org/github/bblais/Tech-
SIE/blob/master/Introduction/Introduction.ipynb) A little history, and
introduction to the perspective taken in the book.
* [**Mean, Known Deviation:**](http://nbviewer.ipython.org/github/bblais/Tech-SI
E/blob/master/Estimating_Mean_Known_Deviation/Estimating_Mean_Known_Deviation.ip
ynb) Where we estimate the mean (i.e. true value), knowing the deviation.
* **Mean and the Deviation**
* **Proportion**
* **Difference Between Means**
* **Difference Between Deviations**
* **Difference Between Proportions**
* **Goodness of Fit**
* **Linear Regresssion**
* **Objective Priors**



---------------------


    from IPython.core.display import HTML
    
    
    def css_styling():
        styles = open("../styles/custom.css", "r").read()
        return HTML(styles)
    css_styling()




<style>
  @font-face {
    font-family: "Computer Modern";
    src: url('http://mirrors.ctan.org/fonts/cm-unicode/fonts/otf/cmunss.otf');
  }
  @font-face {
    font-family: "Computer Modern";
    src: url('http://mirrors.ctan.org/fonts/cm-unicode/fonts/otf/cmunsx.otf');
    font-weight: bold;
  }
  @font-face {
    font-family: "Computer Modern";
    src: url('http://mirrors.ctan.org/fonts/cm-unicode/fonts/otf/cmunsi.otf');
    font-style: italic, oblique;
  }
  @font-face {
    font-family: "Computer Modern";
    src: url('http://mirrors.ctan.org/fonts/cm-unicode/fonts/otf/cmunbxo.otf');
    font-weight: bold;
    font-style: italic, oblique;
  }

    div.cell{
        width:800px;
        margin-left:16% !important;
        margin-right:auto;
    }
    h1 {
        font-family: Garamond, Times, serif;
    }
    h4{
        margin-top:12px;
        margin-bottom: 3px;
       }
    div.text_cell_render{
        font-family: Garamond, Times, serif;
        line-height: 145%;
        font-size: 130%;
        width:800px;
        margin-left:auto;
        margin-right:auto;
    }
    .CodeMirror{
            font-family: "Source Code Pro", source-code-pro,Consolas, monospace;
    }
    .prompt{
        display: None;
    }
    .text_cell_render h5 {
        font-weight: 300;
        font-size: 22pt;
        color: #4057A1;
        font-style: italic;
        margin-bottom: .5em;
        margin-top: 0.5em;
        display: block;
    }
    
    .warning{
        color: rgb( 240, 20, 20 )
        }  
</style>
<script>
    MathJax.Hub.Config({
                        TeX: {
                           extensions: ["AMSmath.js"]
                           },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
                },
                displayAlign: 'center', // Change this to 'center' to center equations.
                "HTML-CSS": {
                    styles: {'.MathJax_Display': {"margin": 4}}
                }
        });
</script>



