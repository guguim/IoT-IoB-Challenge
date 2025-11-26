# IoT & IoB — Detecção Facial com OpenCV
Challenge FIAP Care Plus 2025

## Objetivo do Projeto
Este projeto tem como finalidade implementar uma detecção facial simples utilizando OpenCV, conforme solicitado na disciplina Physical Computing: IoT & IoB da FIAP.

A aplicação executa:
- Detecção de rostos
- Identificação sequencial dos rostos detectados
- Exibição de pontos aproximados (olhos, boca e centro)
- Parâmetros da detecção exibidos na tela
- Processamento totalmente local

---

## Tecnologias Utilizadas
- Python 3.12  
- OpenCV (cv2)  
- Haar Cascade (frontalface_default.xml)  
- Webcam local  
- VS Code

---

## Dependências
Instale o OpenCV:
py -3.12 -m pip install opencv-python


---

## Como Executar
Entre na pasta do projeto e execute:
py -3.12 main.py


A câmera abrirá automaticamente.  
Pressione **Q** para encerrar.

---

## Parâmetros da Detecção
A função `detectMultiScale()` utiliza três parâmetros principais:

### scaleFactor
Controla a redução da imagem por passo.
- 1.1 – mais preciso, mais lento  
- 1.3 – recomendado  
- 1.4 – mais rápido, menos preciso  

### minNeighbors
Quantidade de verificações antes de confirmar uma detecção.
- 3 – mais sensível  
- 5 – recomendado  
- 8 – mais rigoroso  

### minSize
Tamanho mínimo para que um rosto seja detectado.
- (30, 30) – rostos distantes  
- (60, 60) – padrão  
- (100, 100) – rostos próximos  

---

## Funcionamento da Aplicação
1. Captura frames da webcam  
2. Converte para escala de cinza  
3. Executa Haar Cascade para localizar rostos  
4. Exibe:  
   - Retângulo ao redor do rosto  
   - Identificação (Rosto 1, Rosto 2…)  
   - Pontos aproximados (olhos, boca, centro)  
   - Parâmetros utilizados  

---

## Considerações Éticas (LGPD)
- Processamento totalmente local  
- Nenhum dado é armazenado  
- Nenhuma imagem é enviada para qualquer servidor  
- Uso apenas acadêmico  

---

## Integrantes
- Hugo Santos — RM553266  
- Enzo Rodrigues — RM553377  
- Rafael Cristofali — RM553521 
- Maria Júlia — RM553384




