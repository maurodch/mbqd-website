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
      padding: 5%;
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
        <img src="/logos/isoquant.jpg" alt="SFB 1225 ISOQUANT">
      </a>
    </div>
    <div class="funding-cell">
      <span>We are funded by the DFG within the Collaborative Research Center ISOQUANT (SFB1225). Within this network we study entanglement in quantum fields (Project A06) and the dynamics of disordered quantum systems (Project A05) in collaboration with experimental and theoretical groups.</span>
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
      <span>We are funded by the Cluster of Excellence STRUCTURES within which we collaborate with Razvan Gurau and Christoph Schnörr on two exploratory projects.</span>
    </div>
  </div>
</div>

