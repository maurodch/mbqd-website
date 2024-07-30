---
title: High-Harmonic Generation in Spin Chains with Broken Inversion Symmetry
summary: High-Harmonic Generation in Spin Chains with Broken Inversion Symmetry

# Short title used in page links (if not set, defaults to title)
# title_short: ANN

projects:
- entanglement

authors:
- vahedi

# Determines ordering of projects
# weight: 4

# Optional external URL for project (replaces project detail page).
# external_link: ""

tags:
- high harmonic generation
- quantum spin systems

image:
  caption: "Image taken from: https://physics.aps.org/articles/v7/s84"
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
## Overview:
High-Harmonic Generation (HHG) is a non-linear optical process wherein higher multiples of the fundamental frequency of an input light are generated[^1]. While extensively studied in electronic systems, HHG in quantum spin systems remains less explored, offering novel insights into material properties and magnetic dynamics[^2][^3]. This research aims to investigate HHG within one-dimensional spin chains featuring both the XXZ interaction and the Dzyaloshinskii-Moriya Interaction (DMI), a key mechanism in systems with broken inversion symmetry[^4][^5]. Spin systems exhibiting DMI have recently attracted considerable attention in various fields, including the study of magnetised thin films [^6][^7][^8], graphene [^9], spin-1/2 ladders [^10], multiferroic phases [^11], anisotropic Heisenberg antiferromagnets [^12] and XY spin chains [^13], highlighting the broad relevance and interdisciplinary nature of research in this field.

## Background
In quantum spin systems, magnetic fields can induce dynamics leading to HHG through time-dependent magnetization changes. The inclusion of DMI adds a critical layer of complexity. DMI leads to spin canting and is crucial for understanding phenomena such as magnetic skyrmions and certain magnetoelectric effects, which are vital for spintronic applications.

## Objectives:
The primary objective of this research is to theoretically explore the effects of DMI on the HHG spectrum in one-dimensional ferromagnetic spin chains, analyzing how broken inversion symmetry influences the generation of harmonics. Specifically, the project will:
- Develop a theoretical model incorporating both XXZ and DMI interactions.
- Use numerical simulation tools to predict the HHG spectrum.
- Analyze the role of magnon excitations and their coupling due to DMI in the generation of high harmonics.

## Methodology:
The research will employ numerical simulations, particularly using exact diagonalization or time dependent Matrix product techniques [^14], to study the spin dynamics under periodic magnetic driving. Initial conditions will mimic real-world materials where DMI plays a significant role. The study will utilize Python and potentially Julia for performance-critical simulations, alongside libraries such as QuTiP[^15]/iTensors[^16] for quantum dynamics.

## Expected Outcomes:
- How DMI influences the cutoff energies in the HHG spectrum.
- The potential for phase transitions induced by high magnetic fields and their effects on the HHG.
- Insights into the spin excitation characteristics modified by DMI, enhancing the understanding of spin-based devices.

## Significance:
This research is positioned at the cutting edge of quantum materials and photonics, promising to deepen the theoretical understanding of spin dynamics in non-centrosymmetric systems and contribute to the development of next-generation magnetic materials with tailored optical properties. 


## Contact persons 
[Prof. Martin Gärttner](mailto:martin.gaerttner@uni-jena.de) and [Javad Vahedi](mailto:javad.vahedi@uni-jena.de) </br>IFTO, Friedrich-Schiller-University Jena.

### References:

[^1]: High-harmonic generation in quantum spin systems, Phys. Rev. B 99, 184303 (2019).
[^2]: Photo-induced nonequilibrium states in Mott insulators, arXiv:2310.05201
[^3]: High-harmonic generation in spin-orbit coupled systems, Phys. Rev. B 102, 081121(R) (2020).
[^4]: Anisotropic Superexchange Interaction and Weak Ferromagnetism, Phys. Rev. 120, 91 (1960).
[^5]: A thermodynamic theory of “weak” ferromagnetism of antiferromagnetics, Journal of Physics and Chemistry of Solids 4, 241-255, (1958).
[^6]: Measuring and tailoring the Dzyaloshinskii-Moriya interaction in perpendicularly magnetized thin films, Phys. Rev. B 90, 020402(R) (2014).
[^7]: Dzyaloshinskii-Moriya interaction accounting for the orientation of magnetic domains in ultrathin films: Fe/W(110), Phys. Rev. B 78, 140403(R) (2008).
[^8]: Skyrmion confinement in ultrathin film nanostructures in the presence of Dzyaloshinskii-Moriya interaction, Phys. Rev. B 88, 184422 (2013).
[^9]: Unraveling Dzyaloshinskii–Moriya Interaction and Chiral Nature of Graphene/Cobalt Interface, Nano Lett. 18, 5364 (2018).
[^10]: Emergent spin-1 Haldane gap and ferroelectricity in a frustrated spin-1/2 ladder., Phys. Rev. B 101, 140408 (2020).
[^11]: Role of the Dzyaloshinskii-Moriya interaction in multiferroic perovskites, Phys. Rev. B 73, 094434 (2006)
[^12]: Spin-1/2 anisotropic Heisenberg antiferromagnet model with Dzyaloshinskii-Moriya interaction via mean-field approximation, J. Magn. Magn. Mater. 462, 8 (2018).
[^13]: Topological phase transition of the anisotropic XY model with Dzyaloshinskii-Moriya interaction, Phys. Rev. B 98, 085136 (2018).
[^14]: Time-evolution methods for matrix-product states, Annals of Physics 411, 167998 (2019).
[^15]: https://qutip.org/
[^16]: https://itensor.org/