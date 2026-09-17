# <span style= "color:#CF9FFF"> Equipe

Nome: **David Neves**
<BR>
Nome: **Jhemeson Conde**
<BR>
Nome: **Samia Albuquerque**
<BR>
Nome: **Yara Vaz da Silva**
<BR>
Nome: **Ray Kelvyn**

<br><br>

# <span style= "color:#CF9FFF">Busca por interpolação 

### <span style="color:#F0B880">**MAIS PRECISO**  - **RÁPIDA**  -  **FORMULA MATEMATICA** - **DADOS UNIFORME** 

### <span style= "color:#F0B880"> **BUSCA BINARIA**  - **BUSCA LINEAR** 

### <span style= "color:#EB7083"> **INSTÁVEL** - **DADOS IRREGULARES** - **PIOR CASO** - **DIVISÃO POR ZERO** 

<br><br>

# <span style= "color:#CF9FFF"> 1. Melhor caso [.py](./src/case/melhor_caso.py) 
## Ocorre quando os dados estão **uniformemente distribuídos**, fazendo com que a fórmula de interpolação acerte a posição do elemento logo nas primeiras tentativas.

<br><br>

# <span style= "color:#CF9FFF"> 2. Medio caso [.py](./src/case/medio_caso.py)
## Situação intermediária, com dados **razoavelmente distribuídos**, mas não perfeitamente uniformes. A interpolação ainda tem vantagem sobre a busca binária, mas com estimativas menos precisas.

<br><br>
# <span style= "color:#CF9FFF">  3. Pior caso [.py](./src/case/pior_caso.py)
## Acontece quando os dados são **irregulares/não-uniformes**, fazendo a fórmula estimar posições erradas repetidamente. Nesse cenário, o algoritmo se aproxima de uma busca linear.

<br><br>

# <span style= "color:#CF9FFF"> Caso real [Detran.py](./src/detran.py)

## Aplicação prática com placas reais, convertidas em valores numéricos para permitir a busca. Na prática, um `dict` resolveria isso de forma mais simples (O(1)), mas o objetivo aqui é comparar como cada algoritmo se comporta com dados do mundo real.


