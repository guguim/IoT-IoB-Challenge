import cv2

# carrega o classificador de face frontal
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# abre a webcam
camera = cv2.VideoCapture(0)

# parâmetros da detecção 
scale_factor = 1.3
min_neighbors = 5
min_size = (60, 60)

while True:
    ret, frame = camera.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detecção de faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=scale_factor,
        minNeighbors=min_neighbors,
        minSize=min_size
    )

    # debug no terminal
    print("faces detectadas:", len(faces))

    for idx, (x, y, w, h) in enumerate(faces, start=1):
        # retângulo verde
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # identificação simples
        cv2.putText(frame, f"Rosto {idx}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # landmarks

        # centro do rosto
        center = (x + w // 2, y + h // 2)
        cv2.circle(frame, center, 5, (0, 0, 255), -1)  # bolão vermelho

        # olho esquerdo / direito (aprox.)
        left_eye = (x + int(0.30 * w), y + int(0.35 * h))
        right_eye = (x + int(0.70 * w), y + int(0.35 * h))

        # boca esquerda / direita (aprox.)
        mouth_left = (x + int(0.35 * w), y + int(0.75 * h))
        mouth_right = (x + int(0.65 * w), y + int(0.75 * h))

        # bolas amarelas
        for px, py in [left_eye, right_eye, mouth_left, mouth_right]:
            cv2.circle(frame, (px, py), 4, (0, 255, 255), -1)

    # overlay de informacoes
    cv2.putText(frame, f"scaleFactor={scale_factor}", (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, f"minNeighbors={min_neighbors}", (10, 55),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, f"minSize={min_size}", (10, 85),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.putText(frame, "Landmarks (centro, olhos, boca)", (10, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    cv2.putText(frame, "Pressione Q para sair", (10, frame.shape[0] - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 2)

    cv2.imshow("Deteccao Facial - IoT & IoB", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
