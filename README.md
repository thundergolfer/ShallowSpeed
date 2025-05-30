# Shallowspeed
![stability-wip](https://img.shields.io/badge/stability-work_in_progress-lightgrey.svg)

A tiny POC implementation of distributed training for sequential deep learning models.
Implemented using plain Numpy & mpi4py.

![](.github/assets/title_picture.jpg)


Currently implements:
- Sequential models / deep MLPs, training using SGD.
- Data parallel training with interleaved communication & computation, similar to PyTorch's [DistributedDataParallel](https://arxiv.org/abs/2006.15704).
- Pipeline parallel training:
  - Naive schedule without interleaved stages.
  - [Gpipe](https://arxiv.org/abs/1811.06965) schedule with interleaved FWD & interleaved BWD.
  - (soon) [PipeDream Flush](https://arxiv.org/abs/2006.09503) schedule with additional inter-FWD & BWD interleaving.
- Any combination of DP & PP algorithms.

## Setup
```bash
conda env create
pip install -e .
# M1 Macs: conda install "libblas=*=*accelerate"
python download_dataset.py
pytest
```

## Usage
```bash
# Sequential training
uv run python train.py
# Data parallel distributed training
uv run mpirun -n 4 python train.py --dp 4
# Pipeline parallel distributed training
uv run mpirun -n 4 python train.py --pp 4 --schedule naive
# Data & pipeline parallel distributed training
uv run mpirun -n 8 python train.py --dp 2 --pp 4 --schedule gpipe
```


## Internals
![](.github/assets/PP_pebble_graph.gif)
