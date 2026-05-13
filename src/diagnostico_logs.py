#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Induced Dependence Framework (v0.2.9).

Unified Core: Operational Diagnostics, KL-Divergence, and Dual-Clone.

Author: German Garcia --- Investigador Titular Independiente
DOI: 10.5281/zenodo.20172257
"""

from __future__ import annotations

import math
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class DeformacionObservacional:
    """Forensic diagnostic summary for a filtered observable state."""

    delta_obs_kl_regularizada: float
    kl_absoluta_dn_df: float
    entropia_filtrada: float
    varianza_perdida: float
    masa_superviviente: float


def _normal_pdf(x: np.ndarray, mu: float, sigma: float) -> np.ndarray:
    z = (x - mu) / sigma
    return np.exp(-0.5 * z * z) / (sigma * math.sqrt(2.0 * math.pi))


def _normal_survival(z: float) -> float:
    return 0.5 * math.erfc(z / math.sqrt(2.0))


def calcular_deformacion_observacional(
    mu_nat: float,
    sigma_nat: float,
    limite_filtro: float,
    epsilon: float = 1e-4,
    puntos: int = 20_000,
) -> DeformacionObservacional:
    """Cuantifica la deformacion observacional inducida por un filtro rigido.

    El diagnostico conserva dos lecturas complementarias:

    1. ``KL(D_N || D_F) = inf`` cuando el filtro elimina soporte donde
       la naturaleza aun posee masa de probabilidad. Esta lectura opera como
       alarma forense de truncamiento destructivo.
    2. ``KL(D_N || D_F_regularizada)`` con suelo estocastico ``epsilon`` para
       obtener una metrica finita y operacional en sistemas de monitoreo.
    """

    if sigma_nat <= 0:
        raise ValueError("sigma_nat must be positive")
    if not (0.0 < epsilon < 1.0):
        raise ValueError("epsilon must be between 0 and 1")
    if puntos < 1000:
        raise ValueError("puntos must be at least 1000")

    a_zscore = (limite_filtro - mu_nat) / sigma_nat
    survival = _normal_survival(a_zscore)
    if survival <= 0:
        raise ValueError("filter limit leaves no observable probability mass")

    x = np.linspace(mu_nat - 4.0 * sigma_nat, mu_nat + 4.0 * sigma_nat, puntos)
    p_n = _normal_pdf(x, mu_nat, sigma_nat)

    # Normal truncada inferiormente: p_T(x) = p_N(x) / P(X >= limite)
    # sobre el soporte retenido, y 0 fuera de el.
    p_truncada = np.where(x >= limite_filtro, p_n / survival, 0.0)

    # Lectura forense absoluta: si se elimina soporte, KL(D_N || D_F) diverge.
    kl_absoluta = math.inf if np.any((x < limite_filtro) & (p_n > 0.0)) else 0.0

    # Regularizacion operacional: se deja un suelo de ruido estocastico para
    # evitar infinitos en sistemas automatizados de monitoreo.
    p_f = np.where(
        x >= limite_filtro,
        (1.0 - epsilon) * p_truncada + epsilon * p_n,
        epsilon * p_n,
    )
    p_f /= np.trapezoid(p_f, x)

    idx = (p_n > 1e-12) & (p_f > 1e-12)
    kl_regularizada = np.trapezoid(p_n[idx] * np.log(p_n[idx] / p_f[idx]), x[idx])

    media_f = np.trapezoid(x * p_f, x)
    varianza_f = np.trapezoid(((x - media_f) ** 2) * p_f, x)
    entropia_f = -np.trapezoid(p_f[idx] * np.log(p_f[idx]), x[idx])

    return DeformacionObservacional(
        delta_obs_kl_regularizada=max(0.0, float(kl_regularizada)),
        kl_absoluta_dn_df=kl_absoluta,
        entropia_filtrada=float(entropia_f),
        varianza_perdida=max(0.0, float(sigma_nat**2 - varianza_f)),
        masa_superviviente=float(survival),
    )


def simular_sensibilidad_aduana(
    generaciones: int = 50,
    tau: float = 0.8,
    mu_base: float = 0.0,
    sigma_base: float = 1.0,
) -> pd.DataFrame:
    """Simula degradacion autogena frente a contencion activa Dual-Clone."""

    t = np.arange(generaciones)

    # Simulacion 1: colapso autogeno degradativo sin aduana.
    entropia_colapso = 1.5 / (1.0 + 0.08 * t)

    # Simulacion 2: contencion en tiempo real con lazo doble clon.
    entropia_regulada: list[float] = []
    h_actual = 1.5
    estatus_clon2: list[str] = []
    fuerza_correccion: list[float] = []
    deformaciones_kl: list[float] = []
    alarmas_forenses: list[str] = []

    os.makedirs("poster", exist_ok=True)

    for i in range(generaciones):
        # El filtro reduce la varianza del sistema de manera iterativa.
        h_actual -= 0.05 * (h_actual**0.5)

        # Correlacionar dinamicamente el limite del filtro con el desgaste entropico.
        filtro_dinamico = mu_base + (1.2 * (1.0 - (h_actual / 1.5)))

        diagnostico = calcular_deformacion_observacional(mu_base, sigma_base, filtro_dinamico)
        kl_actual = diagnostico.delta_obs_kl_regularizada

        # Arquitectura Dual-Clone: intercepcion y compensacion.
        if h_actual <= (tau + 0.15):
            alerta = "ACTIVA"
            inyector_ruido = math.sqrt(diagnostico.varianza_perdida) * 1.4142
            h_actual += inyector_ruido * 0.42 + 0.02 * math.sin(i * 1.5)
        else:
            alerta = "STANDBY"
            inyector_ruido = 0.0

        entropia_regulada.append(max(0.0, h_actual))
        estatus_clon2.append(alerta)
        fuerza_correccion.append(inyector_ruido)
        deformaciones_kl.append(kl_actual)
        alarmas_forenses.append("INFINITO" if math.isinf(diagnostico.kl_absoluta_dn_df) else "FINITO")

    reporte_df = pd.DataFrame(
        {
            "Generacion_t": t,
            "Umbral_Admisibilidad_Tau": np.full(generaciones, tau),
            "H_Colapso_Autogeno": entropia_colapso,
            "H_Regulada_DualClone": entropia_regulada,
            "Delta_Deformacion_KL_Regularizada": deformaciones_kl,
            "Alarma_Forense_KL_DN_DF": alarmas_forenses,
            "Estatus_Clon2": estatus_clon2,
            "Fuerza_Inyeccion_C2": fuerza_correccion,
        }
    )

    reporte_df.to_csv("poster/reporte_sensibilidad_forense.csv", index=False)
    return reporte_df


def main() -> None:
    print("==================================================================")
    print("      DIAGNOSTICO REGULARIZADO: INDUCED DEPENDENCE FRAMEWORK     ")
    print("                    AUTOR: GERMAN GARCIA                         ")
    print("==================================================================")

    reporte = simular_sensibilidad_aduana(generaciones=15, tau=0.8)

    print(
        reporte.to_string(
            index=False,
            columns=[
                "Generacion_t",
                "H_Colapso_Autogeno",
                "H_Regulada_DualClone",
                "Delta_Deformacion_KL_Regularizada",
                "Alarma_Forense_KL_DN_DF",
                "Estatus_Clon2",
            ],
            formatters={
                "H_Colapso_Autogeno": "{:.4f}".format,
                "H_Regulada_DualClone": "{:.4f}".format,
                "Delta_Deformacion_KL_Regularizada": "{:.4f}".format,
            },
        )
    )

    print("\n------------------------------------------------------------------")
    print("[EXITO] Diagnostico operativo con KL regularizada y alarma infinita.")
    print("[REGISTRO] Reporte forense salvado en 'poster/reporte_sensibilidad_forense.csv'.")
    print("==================================================================")


if __name__ == "__main__":
    main()

