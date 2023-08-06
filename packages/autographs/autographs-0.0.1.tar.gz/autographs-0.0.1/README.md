# `autographs`
This package contains a collection of tools for making graph stuff easy.

## Installation
Simply run `pip install autographs`, and you're set! Otherwise, you can clone this repository, navigate to its root directory, and run either (or both) of:

```
    python setup.py install
    python setup.py develop
```

## Usage
Import as you normally would: `import autographs`. As an example program, we can find the faces of the dual graph induced by the counties of Iowa using a half-edge structure:

```
    from autographs.faces import HalfEdge

    # Create a new half-edge data structure.
    he = HalfEdge("./test/data/2018_19_counties/county.shp")

    # Simply iterate over the faces.
    for face in he.faces:
        print(face)
```

## Inlcuded Tools
(Check these off as they're completed)

- [x] Finding faces of planar graphs
- [ ] Complete enumeration of k-equipartitions
- [ ] Making graphs
- [ ] Grid graph stuff (?)
- [ ] Null models

## Docs
Forthcoming Overleaf documents with more information about the math we
use here.
