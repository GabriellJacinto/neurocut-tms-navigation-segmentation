# Roadmap

A segmentação precisa de estruturas cerebrais em imagens de ressonância magnética (MRI) é essencial para diversas aplicações clínicas, incluindo a estimulação magnética transcraniana (TMS). Este projeto tem como objetivo o desenvolvimento de um pipeline de segmentação cerebral que compare abordagens clássicas de visão computacional com métodos baseados em aprendizado profundo. A proposta se insere no contexto do software open-source InVesalius, mas a integração será simulada via visualizações interativas em Python. O projeto busca fortalecer a compreensão teórica e prática de técnicas clássicas e modernas de segmentação, além de promover uma análise crítica baseada em métricas quantitativas.

## **Objetivos**
1. Implementar um pipeline de segmentação de imagens cerebrais usando:
    - Técnicas **clássicas** de visão computacional (limiarização, morfologia, watershed, clustering);
    - Técnicas de **aprendizado profundo** baseadas em redes convolucionais 3D.
2. Comparar o desempenho qualitativo e quantitativo entre as abordagens;
3. Realizar a visualização 3D interativa das segmentações obtidas;
4. Produzir um relatório técnico com discussão crítica dos resultados.

## **Arquitetura do Sistema**
O sistema será modular e construído em Python, com foco em prototipação, experimentação e visualização. Ele será composto por:
1. **Pré-processamento**:
    - Normalização de intensidade (Z-score);
    - Correção de campo de bias (N4ITK);
    - Filtros clássicos (mediana, anisotropic diffusion);
    - Equalização de histograma para melhoria de contraste.
2. **Segmentação Clássica**:
    - Limiarização automática (Otsu);
    - Segmentação por regiões (Watershed);
    - Clustering (K-means para segmentação em regiões);
    - Morfologia matemática para refinamento (abertura/fechamento).
3. **Segmentação com Deep Learning**:
    - U-Net 3D pré-treinada (usando `MONAI` ou `nnU-Net`);
    - Fine-tuning opcional com subconjunto de dados públicos;
    - Avaliação com e sem uso de atlas para referência anatômica.
4. **Visualização Interativa**:
    - Exibição 3D com bibliotecas como `itkwidgets`, `nilearn` ou `vedo`;
    - Comparação lado a lado de resultados clássicos vs. deep learning.
5. **Avaliação e Validação**:
    - Métricas quantitativas: Dice Coefficient, Hausdorff Distance, Volume Similarity;
    - Análise qualitativa com inspeção visual;
    - Análise estatística de variações entre métodos.

## Datasets Utilizados
Os experimentos serão realizados com dados públicos, incluindo:
- **IBSR (Internet Brain Segmentation Repository)** – Segmentações manuais de estruturas anatômicas em T1-MRI.
- **MICCAI BraTS (subset restrito)** – Apenas para fins de comparação morfológica.
- **MNI152 template** – Como referência anatômica para visualização e alinhamento.

## **Entregáveis**
1. Código em Python do pipeline completo, com notebooks para experimentação.
2. Visualizações 3D interativas dos resultados de segmentação.
3. Relatório técnico contendo:
    - Fundamentação teórica das técnicas usadas;
    - Metodologia e justificativa das escolhas;
    - Avaliação quantitativa e análise crítica dos resultados;
    - Discussão sobre vantagens, limitações e aplicabilidade de cada abordagem.

### 🔹 **Entrega 1 – Entendimento do Problema e Coleta de Dados**

**Objetivo:** Familiarizar-se com o problema e os dados a serem usados
* **Input:**
  * Descrição do projeto
  * Links para download dos datasets (IBSR, BraTS subset, MNI template)
* **Tarefas:**
  * Estudar conceitos básicos de segmentação cerebral em MRI.
  * Baixar e explorar visualmente os datasets escolhidos.
  * Padronizar o formato (ex: NIfTI `.nii.gz`) e criar um pequeno subconjunto (\~5 amostras) para prototipagem rápida.
* **Output:**
  * Subconjunto de dados organizado localmente (ex: `/data/ibsr_sample/`)
  * Documentação sobre o formato das imagens, estruturas segmentadas, e resolução

### 🔹 **Entrega 2 – Implementação do Pré-processamento**

**Objetivo:** Normalizar e preparar os dados para segmentação
* **Input:**
  * Imagens T1w originais do dataset escolhido (IBSR ou similar)
  * Template atlas (Desikan‑Killiany / MNI)
* **Tarefas:**
  * Adquirir atlas anatômico (Desikan) contendo labels do córtex.
  * Alinhar (registro) MRI individuais ao atlas.
  * Confirmar labels de DLPFC e M1.
  * Implementar:
    * Z-score normalization (`(x - μ) / σ`)
    * N4ITK bias correction (via SimpleITK)
    * Histogram equalization (OpenCV ou scikit-image)
    * Redução de ruído (filtro Gaussiano, anisotropic diffusion)
