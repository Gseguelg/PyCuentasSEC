class GeneradorCUDN:
    """
    Clase para generar el Código Único de Disposiciones Normalizadas (CUDN)
    basado en la normativa para instalaciones de distribución eléctrica.
    """

    @staticmethod
    def _format_num(valor, longitud):
        """Rellena un número con ceros a la izquierda hasta alcanzar la longitud deseada (ej. nnn)."""
        return str(valor).zfill(longitud)

    @staticmethod
    def _format_decimal(valor, len_enteros=2, len_decimales=2):
        """Da formato a valores como el Diámetro (NNnn: 2 enteros, 2 decimales)."""
        valor_float = float(valor)
        enteros = int(valor_float)
        decimales = int(round((valor_float - enteros) * (10 ** len_decimales)))
        return f"{str(enteros).zfill(len_enteros)}{str(decimales).zfill(len_decimales)}"

    # ---------------------------------------------------------
    # 9.2 EMPALMES (A) - Largo: 5 caracteres
    # ---------------------------------------------------------
    @classmethod
    def empalme(cls, fases: str, tension: str, caracteristica: str, capacidad: str) -> str:
        """
        Genera CUDN para Empalmes.
        :param fases: 1 (Monofásico), 2 (Bifásico), 3 (Trifásico)
        :param tension: A (AT 15kV), B (BT), C (AT 23kV)
        :param caracteristica: A (Aéreo), S (Subterráneo)
        :param capacidad: 1 al 7 (Rango en kVA)
        """
        return f"A{fases}{tension}{caracteristica}{capacidad}"

    # ---------------------------------------------------------
    # 9.3 CÁMARAS (B) - Largo: 9 caracteres
    # ---------------------------------------------------------
    @classmethod
    def camara(cls, tension: str, material: str, ubicacion: str, volumen_dm3: int) -> str:
        """
        Genera CUDN para Cámaras.
        :param volumen_dm3: Volumen en dm3 (se formateará a 5 dígitos 'nnnnn')
        """
        vol = cls._format_num(volumen_dm3, 5)
        return f"B{tension}{material}{ubicacion}{vol}"

    # ---------------------------------------------------------
    # 9.4 CONDUCTORES (C) - Largo: 14 caracteres
    # ---------------------------------------------------------
    @classmethod
    def conductor(cls, aislacion: str, instalacion: str, construccion: str, 
                  material: str, fases: str, tension: str, 
                  seccion_fase_mm2: int, seccion_neutro_mm2: int) -> str:
        """
        Genera CUDN para Conductores.
        :param material: Ej. 'CU', 'AL', 'AS'. Debe ser de 2 caracteres.
        """
        mat = material.ljust(2, 'X')[:2] # Asegura 2 caracteres
        sec_fase = cls._format_num(seccion_fase_mm2, 3)
        sec_neu = cls._format_num(seccion_neutro_mm2, 3)
        return f"C{aislacion}{instalacion}{construccion}{mat}{fases}{tension}{sec_fase}{sec_neu}"

    # ---------------------------------------------------------
    # 9.5 CANALIZACIONES (D) - Largo: 11 caracteres
    # ---------------------------------------------------------
    @classmethod
    def canalizacion(cls, tension: str, ubicacion: str, material: str, 
                     proteccion: str, cant_ductos: int, diametro_cm: float) -> str:
        """
        Genera CUDN para Canalizaciones.
        :param diametro_cm: Diámetro en cm (se formatea a NNnn). Ej: 12.5 -> '1250'
        """
        ductos = cls._format_num(cant_ductos, 2)
        diam = cls._format_decimal(diametro_cm, 2, 2)
        return f"D{tension}{ubicacion}{material}{proteccion}{ductos}{diam}"

    # ---------------------------------------------------------
    # 9.12 TOMA TIERRA (K) - Largo: 4 caracteres
    # ---------------------------------------------------------
    @classmethod
    def toma_tierra(cls, caracteristica: str, seccion: str, electrodo: str) -> str:
        """Genera CUDN para Tomas de Tierra."""
        return f"K{caracteristica}{seccion}{electrodo}"

    # ---------------------------------------------------------
    # 9.19 TRANSFORMADORES DE DISTRIBUCIÓN (S) - Largo: 12 caracteres
    # ---------------------------------------------------------
    @classmethod
    def transformador(cls, tension_primario: str, tipo: str, caracteristica: str, 
                      cambiador: str, perdidas_kva: int, 
                      caract_constructiva: str, capacidad_kva: int) -> str:
        """
        Genera CUDN para Transformadores.
        La capacidad en kVA si es menor a 1, se indica como 0001 por norma.
        """
        perdidas = cls._format_num(perdidas_kva, 2)
        
        # Regla PDF: "Si capacidad es menor que 1 kVA, se indica 0001"
        if capacidad_kva < 1:
            capacidad_formateada = "0001"
        else:
            capacidad_formateada = cls._format_num(capacidad_kva, 4)
            
        return f"S{tension_primario}{tipo}{caracteristica}{cambiador}{perdidas}{caract_constructiva}{capacidad_formateada}"

    # ---------------------------------------------------------
    # 9.21 GENERACIÓN (U) - Largo: 19 caracteres
    # ---------------------------------------------------------
    @classmethod
    def generacion(cls, tension: str, fases: str, tipo: str, emplazamiento: str, 
                   modo_operacion: str, recurso: str, uso: str, 
                   autonomia_min: int, transf_elevador: str, ruido: str, 
                   unidad_cap: str, cantidad_cap: int) -> str:
        
        autonomia = cls._format_num(autonomia_min, 4)
        capacidad = cls._format_num(cantidad_cap, 4)
        
        return f"U{tension}{fases}{tipo}{emplazamiento}{modo_operacion}{recurso}{uso}{autonomia}{transf_elevador}{ruido}{unidad_cap}{capacidad}"


