from ultralytics import YOLO

# Carregar um modelo pré-treinado
model = YOLO("yolov8n.pt")  # yolov8n
# model = YOLO("yolov8m.pt")  # yolov8m


# Treinar o modelo com dataset customizado
results = model.train(
    data="dataset.yaml",  # path do dataset
    epochs=100,  # define quantas vezes o modelo irá passar pelo conjunto de dados durante o treino.
    imgsz=1024, # define o tamanho da imagem que será utilizado como entrada no modelo
    fliplr=0  # garante que o modelo não inverta a imagem horizontalmente ao aplicar o aumento de dados
)

# Se caso for retomar um treinamento
# results = model.train(
#    data="dataset.yaml",
#    epochs=100,
#    imgsz=1024,
#    fliplr=0,
#    resume=True  # serve para retomar o treinamento de onde ele parou
#)