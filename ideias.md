## Cenário: Monitoramento Ambiental

### Sensores de Temperatura e Umidade:

1. Sensores enviam dados para o gateway.
Gateway de Névoa (no Kubernetes):

    - Pod 1: Coleta dados dos sensores.
    - Pod 2: Realiza filtragem e agregação de dados.
    - Pod 3: Publica dados processados em um tópico Kafka.

### Cluster Kubernetes:

1. Serviço de Kafka: Armazena dados em tópicos e permite que outros serviços consumam esses dados.

    - Pod de Análise: Consome dados do Kafka, realiza análises adicionais e atualiza dashboards.
    - Pod de Armazenamento: Armazena dados em bancos de dados para análise futura.