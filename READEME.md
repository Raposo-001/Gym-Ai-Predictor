# Gym-AI Predictor 🏋️‍♂️🤖

Um sistema de Inteligência Artificial para a analise da eficiencia dos meus treinos

## Como funciona:
O projeto utiliza **Machine Learning** (Random Forest) para calcular a eficiência de cada exercício com base em:
* Carga (kg)
* Repetições
* Amplitude do movimento

Inicialmente o projeto tera só esses 3 métodos de avaliaçãos, posteriormente pretendo adicionar outros 4 valores para a analise, esse código vai se basear em duas **Machine Learning** diferentes, a primeira vai fazer a análise das Cargas, Repetições e da Amplitude, com isso ela gera um valor de Eficiencia do treino, após isso, a segunda **Machine Learning** vai usar esses dados de eficiencia mais os outros 4 valores adicionais para definir quão produtivo foi o dia e o quão eficiente o músculo se desenvolveu


## Encerramento:
Decidi encerrar o desenvolvimento deste projeto após atingir o objetivo principal: dominar e aplicar os fundamentos da biblioteca Scikit-Learn.

Durante o processo, identifiquei um desafio lógico na transição entre a primeira e a segunda IA. Para que a segunda IA analisasse o treino completo, ela precisaria receber uma lista de eficiências (uma para cada exercício realizado). Como modelos de Machine Learning convencionais esperam formatos de entrada fixos e não processam listas dentro de índices de um DataFrame de forma nativa, surgiram dois caminhos:

A Solução Comum: Criar uma função simples de média aritmética.

A Solução Complexa: Estruturar um modelo que preservasse a individualidade de cada dado sem "achatar" a análise.

Como minha intenção era exercer o raciocínio lógico ao máximo e evitar soluções "fáceis" ou simplistas, percebi que continuar o projeto apenas para realizar preenchimento manual de dados (trabalho braçal) não agregaria novos desafios técnicos no momento.

O projeto cumpre seu objetivo de prova de conceito, demonstrando minha capacidade de implementar o pipeline de Machine Learning (Encoders, Train-Test Split e Avaliação de Modelos) e, principalmente, de analisar criticamente a viabilidade e a arquitetura de um software.