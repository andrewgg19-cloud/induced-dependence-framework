#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Induced Dependence Framework (v1.1.0).

Unified Core: Pure Variance Truncation, Hard-Sieve Discontinuity, and Analytical Plots.

Author: German Garcia --- Investigador Titular Independiente
DOI: 10.5281/zenodo.20172257
"""

from __future__ import annotations

import math
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageFont


@dataclass(frozen=True)
class DeformacionObservacional:
    """Forensic diagnostic summary for a filtered observable state."""

    delta_obs_kl_pura: float
    varianza_perdida: float
    masa_superviviente: float


def _normal_pdf(x: np.ndarray, mu: float, sigma: float) -> np.ndarray:
    z = (x - mu) / sigma
    return np.exp(-0.5 * z * z) / (sigma * math.sqrt(2.0 * math.pi))


def _normal_survival(z: float) -> float:
    return 0.5 * math.erfc(z / math.sqrt(2.0))


def _truncated_normal_variance(mu: float, sigma: float, lower_limit: float) -> tuple[float, float]:
    a = (lower_limit - mu) / sigma
    survival = _normal_survival(a)
    if survival <= 0:
        raise ValueError("filter limit leaves no observable probability mass")
    phi_a = math.exp(-0.5 * a * a) / math.sqrt(2.0 * math.pi)
    lambda_a = phi_a / survival
    variance = sigma**2 * (1.0 + a * lambda_a - lambda_a**2)
    return variance, survival


def calcular_deformacion_observacional(mu_nat: float, sigma_nat: float, limite_filtro: float) -> DeformacionObservacional:
    """Cuantifica la deformacion observacional pura.

    Si el filtro restringe el soporte de la distribucion natural, la
    divergencia KL ``D_KL(D_N || D_F)`` tiende a infinito. En este framework,
    ese infinito se conserva como indicador teorico de discontinuidad por
    filtrado rigido.
    """

    if sigma_nat <= 0:
        raise ValueError("sigma_nat must be positive")

    var_filtrada, survival = _truncated_normal_variance(mu_nat, sigma_nat, limite_filtro)

    if limite_filtro > mu_nat - 3.0 * sigma_nat:
        return DeformacionObservacional(
            delta_obs_kl_pura=math.inf,
            varianza_perdida=max(0.0, sigma_nat**2 - var_filtrada),
            masa_superviviente=float(survival),
        )

    x = np.linspace(limite_filtro, mu_nat + 4.0 * sigma_nat, 5_000)
    p_n = _normal_pdf(x, mu_nat, sigma_nat)
    p_f = p_n / survival

    idx = (p_n > 1e-9) & (p_f > 1e-9)
    kl_divergence = np.trapezoid(p_n[idx] * np.log(p_n[idx] / p_f[idx]), x[idx])

    return DeformacionObservacional(
        delta_obs_kl_pura=max(0.0, float(kl_divergence)),
        varianza_perdida=max(0.0, sigma_nat**2 - var_filtrada),
        masa_superviviente=float(survival),
    )


def _load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf",
    ]
    for candidate in candidates:
        if os.path.exists(candidate):
            return ImageFont.truetype(candidate, size=size)
    return ImageFont.load_default()


def generar_figura_deformacion() -> float:
    """Genera ``poster/deformacion_observacional.png`` sin depender de matplotlib."""

    np.random.seed(42)
    os.makedirs("poster", exist_ok=True)

    x1 = np.random.normal(0.0, 1.0, 3_000)
    x2 = np.random.normal(0.0, 1.0, 3_000)
    condicion_filtro = (x1 + x2) > 0.8
    cov_inducida = float(np.corrcoef(x1[condicion_filtro], x2[condicion_filtro])[0, 1])

    width, height = 1400, 1050
    margin_left, margin_right = 120, 70
    margin_top, margin_bottom = 125, 120
    plot_w = width - margin_left - margin_right
    plot_h = height - margin_top - margin_bottom

    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    title_font = _load_font(34, bold=True)
    label_font = _load_font(24)
    small_font = _load_font(20)

    draw.text(
        (width / 2, 35),
        "Figure 1: Induced Correlation under Informative Filtering",
        fill=(20, 30, 40),
        font=title_font,
        anchor="ma",
    )
    draw.text(
        (width / 2, 78),
        f"Emergent Correlation: {cov_inducida:.4f} (Natural Covariance = 0.0000)",
        fill=(20, 30, 40),
        font=small_font,
        anchor="ma",
    )

    x_min, x_max = -3.0, 3.0
    y_min, y_max = -3.0, 3.0

    def map_xy(x: np.ndarray | float, y: np.ndarray | float) -> tuple[np.ndarray | float, np.ndarray | float]:
        px = margin_left + ((x - x_min) / (x_max - x_min)) * plot_w
        py = margin_top + (1.0 - ((y - y_min) / (y_max - y_min))) * plot_h
        return px, py

    # Grid and axes.
    draw.rectangle((margin_left, margin_top, margin_left + plot_w, margin_top + plot_h), outline=(30, 30, 30), width=2)
    for value in range(-3, 4):
        px, _ = map_xy(value, 0)
        _, py = map_xy(0, value)
        draw.line((px, margin_top, px, margin_top + plot_h), fill=(225, 225, 225), width=1)
        draw.line((margin_left, py, margin_left + plot_w, py), fill=(225, 225, 225), width=1)

    px0, py0 = map_xy(0, 0)
    draw.line((px0, margin_top, px0, margin_top + plot_h), fill=(80, 80, 80), width=2)
    draw.line((margin_left, py0, margin_left + plot_w, py0), fill=(80, 80, 80), width=2)

    # Scatter points.
    for x, y, keep in zip(x1, x2, condicion_filtro):
        if x < x_min or x > x_max or y < y_min or y > y_max:
            continue
        px, py = map_xy(float(x), float(y))
        if keep:
            color = (0, 210, 220)
            radius = 3
        else:
            color = (165, 165, 165)
            radius = 2
        draw.ellipse((px - radius, py - radius, px + radius, py + radius), fill=color)

    # Filter boundary: x2 = 0.8 - x1.
    line_x = np.linspace(-2.5, 2.5, 100)
    points = [map_xy(float(x), float(0.8 - x)) for x in line_x]
    draw.line(points, fill=(210, 30, 30), width=4)

    draw.text((width / 2, height - 72), "X1 (Intrinsic Feature Space)", fill=(20, 30, 40), font=label_font, anchor="ma")
    draw.text((38, height / 2), "X2", fill=(20, 30, 40), font=label_font, anchor="mm")
    draw.rectangle((900, 145, 1320, 245), fill=(255, 255, 255), outline=(80, 80, 80))
    draw.ellipse((925, 170, 945, 190), fill=(165, 165, 165))
    draw.text((955, 163), "Eliminated Support (D_N)", fill=(20, 30, 40), font=small_font)
    draw.ellipse((925, 208, 945, 228), fill=(0, 210, 220))
    draw.text((955, 201), "Observable State (D_F)", fill=(20, 30, 40), font=small_font)
    draw.line((925, 242, 945, 242), fill=(210, 30, 30), width=4)
    draw.text((955, 233), "Filter Boundary (F=1)", fill=(20, 30, 40), font=small_font)

    out = "poster/deformacion_observacional.png"
    img.save(out)
    print(f"[GRAFICO] '{out}' generado exitosamente.")
    return cov_inducida


def simular_sensibilidad_aduana(
    generaciones: int = 50,
    tau: float = 0.8,
    mu_base: float = 0.0,
    sigma_base: float = 1.0,
) -> pd.DataFrame:
    """Simula sensibilidad secuencial frente a discontinuidad Hard-Sieve."""

    t = np.arange(generaciones)

    # Simulacion 1: colapso autogeno degradativo sin aduana.
    entropia_colapso = 1.5 / (1.0 + 0.08 * t)

    # Simulacion 2: contencion en tiempo real con lazo doble clon.
    entropia_regulada: list[float] = []
    h_actual = 1.5
    estatus_clon2: list[str] = []
    fuerza_correccion: list[float] = []
    deformaciones_kl: list[float] = []

    os.makedirs("poster", exist_ok=True)

    for i in range(generaciones):
        # El filtro reduce la varianza del sistema de manera iterativa.
        h_actual -= 0.05 * (h_actual**0.5)

        # Correlacionar dinamicamente el limite del filtro con el desgaste entropico.
        filtro_dinamico = mu_base + (1.2 * (1.0 - (h_actual / 1.5)))

        diagnostico_admon = calcular_deformacion_observacional(mu_base, sigma_base, filtro_dinamico)
        kl_actual = diagnostico_admon.delta_obs_kl_pura

        if math.isinf(kl_actual) or h_actual <= (tau + 0.15):
            alerta = "ACTIVA"
            inyector_ruido = math.sqrt(diagnostico_admon.varianza_perdida) * 1.4142
            h_actual += inyector_ruido * 0.45 + 0.02 * math.sin(i * 1.5)
        else:
            alerta = "STANDBY"
            inyector_ruido = 0.0

        entropia_regulada.append(max(0.0, h_actual))
        estatus_clon2.append(alerta)
        fuerza_correccion.append(inyector_ruido)
        deformaciones_kl.append("inf" if math.isinf(kl_actual) else f"{kl_actual:.6f}")

    reporte_df = pd.DataFrame(
        {
            "Generacion_t": t,
            "Umbral_Tau": np.full(generaciones, tau),
            "H_Colapso_Autogeno": entropia_colapso,
            "H_Regulada_DualClone": entropia_regulada,
            "Delta_Deformacion_KL_Pura": deformaciones_kl,
            "Estatus_Clon2": estatus_clon2,
            "Fuerza_Inyeccion_C2": fuerza_correccion,
        }
    )

    reporte_df.to_csv("poster/reporte_sensibilidad_forense.csv", index=False)
    return reporte_df


def main() -> None:
    print("==================================================================")
    print("       DIAGNOSTICO PURO: INDUCED DEPENDENCE FRAMEWORK (v1.1.0)   ")
    print("==================================================================")

    generar_figura_deformacion()
    reporte = simular_sensibilidad_aduana(generaciones=10, tau=0.8)

    print(
        reporte.to_string(
            index=False,
            columns=[
                "Generacion_t",
                "H_Colapso_Autogeno",
                "H_Regulada_DualClone",
                "Delta_Deformacion_KL_Pura",
                "Estatus_Clon2",
            ],
            formatters={
                "H_Colapso_Autogeno": "{:.4f}".format,
                "H_Regulada_DualClone": "{:.4f}".format,
            },
        )
    )

    print("\n------------------------------------------------------------------")
    print("[REGISTRO] Reporte forense salvado sin infinitos maquillados.")
    print("==================================================================")


if __name__ == "__main__":
    main()
