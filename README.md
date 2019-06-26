# rsi-psd-project
Repositório do projeto da disciplina de RSI + PSD

## Como usar
- Baixe e instale o Python 2.7 e o gerenciador de pacotes pip
- Instale a lib necessária `pip install scapy` ou `C:/Python27/python.exe -m pip install -U "scapy" --user` ou
- Instale a lib necessária `pip3 install scapy`
- Instale a lib networkx 'pip install networkx' para o algoritmo de análise
- Baixe os arquivos pcap do nosso tema *Train Station* [aqui](https://drive.google.com/file/d/1YdBczL5VtOLT5C1T429q6Ovu1qHvprgh/view)
- Extraia os arquivos na raiz deste repositório
- Abra e execute o arquivo `pcap-extractor.py`

## Etapas
* [x] Criar script para ler arquivos .pcap
* [x] Criar estrutura para armazenar dados extraídos
* [x] Associar endereços MAC dos devices aos respectivos vendors >[lista](https://gist.github.com/aallan/b4bb86db86079509e6159810ae9bd3e4)<
* [x] Gerar Table 2 do artigo
* [x] Gerar arquivo .csv respectivo à Figure 01 do artigo
* [x] Gerar arquivo .csv respectivo à Figure 02 do artigo
* [x] Gerar arquivo .csv respectivo à Figure 03 a do artigo
* [x] Gerar arquivo .csv respectivo à Figure 03 b do artigo
* [x] Implementar algoritmo Adamic-Adar
* [x] Obter timestamp do scapy
* [-] Gerar Table 3
* [-] Gerar Table 4
* [-] Gerar arquivo .csv respectivo à Figure 05 a do artigo
* [-] Gerar arquivo .csv respectivo à Figure 06 a do artigo

## Comandos úteis
* Instalar spark: `pip3 install pyspark`
* Rodar Spark: `rsi-psd-project$ ../spark-2.4.3-bin-hadoop2.7/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.3 /home/rsi-psd-vm/Documents/rsi-psd-project/probe-count.py localhost:9092 subscribe probes`
* Rodar o Docker-Composer: `docker-composer up`
* Corrigir a versão do java: `sudo cp jdk.sh /etc/profile.d/ > sudo init 6`
* Rodar o ThingsBoard: `docker run -it -p 9090:9090 -p 1883:1883 -p 5683:5683/udp -v ~/.mytb-data:/data -v ~/.mytb-logs:/var/log/thingsboard --name mytb --restart always thingsboard/tb-cassandra` [doc](https://thingsboard.io/docs/user-guide/install/docker/)
* Apontar o spark para o python3 `export PYSPARK_PYTHON=python3`
* Liberar porta do KAFKA para a rede local: `sudo ufw allow <PORTA>/tcp`