# ==========================================
# EJEMPLOS DE USO Y PRUEBAS
# ==========================================
if __name__ == "__main__":
    generador = GeneradorCUDN()

    # Ejemplo 1: Empalme Trifásico, BT, Aéreo, de 10 a 50 kVA
    cudn_empalme = generador.empalme(fases="3", tension="B", caracteristica="A", capacidad="3")
    print(f"CUDN Empalme:       {cudn_empalme} (Esperado: A3BA3)")

    # Ejemplo 2: Cámara AT, Hormigón, Calzada, 120 dm3 de volumen (Aplica pad de ceros)
    cudn_camara = generador.camara(tension="A", material="G", ubicacion="C", volumen_dm3=120)
    print(f"CUDN Cámara:        {cudn_camara} (Esperado: BAGC00120)")

    # Ejemplo 3: Conductor XLPE, Subterráneo, Cable, Cobre, Trifásico, BT, 120mm fase, 70mm neutro
    cudn_conductor = generador.conductor(aislacion="L", instalacion="S", construccion="C", 
                                         material="CU", fases="3", tension="B", 
                                         seccion_fase_mm2=120, seccion_neutro_mm2=70)
    print(f"CUDN Conductor:     {cudn_conductor} (Esperado: CLSCCU3B120070)")

    # Ejemplo 4: Canalización con decimales (Tubo PVC Schedule 40 de 10.5 cm de diámetro, 2 ductos)
    cudn_canalizacion = generador.canalizacion(tension="B", ubicacion="D", material="C", 
                                               proteccion="D", cant_ductos=2, diametro_cm=10.5)
    print(f"CUDN Canalización:  {cudn_canalizacion} (Esperado: DBDCD021050)")

    # Ejemplo 5: Transformador (probando la regla de < 1 kVA)
    cudn_trafo = generador.transformador(tension_primario="A", tipo="3", caracteristica="A", 
                                         cambiador="N", perdidas_kva=5, caract_constructiva="2", capacidad_kva=0.5)
    print(f"CUDN Transformador: {cudn_trafo} (Esperado: SA3AN0520001)")