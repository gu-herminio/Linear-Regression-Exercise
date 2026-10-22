from sklearn.linear_model import LinearRegression

# Horas de estudo
x = [[1], [2], [3], [4], [5]]  # Exemplo de dados de entrada (horas de estudo)

y = [2, 4, 6, 8, 10]  # Exemplo de dados de saída (notas correspondentes)

modelo = LinearRegression()  # Criação do modelo de regressão linear
modelo.fit(x, y)  # Treinamento do modelo com os dados 

previsao = modelo.predict([[6]])  # Previsão para 6 horas de estudo
print(f"Previsão de nota para 6 horas de estudo: {previsao[0]}")  # Exibe a previsão

print("Quanto a nota aumenta por hora:", modelo.coef_[0])
print("Valor inicial da linha:", modelo.intercept_)