import os
from ultralytics import YOLO
from PIL import Image
import pytesseract

# Carregar o modelo treinado
model = YOLO("runs/detect/train/weights/best.pt")
images_dir = 'images'

# Converter o PDF para imagens
images_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]

for file in images_files:

    # Fazer a predição na imagem
    results = model.predict(
        source=f'{images_dir}/{file}',
        save=True,
        show=True,
        # conf=0.1
    )

    # Classes mapeadas com os rótulos do seu dataset
    classes = ['cnpj', 'value', 'date', 'barcode']

    # Extrair as informações detectadas
    for result in results:
        for box in result.boxes:
            coords = box.xyxy[0].tolist()  # Converte o tensor para uma lista de floats
            class_id = int(box.cls[0])  # Classe detectada (CNPJ, Valor, etc.)
            confidence = box.conf[0]  # Confiança da detecção

            # Obter o rótulo da classe
            label = classes[class_id]
            print(f'Detectado: {label} com confiança {confidence:.2f}')
            print(f'Coordenadas detectadas: {coords}')

            # Abrir a imagem e cortá-la com base nas coordenadas detectadas
            img = Image.open(f'{images_dir}/{file}')
            cropped_img = img.crop((coords[0], coords[1], coords[2], coords[3]))
            cropped_img = cropped_img.convert('L')

            # Usar o Tesseract para extrair o texto da área cortada
            # extracted_text = pytesseract.image_to_string(cropped_img)
            extracted_text = pytesseract.image_to_string(cropped_img, config='--psm 6')
            print(f'Texto extraído para {label}: {extracted_text}')
