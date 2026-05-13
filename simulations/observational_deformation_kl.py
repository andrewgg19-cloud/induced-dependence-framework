"""Compute observational deformation induced by a truncation filter.

This simulation estimates the Kullback-Leibler divergence between a natural
Gaussian state and a filtered observable state produced by rigid truncation.
It supports the selection-symmetry / induced-dependence manuscript.
"""

from __future__ import annotations

import math

import numpy as np


def calcular_deformacion_observacional(mu_nat: float, sigma_nat: float, limite_filtro: float) -> dict[str, float]:
    """
    Calcula la Divergencia de Kullback-Leibler (KL) para cuantificar
    la deformacion observacional (Delta_obs) inducida por el filtro.
    """
    if sigma_nat <= 0:
        raise ValueError("sigma_nat must be positive")

    # 1. Definir el estado natural (D_N).
    def pdf_natural(values: np.ndarray) -> np.ndarray:
        z = (values - mu_nat) / sigma_nat
        return np.exp(-0.5 * z * z) / (sigma_nat * math.sqrt(2.0 * math.pi))

    # 2. Definir el estado filtrado truncado (D_F) desde el limite hacia el infinito.
    a_zscore = (limite_filtro - mu_nat) / sigma_nat
    survival = 0.5 * math.erfc(a_zscore / math.sqrt(2.0))
    if survival <= 0:
        raise ValueError("filter limit leaves no observable probability mass")

    def pdf_filtrada(values: np.ndarray) -> np.ndarray:
        return pdf_natural(values) / survival

    # 3. Muestreo numerico para aproximar la integral de la divergencia KL.
    x = np.linspace(limite_filtro, mu_nat + 4 * sigma_nat, 10_000)

    p_n = pdf_natural(x)
    p_f = pdf_filtrada(x)

    # Evitar divisiones por cero o logaritmos indeterminados.
    idx = (p_n > 1e-10) & (p_f > 1e-10)

    # Si el filtro elimina soporte, D_KL(D_N || D_F) es infinita:
    # D_F(x) = 0 para x < limite_filtro mientras D_N(x) > 0.
    kl_natural_to_filtered = math.inf

    # La direccion finita y reproducible para medir deformacion observada es:
    # D_KL(D_F || D_N). Para una distribucion truncada inferiormente equivale
    # a log(1 / survival), porque p_F(x) = p_N(x) / survival en el soporte retenido.
    kl_filtered_to_natural = math.log(1.0 / survival)

    # 4. Calcular entropia de Shannon remanente.
    # Entropia diferencial de una normal truncada inferiormente:
    # H = log(sigma * Z * sqrt(2*pi*e)) + alpha * phi(alpha) / (2Z)
    phi_alpha = math.exp(-0.5 * a_zscore * a_zscore) / math.sqrt(2.0 * math.pi)
    entropia_filtrada = math.log(sigma_nat * survival * math.sqrt(2.0 * math.pi * math.e))
    entropia_filtrada += (a_zscore * phi_alpha) / (2.0 * survival)

    # Varianza de una normal truncada inferiormente.
    lambda_alpha = phi_alpha / survival
    var_filtrada = sigma_nat**2 * (1.0 + a_zscore * lambda_alpha - lambda_alpha**2)

    return {
        "Delta_obs_KL_DF_DN": kl_filtered_to_natural,
        "KL_DN_DF": kl_natural_to_filtered,
        "Entropia_H_DF": entropia_filtrada,
        "Varianza_Destruida": sigma_nat**2 - var_filtrada,
    }


def main() -> None:
    print("--- DIAGNOSTICO DE DEPENDENCIAS INDUCIDAS ---")
    # Simulacion de un filtro rigido: umbral de deteccion o curacion de datos de IA.
    resultado = calcular_deformacion_observacional(mu_nat=0.0, sigma_nat=1.0, limite_filtro=0.5)

    print(f"Deformacion Observacional (Delta_obs = KL[D_F || D_N]): {resultado['Delta_obs_KL_DF_DN']:.4f} nats")
    print(f"KL[D_N || D_F] por soporte eliminado:                 {resultado['KL_DN_DF']}")
    print(f"Entropia del Estado Filtrado (H[D_F]):       {resultado['Entropia_H_DF']:.4f} nats")
    print(f"Varianza Absorbida/Destruida por el Filtro:  {resultado['Varianza_Destruida']:.4f}")


if __name__ == "__main__":
    main()
