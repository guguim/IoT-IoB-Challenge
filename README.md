<h1 align="center">🧠 IoT & IoB — Detecção Facial com OpenCV<br>Challenge FIAP Care Plus 2025</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/OpenCV-4.x-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Funcional-brightgreen?style=for-the-badge">
</p>

---

## 📌 Visão Geral

Este projeto foi desenvolvido para a disciplina **Physical Computing: IoT & IoB** da FIAP, como parte da **Challenge Care Plus — 2025**.

A aplicação realiza **detecção facial em tempo real** utilizando **OpenCV + Haar Cascade**, exibindo:

- 🔲 Retângulo ao redor do rosto  
- 🧍 Identificação simples: `Rosto 1`, `Rosto 2`, …  
- 🎯 *“Landmarks” aproximados* (centro do rosto, olhos e boca)  

Tudo é processado **localmente**, sem envio de dados para servidores externos.

---

## 🎯 Objetivo do Projeto

Demonstrar uma solução de visão computacional aplicada a IoT & IoB que:

- Detecta rostos via webcam  
- Permite configurar parâmetros da detecção  
- Mostra visualmente a área detectada e pontos de interesse (landmarks)  
- Serve como prova de conceito para soluções de saúde preventiva baseadas em biometria facial

---

## 🛠 Tecnologias Utilizadas

- **Python 3.12**  
- **OpenCV (cv2)**  
- Classificador **Haar Cascade – frontalface_default**  
- Webcam integrada  
- Ambiente **Windows + VS Code**

---

## 📦 Instalação

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/guguim/IoT-IoB-Challenge.git
cd IoT-IoB-Challenge
