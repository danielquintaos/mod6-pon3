from ultralytics import YOLO # importa da biblioteca ultralytics a função YOLO, modelo para detecção de imagens
from PIL import Image # importa da biblioteca PIL a função Image, que abre a imagem especificada

# load a pre-trained model
model = YOLO('yolov8n.pt')

# Retrain the model
model.train(data='data.yaml', epochs=1, imgsz=416)

input1 = Image.open("test/images/1616.rf.c868709931a671796794fdbb95352c5a.jpg") # abre a imagem 
input2 = Image.open("test/images/1675.rf.e3aa3f8d28d0247ef0284dd46dacc29f.jpg") # abre a imagem
inputs = [input1, input2] # organiza as imagens em forma de lista

model.val() # valida o modelo e mostra estatísticas
for input in inputs: # 'for' para predizer as imagens
    model.predict(source=input, save=True, show=True) # analisa a imagem; procura a rachadura; mostra se encontrou; salva a imagem