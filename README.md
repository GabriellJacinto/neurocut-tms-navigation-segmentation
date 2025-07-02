# Neurocut: Visão Computacional para Segmentação de Ressonância Magnética Cerebral na Navegação TMS

Este projeto explora e compara técnicas clássicas de visão computacional e abordagens de deep learning para segmentação de estruturas cerebrais em imagens de ressonância magnética ponderada em T1. O objetivo é construir um pipeline modular e interpretável que suporte tanto métodos tradicionais (ex: limiarização, watershed, morfologia) quanto redes convolucionais 3D modernas (U-Net), focando em precisão, robustez e visualização para casos de uso de neuro-navegação como Estimulação Magnética Transcraniana (TMS).

## 🎯 Objetivos do Projeto

- **Segmentação Clássica**: Implementar e avaliar técnicas tradicionais de processamento de imagem para segmentação de RM cerebral
- **Deep Learning**: Aplicar modelos 3D U-Net pré-treinados para extração de estruturas anatômicas
- **Regiões Alvo**: Focar em regiões cerebrais-chave como M1 (Córtex Motor Primário) e DLPFC (Córtex Pré-frontal Dorso-lateral)
- **Avaliação**: Comparar métodos usando métricas quantitativas (Dice, Jaccard, Hausdorff)
- **Visualização**: Criar visualizações 3D para cenários de navegação clínica

## 📁 Estrutura do Projeto

```
neurocut-tms-navigation-segmentation/
├── data/                          # Organização dos datasets
│   ├── raw/                       # Arquivos originais do dataset
│   ├── subset/                    # Amostras selecionadas para análise
│   ├── preprocessed/              # Imagens pré-processadas
│   └── classical_segmented/       # Resultados dos métodos clássicos
├── notebooks/                     # Jupyter notebooks para análise
│   ├── 0. extract_targets.ipynb           # Extração de regiões alvo
│   ├── 1. preprocessing_pipeline.ipynb    # Pré-processamento de imagens
│   ├── 2. classical_3D_segmentation.ipynb # Métodos de segmentação clássica
│   └── 3. unest_inference.ipynb           # Inferência de deep learning
├── results/                       # Arquivos de saída e métricas
│   ├── segmentation_metrics.csv   # Resultados de avaliação quantitativa
│   ├── segmentation.nii.gz       # Saídas de segmentação
│   └── *.png                     # Imagens de visualização
├── UNesT/                         # Implementação do modelo UNesT
├── utils/                         # Funções utilitárias
├── checkpoints/                   # Checkpoints dos modelos
├── docs/                          # Documentação e relatórios
├── requirements.txt               # Dependências Python
└── README.md                      # Documentação do projeto
```

## 🚀 Como Começar

### Pré-requisitos

- Python 3.8+
- GPU compatível com CUDA (recomendado para deep learning)
- RAM suficiente para processamento de imagens 3D

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositório>
   cd neurocut-tms-navigation-segmentation
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## 📊 Principais Funcionalidades

### 1. Extração de Regiões Alvo
- **M1 (Córtex Motor Primário)**: Essencial para mapeamento de função motora
- **DLPFC (Córtex Pré-frontal Dorso-lateral)**: Crítico para funções cognitivas
- Extração automatizada de regiões baseada em parcelamento
- Saída em formato NIfTI para compatibilidade clínica

### 2. Pipeline de Pré-processamento
- **Normalização Z-score** para padronização de intensidade
- **Correção de viés N4ITK** para inhomogeneidade de campo
- **Equalização de histograma** para melhoria de contraste
- **Suavização Gaussiana** para redução de ruído
- **Difusão anisotrópica** para preservação de bordas
- Capacidades de processamento em lote

### 3. Métodos de Segmentação Clássica
- **Limiarização de Otsu** para seleção automática de limiar
- **Segmentação Watershed** para separação baseada em regiões
- **Agrupamento K-means** para agrupamento baseado em intensidade
- **Operações morfológicas** para refinamento pós-processamento
- Suporte a processamento 3D com avaliação quantitativa

### 4. Integração de Deep Learning
- **Modelo UNesT** para segmentação 3D avançada
- Inferência de modelo pré-treinado
- Processamento em lote para múltiplos sujeitos
- Integração com métodos clássicos para comparação

## 📈 Métricas de Avaliação

O projeto avalia a qualidade da segmentação usando:

- **Coeficiente de Dice**: Mede a sobreposição entre predição e ground truth
- **Índice de Jaccard**: Métrica de interseção sobre união
- **Distância de Hausdorff**: Medição de precisão de borda
- **Similaridade de Volume**: Comparação quantitativa de volume

## 📋 Dependências

Principais bibliotecas utilizadas neste projeto:

- **Imagem Médica**: `nibabel`, `nilearn`, `SimpleITK`
- **Processamento de Imagem**: `scikit-image`, `opencv-python`
- **Deep Learning**: `torch`, `torchvision`, `MONAI`
- **Análise de Dados**: `numpy`, `pandas`, `scipy`
- **Visualização**: `matplotlib`, `plotly`
- **Machine Learning**: `scikit-learn`