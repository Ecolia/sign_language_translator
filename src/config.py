"""
Configuration file for the Sign Language Translator project.
"""

import os

# ==========================================================
# Project Directories
# ==========================================================

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_DIR = os.path.join(PROJECT_ROOT, "dataset")

RAW_DATA_DIR = os.path.join(DATASET_DIR, "raw")

TRAIN_DIR = os.path.join(RAW_DATA_DIR, "asl_alphabet_train")

TEST_DIR = os.path.join(RAW_DATA_DIR, "asl_alphabet_test")

PROCESSED_DATA_DIR = os.path.join(DATASET_DIR, "processed")

MODEL_DIR = os.path.join(PROJECT_ROOT, "models")

CHECKPOINT_DIR = os.path.join(MODEL_DIR, "checkpoints")

SAVED_MODEL_DIR = os.path.join(MODEL_DIR, "saved_models")

# ==========================================================
# Model Parameters
# ==========================================================

IMAGE_SIZE = (224, 224)

CHANNELS = 3

INPUT_SHAPE = (224, 224, 3)

NUM_CLASSES = 29

BATCH_SIZE = 32

EPOCHS = 20

LEARNING_RATE = 1e-4

VALIDATION_SPLIT = 0.20

SEED = 42

# ==========================================================
# MobileNetV2 Parameters
# ==========================================================

BASE_MODEL = "MobileNetV2"

WEIGHTS = "imagenet"

DROPOUT_RATE = 0.5

# ==========================================================
# Model Save Paths
# ==========================================================

BEST_MODEL_PATH = os.path.join(
    SAVED_MODEL_DIR,
    "mobilenetv2_best.keras"
)

FINAL_MODEL_PATH = os.path.join(
    SAVED_MODEL_DIR,
    "mobilenetv2_final.keras"
)

# ==========================================================
# Create Required Directories Automatically
# ==========================================================

os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
os.makedirs(CHECKPOINT_DIR, exist_ok=True)
os.makedirs(SAVED_MODEL_DIR, exist_ok=True)