# Fall Event Detection (CNN)

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white&style=flat-square)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white&style=flat-square)
![Keras](https://img.shields.io/badge/Keras-D00000?logo=keras&logoColor=white&style=flat-square)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)

Frame-level CNN baseline for classifying fall-like behavior in video data. The repository keeps the model definition in Python and leaves private videos, frames, and trained weights outside Git.

![Pipeline](assets/pipeline.png)

## What It Does

- Defines a compact CNN classifier in `src/model.py`.
- Prints the model summary from a small command-line script.
- Documents the expected local dataset layout.
- Keeps raw videos, extracted frames, and trained models out of Git.

## Architecture

![CNN architecture](assets/architecture.png)

## Layout

```text
Fall-Event-Detection-CNN/
  assets/      pipeline and architecture diagrams
  notebooks/   recorded workflow
  scripts/     model summary command
  src/         CNN model code
```

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```powershell
python scripts/model_summary.py
```

## Local Data

```text
data/
  raw/
    training/
    evaluation/
```

A common binary setup is `0 = normal`, `1 = fall`. Class labels should be documented with the dataset.

## License

Released under the [MIT License](LICENSE).
