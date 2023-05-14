import cv2
import easyocr

# Criando um leitor de OCR para Português
reader = easyocr.Reader(['pt'])

# Iniciando a captura de vídeo
cap = cv2.VideoCapture(0)

while True:
    # Capturando o frame
    ret, frame = cap.read()

    if not ret:
        break

    # Convertendo o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Usando o leitor de OCR para extrair o texto
    result = reader.readtext(gray)

    # Imprimindo o resultado
    for detection in result:
        top_left = tuple(map(int, detection[0][0]))
        bottom_right = tuple(map(int, detection[0][2]))
        text = detection[1]
        print(f'Texto: {text}, Top Left: {top_left}, Bottom Right: {bottom_right}')

    # Mostrando o frame
    cv2.imshow('frame', frame)

    # Saindo do loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberando a captura e destruindo todas as janelas
cap.release()
cv2.destroyAllWindows()
