# SpeculateQM: Open-Source Computational Chemistry Workflow

**SpeculateQM** is an open-source Python platform designed to optimize workflows in computational and theoretical chemistry. It provides researchers with the tools to bridge the divide between experimental and computational work, making complex tasks simpler and more intuitive.

## Key Features

- **Streamlined Automation**  
  Save time and reduce errors by automating complex setups, simulations, and folder structures.

- **Reproducible Research**  
  Effortlessly replicate and refine literature methods, ensuring confidence in your findings.

- **Comprehensive Tool Integration**  
  Leverage SpeculateQM's compatibility with software like **ORCA**, **Gaussian**, and other industry-standard tools.

- **Versatile Functionality**  
  - Develop kinetic models from experimental data  
  - Investigate molecular properties and reaction pathways  
  - Explore physical and spectroscopic characteristics in detail  

## Why Use SpeculateQM?

As a former benchtop chemist who transitioned into computational chemistry, I understand how daunting it can be to decode technical documentation or replicate computational workflows. The motivation for **SpeculateQM** arose from my own challenges while working with **Titanium Catecholates**—a project requiring computational insights to address puzzling findings with limited literature data.

SpeculateQM is designed for those like me: researchers who want to use computational methods to deepen their understanding without needing years of computational expertise. It’s a tool to help you focus on science rather than wrestling with unwieldy software setups.

Whether you're a student, a seasoned experimentalist venturing into computation, or a computational chemist seeking a more intuitive workflow, SpeculateQM empowers you to bridge the gap between experiment and theory.




## Preliminary Development Timeline and Plan of Action

This timeline outlines the planned development process for **SpeculateQM**, focusing on integrating Python libraries, establishing a user-friendly GUI, and maintaining good programming practices. Contributions from the community are welcome at every stage.

### Phase 1: Core Library Integration (Months 1-3)

~~1. **Research and Selection** (Weeks 1-2)~~(Done)  
   - Identify Python libraries essential for computational chemistry workflows:
     - Core Libraries: `PySCF`, `SciPy`, `NumPy`, `ChemPy`, `RDKit`
     - Supporting Libraries: `pandas`, `mendeleev`, `molmass`, `pybaselines`

2. **Module Creation and Testing** (Weeks 3-8)  
   - Write Python integration for each library to standardize their usage within SpeculateQM.
   - Test individual modules with sample data to ensure compatibility and robustness.
   - Connect Qt Signals and Slots to  the packages and their gui elements.

3. **Data Handling and Conversion** (Weeks 9-12)  
   - Implement standardized methods for importing, processing, and exporting data.
   - Include format compatibility (e.g., Gaussian log files, MOL files, SDF files).

---

### Phase 2: Application Architecture and GUI Development (Months 4-6)

~~1. **Define Application Structure** (Weeks 13-14)~~(DONE)  
   - Establish a modular architecture to separate backend (computations) and frontend (GUI).  
   - Use **PyQt** for the GUI framework.

2. **Design GUI Mockups** (Weeks 15-16) (In Progress)  
   - Create wireframes for major components:
     - Home screen with navigation menu
     - Workflow selection screen (e.g., thermodynamics, kinetics, spectroscopy)
     - Data visualization and result interpretation panels

3. **Develop GUI Framework** (Weeks 17-22)  
   - Implement basic navigation and functionality within the GUI.
   - Integrate PyQt components for dynamic interactions, such as dropdown menus, tabs, and file explorers.

4. **Backend Integration** (Weeks 23-24)  
   - Link the core Python modules to GUI actions.  
   - Ensure that computational workflows trigger appropriate backend processes.

---

### Phase 3: Advanced Features and SIESTA Wrapper Integration (Months 7-9)

1. **Advanced Module Development** (Weeks 25-28)  
   - Add advanced functionality:
     - Real-time TD-DFT simulations
     - Basis set optimization tools
     - Spectroscopic data analysis workflows

2. **SIESTA Wrapper Development** (Weeks 29-32)  
   - Develop a Python wrapper to handle SIESTA input/output workflows.
   - Ensure compatibility with existing SpeculateQM modules for seamless integration.

3. **Testing and Validation** (Weeks 33-36)  
   - Validate SpeculateQM’s functionality with sample data from literature.
   - Perform rigorous testing to ensure reproducibility of results.

---

### Phase 4: Community Feedback and Refinement (Months 10-12)

1. **Open Beta Release** (Weeks 37-40)  
   - Release a beta version on GitHub.
   - Encourage community contributions and feedback.

2. **Documentation and Tutorials** (Weeks 41-44)  
   - Write comprehensive documentation for users and developers.  
   - Create video tutorials and guides for common workflows.

3. **Final Release** (Weeks 45-48)  
   - Implement community-driven improvements.
   - Launch the first stable version of SpeculateQM.

---

### Contributing to SpeculateQM

Community members can contribute by:
- Suggesting features and improvements
- Testing the software on different computational tasks
- Contributing code or fixing bugs
- Writing tutorials or documenting workflows

SpeculateQM is committed to making computational chemistry accessible and efficient. Join us in building a tool that empowers chemists around the globe!
