import cv2

# Carregar o classificador Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Abrir webcam
camera = cv2.VideoCapture(0)

# Parâmetros ajustáveis (você vai mostrar isso no vídeo)
scale_factor = 1.3       # Quanto a imagem é reduzida em cada escala
min_neighbors = 5         # Quanto maior, menos falsos positivos
min_size = (60, 60)       # Tamanho mínimo do rosto detectado

while True:
    ret, frame = camera.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=scale_factor,
        minNeighbors=min_neighbors,
        minSize=min_size
    )

    # Desenhar retângulos nas faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.putText(frame, f'scaleFactor={scale_factor}', (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, f'minNeighbors={min_neighbors}', (10, 55),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Deteccao Facial - IoT & IoB", frame)

    # Q para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