* **Output:**
  * Imagens alinhadas com atlas
  * Labels M1 e DLPFC identificadas e salvas
  * Scripts Python com pipeline de pré-processamento (salvar imagens tratadas)
  * Visualização antes/depois para cada técnica
  * Relatório curto sobre impacto visual do pré-processamento

### 🔹 **Entrega 3 – Segmentação com Técnicas Clássicas**

**Objetivo:** Construir o pipeline com métodos clássicos de visão computacional
* **Input:**
  * Imagens pré-processadas da etapa anterior
* **Tarefas:**
  * Aplicar segmentação clássica focada em DLPFC e M1 (Otsu / morfologia dentro de bounding boxes das labels)
  * Ajustar método se necessário
  * Implementar: 
    * Limiarização de Otsu
    * Watershed com markers automáticos
    * K-means (com `scikit-learn`) aplicado a intensidades
    * Morfologia matemática para refinamento
* **Output:**
  * Comparação visual dos métodos clássicos em pelo menos 3 amostras
  * Código documentado em notebooks/scripts
  * Métricas iniciais (ex: porcentagem de voxel segmentados)
  * Segmentações clássicas limitadas às regiões de interesse (máscaras DLPFC e M1)

### 🔹 **Entrega 4 – Avaliação das Técnicas Clássicas**

**Objetivo:** Avaliar quantitativamente os métodos clássicos
* **Input:**
  * Segmentações clássicas e ground truth via atlas (IBSR tem segmentações manuais)
* **Tarefas:**
  * Calcular métricas:
    * Dice Coefficient
    * Hausdorff Distance
    * Volume Similarity
  * Visualizar overlay entre segmentação e ground truth (atlas)
* **Output:**
  * Tabela comparativa com métricas por método
  * Análise qualitativa (ex: onde cada método falha/melhora)
  * Gráficos e imagens com overlays

### 🔹 **Entrega 5 – Segmentação com Deep Learning (U-Net 3D)**

**Objetivo:** Aplicar uma rede 3D U-Net pré-treinada
* **Input:**
  * Imagens pré-processadas + masks (opcionalmente convertidas para `HDF5` ou `NIfTI` padronizado)
* **Tarefas:**
  * Usar biblioteca como `MONAI`, `nnU-Net` ou `Segmentation Models 3D`
  * Rodar inferência com pesos pré-treinados (sem treinar do zero)
  * Comparar visualmente com segmentações clássicas
* **Output:**
  * Segmentações geradas por deep learning
  * Notebook ou script para rodar inferência em lote
  * Comparação visual lado a lado com métodos clássicos

### 🔹 **Entrega 6 – Avaliação e Comparação dos Resultados**

**Objetivo:** Analisar as diferenças entre métodos clássicos e de deep learning
* **Input:**
  * Segmentações de ambas abordagens + ground truth
* **Tarefas:**
  * Calcular novamente métricas quantitativas
  * Gerar gráfico comparativo (bar plots, boxplots, heatmaps)
  * Discutir tempo de execução, robustez, interpretabilidade
* **Output:**
  * Tabela consolidada de métricas
  * Gráficos comparativos
  * Texto com análise crítica

### 🔹 **Entrega 7 – Visualização Interativa em 3D**

**Objetivo:** Construir interface para explorar as segmentações
* **Input:**
  * Segmentações finais salvas (.nii ou .npz)
* **Tarefas:**
  * Usar biblioteca como `itkwidgets`, `vedo`, `nilearn.plotting` ou `napari`
  * Permitir alternar entre diferentes métodos e slices
  * (Opcional) Marcar regiões anatômicas conhecidas
* **Output:**
  * Interface básica de visualização
  * Vídeo curto mostrando seu uso (ou GIF animado)
  * Capturas de tela para o relatório

### 🔹 **Entrega 8 – Redação e Apresentação Final**

**Objetivo:** Consolidar a experiência em um relatório técnico
* **Input:**
  * Resultados de todas as etapas anteriores
* **Tarefas:**
  * Escrever relatório com as seções:
    * Introdução teórica
    * Metodologia (pré-processamento, segmentações, avaliação)
    * Resultados (tabelas, gráficos, imagens)
    * Discussão crítica e considerações finais
  * Preparar apresentação oral ou pôster (se solicitado pela disciplina)
* **Output:**
  * Relatório técnico final (.pdf)
  * Repositório GitHub organizado com código e exemplos
  * Slides de apresentação final (PowerPoint ou PDF)

## Extensões Futuras (opcional)
Caso o tempo permita, o projeto poderá explorar:
- Integração parcial com a interface do InVesalius via simulação de plugin ou mockup;
- Implementação de fusão de múltiplos métodos (ex.: média ponderada entre segmentações clássicas e por rede).

## **Motivação Pessoal**
O projeto servirá como base para futuros trabalhos em neuroimagem e interfaces médico-computacionais. Ele também contribuirá para o aprimoramento das minhas habilidades em visão computacional, aprendizado profundo e desenvolvimento de ferramentas aplicadas à área biomédica, com vistas à participação em projetos de pós-graduação na área.
