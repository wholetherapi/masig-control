# masig-control

Reference implementation for **"Cooperative Multi-Agent Signal Control for Mixed Autonomy Corridors"** (Transportation Research Part B: Methodological).

This repository contains the complete training and evaluation pipeline used in the
paper: dataset loaders, the model, the training loop, the evaluation script and the
released metrics.

## Contents

```
configs/
  default.yaml
src/
  __init__.py
  marl.py
train.py
eval.py
results/
  metrics.md
requirements.txt
```

## Quick start

```
pip install -r requirements.txt
python train.py --config configs/default.yaml
python eval.py --checkpoint checkpoints/best.pt
```

The released checkpoint reproduces the numbers in `results/metrics.md`.

## Citation

```bibtex
@inproceedings{masig-control2026,
  title={Cooperative Multi-Agent Signal Control for Mixed Autonomy Corridors},
  booktitle={Transportation Research Part B: Methodological},
  year={2026}
  
}
```
