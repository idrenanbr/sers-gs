# GreenHome Work Assistant
Global Solution – SERS | FIAP – Ciência da Computação (2025)

## 1. Visão Geral

O **GreenHome Work Assistant** é uma solução projetada para otimizar o consumo energético em um ambiente de **home office inteligente**, integrando:

- **Análise de Dados** (Opção A)  
- **IoT Simulado** (Opção B)  
- **Energia Solar Fotovoltaica** (Opção C)

A solução identifica padrões de consumo, simula automações inteligentes e calcula impactos econômicos e ambientais, conectando tecnologia com sustentabilidade no Future at Work.

---

## 2. Estrutura do Repositório

```
data/
├── home_office_energy_30d.csv

notebooks/
├── sers_analysis_greenhome.ipynb

src/
├── iot_simulation.py

docs/
├── arquitetura_sistema.md

README.md
```

---

## 3. Dados Utilizados

O dataset está localizado em `data/home_office_energy_30d.csv`, contendo:

- 720 registros (30 dias × 24 horas)
- irradiância solar
- geração solar
- temperatura externa
- clima
- consumo por equipamento
- tarifa (ponta / fora de ponta)
- custo energético
- emissões de CO₂
- ações IoT simuladas

Dataset totalmente realista e coerente com o cenário de trabalho remoto.

---

## 4. Código e Execução

O notebook principal está em:

```
notebooks/sers_analysis_greenhome.ipynb
```

Para execução:

### ✔ No Google Colab (recomendado)
1. Abra o Colab.  
2. Importe o notebook.  
3. Execute as células na ordem.

### ✔ Localmente (Python)
```
pip install pandas matplotlib numpy
jupyter notebook
```
Então abra o notebook.

---

## 5. IoT Simulado

O arquivo `src/iot_simulation.py` contém lógica que:

- liga/desliga o ar-condicionado com base em temperatura e geração solar  
- reduz iluminação em caso de alta luz natural  
- sugere evitar consumo em horários de ponta  

---

## 6. Energia Renovável

O notebook inclui:

- comparação Solar x Rede  
- impacto da energia solar no consumo total  
- redução de CO₂  
- economia potencial

---

## 7. Vídeo de Apresentação

O vídeo deve ser publicado como **Não listado** no YouTube.

**Link do vídeo:** *inserir aqui após upload*

---

## 8. Integrantes do Grupo

- **Kaio Corrêa – RM563443**  
- **Renan Mano Otero – RM554911**

---

## 9. Conexão com o Future at Work

A solução demonstra como tecnologia, automação e sustentabilidade podem transformar ambientes remotos de trabalho, alinhando:

- eficiência energética  
- bem-estar  
- redução de custos  
- impacto ambiental reduzido  

---

## 10. Licença

Projeto acadêmico – FIAP (2025).
