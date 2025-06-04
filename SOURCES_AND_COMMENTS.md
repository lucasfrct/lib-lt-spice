# Fontes e Comentários sobre os Modelos SPICE neste Repositório

Este documento fornece informações sobre a origem e a idade relativa dos modelos SPICE encontrados neste repositório.

## Modelos Desenvolvidos Internamente (Maio 2019)

Um conjunto significativo de modelos neste repositório foi desenvolvido por **Lucas Costa (lucasfrct@gmail.com)** em **Maio de 2019**. Estes modelos estão no formato SPICE3.
Os fabricantes especificados (`Mfg=`) dentro destes modelos são a fonte primária pretendida para os parâmetros.

Estes incluem:
*   **Diodos:**
    *   `1N40XX-Spice-Model/lib/sub/1N40XX.sub` (Modelos para 1N4001 a 1N4007, Mfg: Vishay)
*   **Transistores de Potência e Uso Geral:**
    *   `2SA1943-Spice-Model/lib/sub/2SA1943.sub` (Mfg: Farchild)
    *   `2SC5200-Spice-Model/lib/sub/2SC5200.sub` (Mfg: Farchild)
    *   `BCXXX-Spice-Model/lib/sub/BCXXX.sub` (Modelos para BC546A-C, BC548A-C, BC549A-C, BC550A-C, Mfg: Philips)
    *   `TIPXXX-Sipice-Model/lib/sub/TIPXXX.sub` (Modelos para TIP41C, TIP42C, TIP147, Mfg: Farchild)
*   **Circuitos Integrados:**
    *   `LM741-Spice-Model/lib/sub/LM741.sub` (Amplificador Operacional, Mfg: Texas Instruments)

## Modelos de Transistores Adicionais (`transistores/transistores.lib`)

O arquivo `transistores/transistores.lib` contém modelos de transistores de diversas fontes e idades:

*   `2SC3281_v1 NPN`, `2SA1302_v1 PNP`:
    *   Comentário original: "*MCE 5/13/95*". Estes são modelos mais antigos, datados de 1995.
*   `2SC3281_v2 NPN`, `2SA1302_v2 PNP`:
    *   Variantes dos modelos acima. A origem e data exatas não estão especificadas nos comentários, mas presume-se que sejam contemporâneos ou modificações dos _v1.
*   `MJL3281A NPN`, `MJL1302A PNP`:
    *   Sem data ou origem explícita nos comentários. Estes são designações de transistores da ON Semiconductor.

## Recomendações para Modelos SPICE

**Para obter os modelos SPICE mais recentes, precisos e oficialmente suportados, é altamente recomendável consultar diretamente os sites dos fabricantes dos componentes.**

Muitos fabricantes fornecem modelos SPICE para seus produtos em suas seções de suporte técnico ou páginas de produtos. Devido a limitações da ferramenta, não foi possível verificar automaticamente por modelos mais recentes na web durante esta análise.

Principais fabricantes para os componentes neste repositório incluem:
*   Vishay ([www.vishay.com](https://www.vishay.com))
*   ON Semiconductor ([www.onsemi.com](https://www.onsemi.com)) - Fabricante de muitos transistores de potência, incluindo as séries MJL e TIP.
*   Nexperia ([www.nexperia.com](https://www.nexperia.com)) - Para transistores de uso geral como a série BC.
*   Texas Instruments ([www.ti.com](https://www.ti.com)) - Para circuitos integrados como o LM741.
*   Fairchild Semiconductor (agora parte da ON Semiconductor)

Ao procurar modelos, verifique a data de lançamento ou revisão do modelo e as notas de aplicação fornecidas pelo fabricante.
