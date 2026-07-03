## Weak-winner phase synchronization: A curious case of weak interactions

This repository reproduces results from the manuscript [Phys. Rev. Research 3, 023144 (2021)](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.3.023144).

---

### Dependencies

- [Boost](https://www.boost.org) (tested with 1.67)
- [Eigen](https://eigen.tuxfamily.org) (header-only)
- CMake >= 3.5, C++17 compiler

---

### Build

1. Install Boost and Eigen, then update the include paths in `CMakeLists.txt` if they are not under `~/Downloads/`:

```cmake
include_directories(/path/to/boost/)
include_directories(/path/to/eigen3/)
```

2. Compile:

```bash
mkdir -p build && cd build
cmake ..
make
```

3. Run from the `build/` directory:

```bash
./run_me
```

---

### Cite this work

```bibtex
@article{choudhary2021weak,
  title={Weak-winner phase synchronization: A curious case of weak interactions},
  author={Choudhary, Anshul and Kumar, Sanjeev},
  journal={Physical Review Research},
  volume={3},
  number={2},
  pages={023144},
  year={2021},
  publisher={APS}
}
```

---

Visual Phase Synchronization                                                     |  Schematic
:-------------------------------------------------------------------------------:|:-------------------------:
<img src="out.gif" alt="drawing" width="600" height="400"/>             |  <img src="WW_Schematic.png" alt="drawing" width="600" height="400"/>
