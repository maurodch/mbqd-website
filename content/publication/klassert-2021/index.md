---
abstract: 'We train a neuromorphic hardware chip to approximate the ground states
  of quantum spin models by variational energy minimization. Compared to variational
  artificial neural networks using Markov chain Monte Carlo for sample generation,
  this approach has the advantage that the neuromorphic device generates samples in
  a fast and inherently parallel fashion. We develop a training algorithm and apply
  it to the transverse field Ising model, showing good performance at moderate system
  sizes (N≤10). A systematic hyperparameter study shows that scalability to larger
  system sizes mainly depends on sample quality which is limited by parameter drifts
  on the analog neuromorphic chip. The learning performance shows a threshold behavior
  as a function of the number of variational parameters of the ansatz, with approximately
  50 hidden neurons being sufficient for representing critical ground states up to
  N=10. The 6+1-bit resolution of the network parameters does not limit the reachable
  approximation quality in the current setup. Our work provides an important step
  towards harnessing the capabilities of neuromorphic hardware for tackling the curse
  of dimensionality in quantum many-body problems. '
authors:
  - klassert
  - 'Andreas Baumbach'
  - 'Mihai A. Petrovici'
  - gaerttner
date: 2021-09-30
doi: 10.48550/arXiv.2109.15169
projects:
  - quantum-ann
publication: 'ArXiv 2109.15169'
publication_types:
  - 2
title: 'Variational learning of quantum ground states on spiking neuromorphic hardware'
---
