Logging para o relátorio:
## Resumo

## Introdução
adicionar 7 ref.
## Objetivo
Desenvolver um pipeline modular para segmentação de estruturas cerebrais em imagens de ressonância magnética (MRI) T1, comparando métodos clássicos de visão computacional (thresholding, watershed, morfologia, clustering) com abordagens modernas de deep learning (U-Net 3D). O objetivo é avaliar acurácia, robustez e aplicabilidade clínica das técnicas, com foco em navegação para estimulação magnética transcraniana (TMS), utilizando métricas quantitativas e visualização 3D interativa dos resultados.

### Targets de Interesse
O foco principal da segmentação está nas seguintes regiões anatômicas, relevantes para aplicações em TMS:
- **Giro pré-central (M1):** Região motora primária, alvo clássico para TMS em protocolos motores.
- **Córtex pré-frontal dorsolateral (DLPFC):** Região frequentemente estimulada em protocolos psiquiátricos (ex: depressão).

## Dataset
Precisei criar uma conta para fazer o download dos dados. Estou pegando apenas pelo [IBSR](https://www.nitrc.org/frs/?group_id=48), o release  IBSR V2.0 (1.5 mm) por mais que existam outras opções de releases do dataset, pois ele inclui:
    - Volumetria T1 já corregida quanto ao bias field;
    - Segmentações únicas com 43 labels de substâncias cerebrais, incluindo Cerebral Cortex (córtex cerebral), tanto branca quanto cinzenta — essenciais para extrair anatomicamente o giro pré-central (M1) e possivelmente regiões corticais como o DLPFC, via processamento adicional
Peguei o formato Analyze (.img), já que facilita a leitura via nibabel ou SimpleITK.

### IBSR V2.0 (1.5mm) - Informações Básicas
- **Número de sujeitos:** 18 (IBSR_01 a IBSR_18)
- **Modalidade:** Imagens volumétricas T1 normalizadas (Talairach, apenas rotação)
- **Resolução:**
    - X/Y: 0.837–1.0 mm
    - Slices: 1.5 mm
- **Formatos disponíveis:**
    - Analyze (.img/.hdr/.mat)
    - CMA (formato proprietário)
- **Estruturas segmentadas:** 43 regiões anatômicas, incluindo:
    - Córtex cerebral (branco/cinzento), ventrículos, cerebelo, tálamo, putamen, caudado, amígdala, hipocampo, etc.
    - Parcellation maps disponíveis (parc)
- **Arquivos por sujeito:**
    - Imagens: `images/analyze/IBSR_##_ana.img/.hdr/.mat`
    - Segmentações: `segmentation/analyze/IBSR_##_seg_ana.img/.hdr/.mat`
    - Parcellation: `segmentation/analyze/IBSR_##_parc_ana.img/.hdr/.mat`
- **Política de uso:**
    - Uso restrito a pesquisa em segmentação automática
    - Obrigatório citar: "The MR brain data sets and their manual segmentations were provided by the Center for Morphometric Analysis at Massachusetts General Hospital and are available at http://www.cma.mgh.harvard.edu/ibsr/."
    - Proibido uso para estudos morfológicos sem permissão
- **Observações:**
    - Segmentações em formato filled volume (Analyze) e outline (CMA)
    - Mapas trinary disponíveis (background, CSF, gray matter, white matter)
    - Parcellation: mapas de subdivisão cortical

### Rótulos de Interesse (Labels)

**Segmentação (`*_seg_ana.img`):**
- Córtex cerebral:
    - 3: Left-Cerebral-Cortex
    - 42: Right-Cerebral-Cortex
- Substância branca:
    - 2: Left-Cerebral-White-Matter
    - 41: Right-Cerebral-White-Matter

**Parcellation (`*_parc_ana.img`):**
- Giro pré-central (M1):
    - 8: Left-PRG (Precentral Gyrus)
    - (Verificar código para hemisfério direito, se necessário)
- DLPFC (Córtex pré-frontal dorsolateral):
    - 5: Left-F2 (Middle Frontal Gyrus)
    - (Verificar código para hemisfério direito, se necessário)

Esses valores são usados para extrair máscaras específicas das regiões de interesse. Para DLPFC, pode ser necessário combinar múltiplos rótulos do lobo frontal, conforme a definição anatômica adotada.

## Solucao
- github ou codigos.ufsc com o código da solução e, caso exista, checkpoint da rede neural
- apresentação no Google Presentation
- video no YouTube

### Workflow

#### Preprocessamento

- **Z-score normalization:** Normaliza a intensidade dos voxels para média 0 e desvio padrão 1. Facilita a comparação entre imagens e melhora a estabilidade de algoritmos de segmentação e aprendizado de máquina.

- **N4ITK bias correction:** Corrige variações lentas de intensidade (bias field) causadas por inhomogeneidades do campo magnético do scanner. Resulta em imagens com contraste mais homogêneo, essenciais para segmentação precisa.

- **Histogram equalization:** Ajusta o histograma de intensidades para melhorar o contraste global da imagem, destacando estruturas anatômicas e facilitando a segmentação.

- **Gaussian filter:** Suaviza a imagem reduzindo ruídos de alta frequência, preservando estruturas maiores. Útil para remover artefatos e pequenas variações indesejadas.

- **Anisotropic diffusion:** Reduz o ruído preservando bordas anatômicas importantes, ao contrário de filtros lineares. Ajuda a manter detalhes estruturais relevantes para segmentação.

Essas técnicas são aplicadas antes da segmentação para padronizar, limpar e realçar as imagens, aumentando a robustez e a acurácia dos métodos subsequentes.

adicionar 2 ref.

#### Clássico
adicionar 4 ref.

#### State of the Art
adicionar 4 ref.

## Resultados

## Conclusão

## Anexo (Poster)