# The Menpo Project

The Menpo Project is a collection of high quality open-source research software developed principally by the Menpo Team. It is an end-to-end solution for 2D and 3D deformable modeling. The Menpo Project is composed of a number of components, each one designed to solve one problem:

#### Menpo (`import menpo`)
At the heart of the Menpo Project is the Python package Menpo. Menpo contains all the core functionality listed in [Motivation](./Motivation.md) in well tested, mature, stable Python package. `menpo` is the `numpy` of the Menpo Project - the foundation upon which all else is built.

#### MenpoFit (`import menpofit`)
MenpoFit contains implementations of state of the art 2D deformable models, including Active Appearance Models, Constrained Local Models, and Supervised Decent Method. Each implementation includes training and fitting code. MenpoFit is the crown jewels of the Menpo Project - most people are interested in using the Menpo Project for the `menpofit` package.
Naturally, `menpofit` is built using the building blocks found in `menpo`.

#### MenpoDetect (`import menpodetect`)
MenpoDetect contains detection methods.
`menpodetect` works on and returns images and landmarks defined in `menpo`.

#### Menpo3D (`import menpo3d`)
Menpo3D is a specialized library for working with 3D data. It is largely separate from the core `menpo` library as it has dependencies on a number of large, 3D specific projects (like VTK, mayavi, assimp) which many people using the Menpo Project would have no use for. You'll want to install `menpo3d` if you need to import and export 3D mesh data or perform advanced mesh processing.

#### Landmarker.io ([www.landmarker.io](https://www.landmarker.io))
- An interactive tool to place landmarks on images and meshes
  - Quickly landmark a single image, or organize a large annotation effort for thousands of files
