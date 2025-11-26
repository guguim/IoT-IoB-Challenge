<h1 align="center">🧠 IoT & IoB — Detecção Facial com OpenCV  
Challenge FIAP Care Plus 2025</h1>

---

## 📌 Objetivo do Projeto

Este projeto implementa um sistema de **detecção facial local**, utilizando **visão computacional com OpenCV**, como parte da disciplina **Physical Computing: IoT & IoB** da FIAP.

A aplicação é capaz de:

- 🔲 Detectar rostos em tempo real  
- 🧍 Identificar rostos individualmente (“Rosto 1”, “Rosto 2”…)
- 🎯 Exibir *landmarks aproximados* (olhos, boca e centro do rosto)  
- ⚙️ Mostrar parâmetros da detecção diretamente na tela  

Todo o processamento ocorre **localmente**, sem envio de dados externos.

---

## 🛠 Tecnologias Utilizadas

- **Python 3.12**  
- **OpenCV (cv2)**  
- **Haar Cascade – frontalface_default.xml**  
- **Webcam local**  
- **VS Code**

---

## 📦 Dependências

Instale o OpenCV utilizando:

```bash
py -3.12 -m pip install opencv-python

Nenhuma outra dependência externa é necessária.
▶️ Como Executar a Aplicação

    Abra o terminal na pasta do projeto

    Execute:

py -3.12 main.py

    A câmera será iniciada automaticamente

    Para encerrar, pressione Q

⚙️ Parâmetros da Detecção

(EXIGÊNCIA DIRETA DO ENUNCIADO DA PROFESSORA)

A aplicação utiliza a função detectMultiScale() com três parâmetros essenciais.
🔧 1. scaleFactor

Controla o quanto a imagem é reduzida a cada varredura.
Valor	Comportamento
1.1	mais preciso e mais lento
1.3 (recomendado)	equilíbrio entre velocidade e precisão
1.4	mais rápido e menos preciso
🔧 2. minNeighbors

Define quantas confirmações são necessárias para validar uma detecção.
Valor	Comportamento
3	muito sensível (mais detecções)
5 (recomendado)	balanceado
8	mais rigoroso (menos falsos positivos)
🔧 3. minSize

Define o tamanho mínimo do rosto analisado pelo algoritmo.
Valor	Uso
(30, 30)	detecta rostos distantes
(60, 60)	padrão recomendado
(100, 100)	apenas rostos próximos
🧩 Funcionamento da Aplicação

    A webcam captura frames continuamente

    A imagem é convertida para tons de cinza

    O Haar Cascade analisa a imagem e detecta regiões faciais

    Para cada rosto detectado:

        É desenhado um retângulo verde

        O rosto recebe um identificador (Rosto 1, Rosto 2…)

        São exibidos landmarks aproximados:

            Olho esquerdo

            Olho direito

            Lado esquerdo da boca

            Lado direito da boca

            Centro do rosto

    Todos os parâmetros usados aparecem no canto da tela

O sistema atende exatamente ao requisito da Challenge:
✔ Retângulo
✔ Identificação
✔ Landmarks simples
✔ Parâmetros da detecção apresentados
⚖️ Considerações Éticas — LGPD

    O processamento é totalmente local

    Nenhum dado é enviado para servidores

    Nenhuma imagem é armazenada

    Nenhuma biometria é salva ou utilizada para reconhecimento facial

    Uso estritamente acadêmico

Para uso real seriam necessários:

    Consentimento explícito

    Criptografia

    Controle de armazenamento

    Políticas de privacidade adequadas à LGPD

👨‍💻 Integrantes do Grupo
Nome	RM	Função
Hugo Santos	RM553266	IoT & IoB / Desenvolvimento
Enzo Rodrigues	RM553377	Desenvolvimento / Documentação
Rafael Cristofali	RM553521	Desenvolvimento / Testes
🟢 Status do Projeto

Projeto concluído, em conformidade com os requisitos da Challenge Care Plus 2025.
<p align="center"><b>FIAP — Physical Computing: IoT & IoB</b></p> ```
