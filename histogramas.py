import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Função para calcular e exibir os histogramas conforme os requisitos
def calcular_histogramas(imagens):
    plt.figure(figsize=(16, 12))

    for i, (titulo, caminho_imagem) in enumerate(imagens.items()):
        # Construir o caminho completo da imagem
        caminho_completo = os.path.join("images", caminho_imagem)

        # Carregar a imagem em tons de cinza
        imagem = cv2.imread(caminho_completo, cv2.IMREAD_GRAYSCALE)

        if imagem is None:
            print(f"Erro ao carregar a imagem '{titulo}' em '{caminho_completo}'")
            continue

        # Calcular o histograma
        histograma, bins = np.histogram(imagem.flatten(), bins=256, range=[0, 256])

        # Calcular as probabilidades normalizadas
        p_rk = histograma / (imagem.shape[0] * imagem.shape[1])

        # Plotar a imagem
        plt.subplot(4, 2, i * 2 + 1)
        plt.imshow(imagem, cmap="gray")
        plt.title(f"Imagem: {titulo}")
        plt.axis("off")

        # Plotar o histograma
        plt.subplot(4, 2, i * 2 + 2)
        plt.bar(range(256), p_rk, color="blue", alpha=0.7)
        plt.title(f"Histograma de {titulo}")
        plt.xlabel("Níveis de Cinza")
        plt.ylabel("Probabilidade Normalizada")

    plt.tight_layout()
    plt.show()

# Dicionário com os nomes das imagens e seus títulos
imagens = {
    "Imagem Escura": "escura.png",
    "Imagem Clara": "clara.png",
    "Imagem de Baixo Contraste": "baixo_contraste.png",
    "Imagem de Alto Contraste": "alto_contraste.png"
}

# Calcular e exibir os histogramas
calcular_histogramas(imagens)
