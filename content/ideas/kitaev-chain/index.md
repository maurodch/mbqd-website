---
title: Dynamic Properties and Quench Dynamics in an Interacting Kitaev Chain with Quasi-Periodic Disorder
summary: Dynamic Properties and Quench Dynamics in an Interacting Kitaev Chain with Quasi-Periodic Disorder

# Short title used in page links (if not set, defaults to title)
# title_short: ANN

projects:
- disorder

authors:
- vahedi

# Determines ordering of projects
# weight: 4

# Optional external URL for project (replaces project detail page).
# external_link: ""

tags:
- quantum spin systems

# image:
#   caption: "Image taken from: https://physics.aps.org/articles/v7/s84"
#   focal_point: Smart

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
## Objective:
Localized edge states are a distinctive feature of topological phases in  many-body quantum systems[^1]. In Kitaev chains[^2], these localized edge modes are identified as Majorana modes. Investigating the robustness of Majorana modes under perturbations in system parameters, including possible experimental noise, is crucial. This research aims to investigate the non-equilibrium dynamics and stability of topological phases in a generalized Kitaev chain subject to both interactions and quasi-periodic disorder.  The primary focus will be on understanding the dynamical response of the system following a quantum quench, utilizing both a self-consistent mean-field approach and Density Matrix Renormalization Group (DMRG) simulations.

## Background:
The Kitaev chain is a fundamental model for topological superconductivity, notable for hosting Majorana zero modes[^2]. Previous studies have explored its ground state properties in the presence of interactions[^3] and quasi-periodic disorder[^4]. However, the combined effects of interactions and quasi-periodic disorder on the non-equilibrium dynamics remain unexplored. Understanding these dynamics, particularly following a quantum quench, is crucial for potential applications in quantum information processing and fault-tolerant quantum computing. 

## Research Questions: 
1.  How do quasi-periodic disorder and interactions affect the non-equilibrium dynamics of the Kitaev chain following a quantum quench? 
</br>We will explore how the introduction of quasi-periodic disorder and interactions impacts the dynamics of Majorana modes, focusing on periodicity and stability changes in the system's response to a quantum quench.
2.  Can the stability of topological phases be maintained or enhanced through controlled quench dynamics? 
</br>This question investigates whether critical and non-critical quenches affect the stability of topological phases differently, especially considering how quasi-periodic disorder and interaction strengths influence phase stability.
3. What are the signatures of topological phase transitions in the time evolution of the system's observables? 
</br>We will analyze how observables like Majorana modes evolve over time to identify signatures of topological phase transitions, focusing on the impact of disorder and interactions.

## Methodology:
The study will employ a combination of theoretical and computational methods, specifically:
1. Self-Consistent Mean-Field Approach
    - Develop a mean-field model incorporating both two-body interactions and quasi-periodic disorder.
    - Implement a self-consistent algorithm in Julia or Python to determine the ground state properties and initial conditions for quench dynamics.
2. Density Matrix Renormalization Group (DMRG) Simulations
    - Utilize iTensor, a powerful library written in Julia and C++, for large-scale DMRG simulations to study the time evolution of the system post-quench.
    - Benchmark the mean-field results against DMRG outcomes to ensure accuracy and reliability.

## Research Plan:
**Month 1-2:** Literature Review and Model Development
- Conduct a comprehensive literature review on Kitaev chains, topological superconductivity, and quench dynamics.
- Develop the theoretical framework for the mean-field self-consistent approach, incorporating interactions and quasi-periodic disorder.

**Month 3-4:** Mean-Field Calculations and Initial Simulations
- Implement the mean-field model computationally preferably in Julia or Python.
- Perform preliminary calculations to determine ground state properties and set up initial conditions for quench dynamics.

**Month 5-6:** DMRG Simulations and Analysis
- Conduct DMRG simulations using iTensor packkage to study the time evolution of the system following a quantum quench.
- Analyze the results to identify signatures of topological phase transitions and assess the stability of topological phases.
- Compare DMRG results with mean-field predictions to validate findings.

## Expected Outcomes:
- Detailed understanding of the dynamical response of the interacting Kitaev chain with quasi-periodic disorder following a quantum quench.
- Identification of conditions under which topological phases are stabilized or destabilized in non-equilibrium settings.
- Insights into the role of interactions and disorder in the manipulation of topological phases.

## Significance:
This research will bridge the gap between ground state studies and the dynamical properties of topological systems, providing valuable insights into the stability and manipulation of topological phases under non-equilibrium conditions. By exploring the interplay between disorder, interactions, and dynamics, this study aims to contribute to the fundamental understanding of topological phase transitions. The findings could have practical implications for the design and optimization of systems in quantum information processing, where maintaining coherent quantum states is crucial[^5].

## Resources and Tools:
- Access to high-performance computing facilities for DMRG simulations.
- Software tools for mean-field calculations and numerical simulations (preferably Julia, alternatively Python or C++).
- iTensor library for DMRG simulations (Julia or C++).


## Contact persons 
[Prof. Martin Gärttner](mailto:martin.gaerttner@uni-jena.de) and [Javad Vahedi](mailto:javad.vahedi@uni-jena.de) </br>IFTO, Friedrich-Schiller-University Jena.

### References:


[^1]: Hasan M Z and Kane C L 2010 Rev. Mod. Phy 82, 3045    
[^2]: Kitaev, A. Y. (2001). Physics-Uspekhi, 44(10S), 131-136. 
[^3]: Nunziante, G., Maiellaro, A., Guarcello, C., & Citro, R. (2024). Condensed Matter, 9(1), 20.
[^4]: Decker, K. S. C., & Karrasch, C. (2024). arXiv:2402.12897.
[^5]: Alicea, J. (2012). Reports on Progress in Physics, 75(7), 076501