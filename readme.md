# **Uso de Containers em Ambientes IoT e Nuvem na Manufatura**: Benefícios e desafios do uso de tecnologias de containers, como Docker e Kubernetes, para implementar soluções IoT em ambientes de manufatura

## Nome: João Emanuel Ricci Barbosa

## Email: <jao.emanuel@gmail.com>

<hr>

# Projeto

### O Projeto será um ambiente Kubernetes que gerenciará sensores fictícios de máquinas por meio de monitoramento desses mesmos sensores, enviando os dados para um servidor de coleta que possuirá uma fila de mensagens (RabbitMQ). Cada sensor/grupo de sensores possuirá um container que estará dentro de um cluster kubernetes, e cada node do cluster possuirá um balanceador de carga e um escalonamento automático, para evitar sobrecarga e lentidão na coleta e também na leitura de dados. Para a visualização dos dados, haverá um dashboard que irá mostrar os dados de diferentes sensores em tempo real, podendo filtrar por data, sensor, grupo de sensores. Também contará com gráficos de comparações entre períodos de tempo diferentes. 

<hr>

# Plano de desenvolvimento

## - Estudo de caso
### 17/08 - 19/08
### -> Realização da pesquisa inicial sobre o estudo de caso
### -> Definição do caso de uso

## - Protótipo
### 24/08 - 26/08
### -> Criação do código do protótipo que será somente o envio a cada X tempo aleatório para um servidor na rede local
### -> Criação da imagem Docker

## - Desenvolvimento
### 31/08 - 30/09
### -> Criação do código fonte baseado no estudo de caso
### -> Criação do servidor de mensageria AMQP/MQTT
### -> Criação do cluster Kubernetes para a orquestração dos containers (sensores/grupo de sensores) e do balanceamento de carga e autoscaling
### -> Criação do dashboard
### -> Testes

## - Artigo
### 05/10 - 14/10
### -> Criação da estrutura do artigo baseado nas normas ABNT
### -> Pesquisa de mais referências
### -> Revisão

## - Apresentação
### 19/10 - 21/10
### -> Criação da apresentação de slides para consolidar todo o progresso e resultados do desenvolvimento do projeto
