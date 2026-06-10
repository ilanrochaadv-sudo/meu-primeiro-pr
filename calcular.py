"""Calculadora de honorários advocatícios."""

PERCENTUAL_MINIMO = 0.10  # 10% conforme OAB


def calcular_honorario(valor_causa: float) -> float:
    """Retorna o honorário mínimo sugerido para o valor da causa."""
    if valor_causa <= 0:
        raise ValueError("O valor da causa deve ser positivo.")
    return valor_causa * PERCENTUAL_MINIMO


if __name__ == "__main__":
    valor = float(input("Informe o valor da causa (R$): "))
    honorario = calcular_honorario(valor)
    print(f"Honorário mínimo sugerido: R$ {honorario:,.2f}")
