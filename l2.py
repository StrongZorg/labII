import numpy as np

# Заданная матрица PP(XX, YY)
PP = np.array([[0.0, 0.1, 0.1],
               [0.3, 0.0, 0.2],
               [0.1, 0.2, 0.0]])

# Вычисление энтропии HH(YY)
def entropy(Y):
    Y = Y[Y > 0]  # Исключаем нулевые значения
    return -np.sum(Y * np.log2(Y))

# Вычисление энтропии HH(XX)
def entropy_XY(PP):
    P_X = np.sum(PP, axis=1)
    return entropy(P_X)

# Вычисление энтропии HH(XX/YY)
def conditional_entropy_X_given_Y(PP):
    P_Y = np.sum(PP, axis=0)
    P_X_given_Y = PP / (P_Y + 1e-8)  # Добавляем маленькое число для избежания деления на 0
    return np.sum(PP * np.log2(P_X_given_Y + 1e-8))

# Вычисление энтропии HH(YY/XX)
def conditional_entropy_Y_given_X(PP):
    P_X = np.sum(PP, axis=1)
    P_Y_given_X = PP / (P_X + 1e-8)
    return np.sum(PP * np.log2(P_Y_given_X + 1e-8))

# Вычисление совместной энтропии HH(XX, YY)
def joint_entropy(PP):
    return entropy(PP.flatten())

# Вычисление взаимной информации I(XX, YY)
def mutual_information(PP):
    return entropy_XY(PP) + conditional_entropy_X_given_Y(PP)

# Вычисление всех требуемых величин
HH_YY = entropy(np.sum(PP, axis=0))
HH_XX = entropy(np.sum(PP, axis=1))
HH_XX_given_YY = abs(conditional_entropy_X_given_Y(PP))
HH_YY_given_XX = abs(conditional_entropy_Y_given_X(PP))
HH_XXYY = joint_entropy(PP)
I_XXYY = mutual_information(PP)

# Вывод результатов
print("HH(YY) =", HH_YY)
print("HH(XX) =", HH_XX)
print("HH(XX/YY) =", HH_XX_given_YY)
print("HH(YY/XX) =", HH_YY_given_XX)
print("HH(XX, YY) =", HH_XXYY)
print("I(XX, YY) =", I_XXYY)