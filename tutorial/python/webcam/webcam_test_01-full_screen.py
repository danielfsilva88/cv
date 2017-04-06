import cv2

# Define a janela de exibição das imagens, com tamanho manual e em tela cheia
winName = 'Janela de Teste para o SOPT'
cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(winName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Abre a webcam para captura de vídeo
cam = cv2.VideoCapture(0)

# Laço de execução infinito (até que o usuário feche com a tecla 'q' ou ESC)
while True:

    # Captura um novo quadro da webcam
    ok, frame = cam.read()
    if not ok:
        break

    # Exibe a imagem na janela existente
    cv2.imshow(winName, frame)

    # Aguarda o pressionamento de uma tecla ou 30 milisegundos
    k = cv2.waitKey(10)
    if k == ord('q') or k == ord('Q') or k == 27:
        break

# Libera a memória do programa
cam.release()
cv2.destroyAllWindows()
