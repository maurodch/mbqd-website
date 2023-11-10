---
title: Quantum Phases in a Frustrated XY Model on a 2D Honeycomb Lattice using NQS
summary: Implement a new semi-classical method for simulating spin systems offering a controlled approximation.

# Short title used in page links (if not set, defaults to title)
# title_short: ANN

projects:
- quantum-ann

authors:
- vahedi

# Determines ordering of projects
# weight: 4

# Optional external URL for project (replaces project detail page).
# external_link: ""

tags:
- neural quantum states

image:
  caption: "A possible short-range spin pairing in a resonating valence bond (RVB) stat"
  focal_point: Smart

links:
- icon: list
  icon_pack: fas
  name: All ideas
  url: /ideas
# url_code: ""
# url_pdf: ""
# url_slides: ""
# url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

math: true
---
## Introduction
Quantum many-body systems, particularly those with frustration, have been the subject of intense study due to their rich phase diagrams and their potential to host exotic quantum states. Extensive work has been done on the ground state phase diagram of the spin-$1/2$ frustrated honeycomb XY model. Varney and colleagues led the study of this model using the numerically exact diagonalization method[^1]. By focusing on the fidelity parameter within finite-size lattices, they discovered the presence of four distinct phases, bounded by three critical quantum phase transitions, within clusters of $N=24$ spin-$1/2$ particles. These phases include the N\'eel state, a spin-wave state characterized by $120\circ$ order, two intermediate phases: a quantum spin liquid (QSL) and an exotic spin-wave state. However, the use of the density matrix renormalization group (DMRG) method for numerical investigations has brought perplexing challenges and uncertainties to the field. Instead of the expected quantum spin liquid (QSL) phase, the intermediate frustration regime reveals the emergence of an antiferromagnetic Ising phase characterized by a staggered magnetization directed along the $z$-axis[^2]. In essence, the ground state phase diagram of the spin-$1/2$ frustrated honeycomb XY model remains exotic and subject to controversial interpretations. This complexity is underlined by the multitude of conflicting results and perspectives from different computational approaches and theoretical frameworks. This project aims to explore the ground state quantum phases of the spin-$1/2$ frustrated honeycomb XY lattice using state-of-the-art techniques, in particular the Neural Network Quantum States (NQS) approach. The project will use tools from quantum information theory, including concurrence, quantum discord (QD), and entanglement entropy, to gain insight into the intricate behavior of the system[^3].

## Objectives
1. Neural network quantum states (NQS): Application of NQS as a powerful computational tool to simulate the quantum ground state of the frustrated XY model[^4]. NQS provides an efficient representation of complex many-body quantum states, allowing detailed exploration of the system's behavior.
2. Quantum information tools: Use quantum information measures such as concurrence, quantum discord (QD) and entanglement entropy to quantify and characterize the entanglement and correlations within the system. These tools will provide valuable insights into the nature of quantum phases and transitions.
3. Investigation of suggested quantum spin liquid phase: Investigate the possible existence of suggested quantum spin liquid phase within the frustrated XY model. Use NQS simulations and quantum information measures to identify and characterize these phases and shed light on the underlying physics.

<p align="center">
  <img src="featured.png"">
  A possible short-range spin pairing in a resonating valence bond (RVB) state. See this interesting <a href="https://www.youtube.com/watch?v=HTzFYQCOCx0">movie</a> for more insight.
</p>

## Significance
This project contributes to a broader understanding of quantum many-body systems with frustration, providing insights into novel quantum phases and transitions. The application of advanced computational techniques combined with quantum information tools provides a unique and powerful approach to the study of complex quantum systems.

### References:
[^1]: [PRL Varney et al.](https://link.aps.org/doi/10.1103/PhysRevLett.107.077201)
[^2]: [PRL Zhu et al.](https://link.aps.org/doi/10.1103/PhysRevLett.111.257201)
[^3]: [Nature report Satoori et al.](https://doi.org/10.1038/s41598-023-43080-3)
[^4]: [Neural quantum states Schmitt et al.](https://doi.org/10.21468/scipostphyscodeb.2)