---
# An instance of the People widget.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: blank

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 10

design:
  columns: "1"

title: Networks and Funding
subtitle:
---
<style>
  .funding-row {
    margin: 25px 5px;
  }

  .funding-cell * {
  margin: auto;
  }

  @media (min-width: 576px){
    .funding-cell {
      display: table-cell;
      vertical-align: middle;
    }

    .funding-cell:nth-child(1) {
      width: 30%;
      /*padding: 5%;*/
    }

    .funding-row {
      display: table-row;
    }

    .funding-table {
      display: table;
      border-spacing: 0.5em;
    }
  }
</style>

<div class="funding-table">
  <div class="funding-row">
    <div class="funding-cell">
      <a href="https://www.isoquant-heidelberg.de/">
        <img src="/logos/acp.jpg" alt="ACP logo Jena">
      </a>
    </div>
    <div class="funding-cell">
      <span>Martin Gärttner is a principal scientist within the <a href="https://www.acp.uni-jena.de/">Abbe Center of Photonics</a>, which bundles research activities in optics and photonics in Jena.</span>
    </div>
  </div>

  <div class="funding-row">
  <div class="funding-cell">
    <a href="https://www.noa.uni-jena.de/">
      <img src="/logos/sfb_noa.png" alt="SFB NOA">
    </a>
  </div>
  <div class="funding-cell">
    <span>We are funded by the DFG within the Collaborative Research Center NOA (SFB 1375, Nonlinear Optics down to Atomic scales). Within this collaboration, we work on characterizing and tailoring quantum states of light from unconventional sources (project A7) together with the group of René Sondenheimer.</span>
  </div>
  </div>

    <div class="funding-row">
    <div class="funding-cell">
      <a href="https://www.isoquant-heidelberg.de/">
        <img src="/logos/isoquant.jpg" alt="SFB 1225 ISOQUANT">
      </a>
    </div>
    <div class="funding-cell">
      <span>We were funded by the DFG within the Collaborative Research Center ISOQUANT (SFB1225, 2020-2024). Within this network we studied entanglement in quantum fields (Project A06) and the dynamics of disordered quantum systems (Project A05). We are still actively collaborating with the involved experimental groups in Heidelberg.</span>
    </div>
  </div>

  <div class="funding-row">
    <div class="funding-cell">
      <a href="https://www.bwstiftung.de/de/programm/quantentechnologie/">
        <img src="/logos/bw_stiftung.png" alt="Baden-Württemberg foundation">
      </a>
    </div>
    <div class="funding-cell">
      <span>We are funded by the Baden-Württemberg foundation within the competence network Quantum Technologies Baden-Württemberg, where we investigate methods for verifying quantum simulators in collaboration with the group of Alexey Ustinov at KIT.</span>
    </div>
  </div>


  <div class="funding-row">
    <div class="funding-cell">
      <a href="https://www.structures.uni-heidelberg.de/">
        <img src="/logos/structures1.png" alt="Cluster of Excellence STRUCTURES">
      </a>
    </div>
    <div class="funding-cell">
      <span>We were funded by the Cluster of Excellence STRUCTURES (2021-2023) within which we collaborated with Razvan Gurau and Christoph Schnörr on two exploratory projects.</span>
    </div>
  </div>
</div>
