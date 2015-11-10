# fepy

## Finite elements in python.

> Currently for computing Laplace spectra of planar domains.

Critical dependency: the [Triangle](http://dzhelil.info/triangle/) library.

Useful: Matplotlib, tkinter.

Next steps:

- [ ] Dirichlet boundary conditions
- [ ] GUI for drawing & working with planar domains
- [ ] Adaptive mesh refinement
  - [ ] Nodal sets
  - [ ] Controlling geometric sources of error
- [ ] Explicit proof-worthy error _a posteriori_ error bounds

### Files

- FE.py: Main attraction. Code for assembling finite element matrices and computing the eigenvalues/eigenfunctions of the Neumann Laplacian
- test suites: code for testing FE
- common_meshes.py: What it says on the box
- gui.py: GUI, currently not working. Hopefully get to this first thing next semester.
- Applications/ (please be warned: code here is not well-commented and depends on importing FE.py)
  - fun_shapes.py: computing and displaying eigenvalues/eigenfunctions of the Facebook cover photo shape
  - hot_spots.py: numerically testing the Hot Spots conjecture for Euclidean triangles (see [Polymath7](http://polymathprojects.org/tag/polymath7/))
  - isospectral.py: verifying isospectrality of certain Euclidean domains
  - low_eigenvalue_survey.py: compute low Neumann eigenvalues for triangles. Used to test a conjecture of Judge-Hillairet.
  - polyatest.py: test a conjecture of Polya that I am _so close_ to proving. (Broken.)
  - thin_triangle.py: compute and display eigenvalues/eigenfunctions of a triangle. edit code to change the triangle.
  - triangle_survey_gui.py: half-built GUI for displaying triangle eigenvalues and eigenfunctions. Uses tkinter and matplotlib. Currently draws a triangle and does nothing else.
