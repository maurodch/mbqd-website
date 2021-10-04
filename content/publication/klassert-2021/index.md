---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Variational learning of quantum ground states on spiking neuromorphic hardware
subtitle: ''
summary: ''
authors:
- klassert
- A. Baumbach
- M. A. Petrovici
- gaerttner

tags: ['ANN', 'neuromorphic hardware']
categories: []
date: 2021-09-30
lastmod: 2021-09-30T20:50:11.942193Z
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects:
- quantum-ann
publishDate: 2021-09-30T20:50:11.942193Z
publication_types:
- '2'
abstract: 'We train a neuromorphic hardware chip to approximate the ground states of quantum spin models by variational energy minimization. Compared to variational artificial neural networks using Markov chain Monte Carlo for sample generation, this approach has the advantage that the neuromorphic device generates samples in a fast and inherently parallel fashion. We develop a training algorithm and apply it to the transverse field Ising model, showing good performance at moderate system sizes (N≤10). A systematic hyperparameter study shows that scalability to larger system sizes mainly depends on sample quality which is limited by parameter drifts on the analog neuromorphic chip. The learning performance shows a threshold behavior as a function of the number of variational parameters of the ansatz, with approximately 50 hidden neurons being sufficient for representing critical ground states up to N=10. The 6+1-bit resolution of the network parameters does not limit the reachable approximation quality in the current setup. Our work provides an important step towards harnessing the capabilities of neuromorphic hardware for tackling the curse of dimensionality in quantum many-body problems. '
publication: 'ArXiv Preprint'
url_pdf: https://arxiv.org/pdf/2109.15169.pdf
doi: 
---
