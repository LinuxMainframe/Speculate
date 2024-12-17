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

## Project Timeline and Workflow

This section outlines the development steps and goals for the application. The focus is on creating a functional, user-friendly Qt-based application that integrates Ketcher and various Python tools/libraries for enhanced user interactivity.

### Current Progress
- **Qt Applications and Ketcher Integration**: 
  - Successfully created Qt applications and integrated Ketcher as a chemical structure editor within the application.
  - Developed ways to enable basic user interactivity with the application and tested functionality.

### Next Steps
1. **Tool and Library Integration**: 
   - Begin integrating Python tools and libraries into the application, one by one. This includes ensuring smooth communication between the GUI and each tool, as well as testing compatibility and functionality.
   - Prioritize tools based on their complexity and importance to the application's core functionality.

2. **GUI Design and Development**:
   - Move from placeholder GUI testing to designing the actual layout for the application.
   - Avoid overwhelming users with excessive menus by adopting a clean, tabbed menu layout at the top of the application (e.g., "File", "Save", and other options).
   - Implement intuitive navigation to streamline the user experience and reduce clutter.

3. **Feature Testing and Refinement**:
   - Continuously test individual features and their integration with the GUI to ensure they work as expected.
   - Make iterative adjustments to improve usability and reliability based on testing outcomes.

4. **Final Integration and Polishing**:
   - Complete the integration of all planned tools and libraries.
   - Perform thorough testing to identify and resolve any remaining issues.
   - Refine the GUI and overall application to create a polished, user-friendly experience.

### Long-Term Goals
- Ensure the application provides seamless interactivity and functionality for its intended use cases.
- Optimize the user interface to maximize efficiency and ease of use.
- Prepare the project for potential distribution or further development as needed.

By following this workflow, the application will evolve into a cohesive and robust tool that integrates key functionalities with an intuitive interface.

---
## Additional Documentation
- [Attribution](./ketcher-standalone-2.26.0/ATTRIBUTION.md): Details on Ketcher 2.26.0 Standalone package, which is used as an embedded webapp.
- [Modifications](./ketcher-standalone-2.26.0/MODIFICATIONS.md): Changes made to Ketcher 2.26.0 Standalone package to make it compatible with this project.
---

### Contributing to SpeculateQM

Community members can contribute by:
- Suggesting features and improvements
- Testing the software on different computational tasks
- Contributing code or fixing bugs
- Writing tutorials or documenting workflows

SpeculateQM is committed to making computational chemistry accessible and efficient. Join us in building a tool that empowers chemists around the globe!
