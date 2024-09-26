import contextlib
import os
import random
import shutil
from pathlib import Path

# Diretório atual
current_directory = str(Path(__file__).resolve().parents[0])


def split_dataset(images_folder: str, labels_folder: str):
    """
    Divide o dataset em conjuntos de `train` e `val`.
    """

    # Cria as pastas de train e val
    train_images_folder = os.path.join(f'{current_directory}/datasets', "dataset/images/train")
    val_images_folder = os.path.join(f'{current_directory}/datasets', "dataset/images/val")
    train_labels_folder = os.path.join(f'{current_directory}/datasets', "dataset/labels/train")
    val_labels_folder = os.path.join(f'{current_directory}/datasets', "dataset/labels/val")

    os.makedirs(train_images_folder, exist_ok=True)
    os.makedirs(val_images_folder, exist_ok=True)
    os.makedirs(train_labels_folder, exist_ok=True)
    os.makedirs(val_labels_folder, exist_ok=True)

    # Lista os arquivos de imagem e os embaralha
    image_files = [f for f in os.listdir(images_folder) if f.endswith('.jpg')]
    random.shuffle(image_files)

    # Divide a lista em 80% para treino e 20% para validação
    num_images = len(image_files)
    num_train = int(num_images * 0.8)
    train_image_files = image_files[:num_train]
    val_image_files = image_files[num_train:]

    # Move os arquivos de treino
    for image_file in train_image_files:
        if '.txt' in image_file:
            continue

        try:
            shutil.move(os.path.join(images_folder, image_file), os.path.join(train_images_folder, image_file))
            label_file = image_file.replace(".jpg", ".txt")
            shutil.move(os.path.join(labels_folder, label_file), os.path.join(train_labels_folder, label_file))

        except Exception as error:
            print(f"Erro ao mover {image_file}: {error}")

    # Move os arquivos de validação
    for image_file in val_image_files:
        with contextlib.suppress(Exception):
            shutil.move(os.path.join(images_folder, image_file), os.path.join(val_images_folder, image_file))
            label_file = image_file.replace(".jpg", ".txt")
            shutil.move(os.path.join(labels_folder, label_file), os.path.join(val_labels_folder, label_file))

    print("Divisão do dataset concluída.")


split_dataset('images', 'labels')