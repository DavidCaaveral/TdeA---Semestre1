Proceso NumeroMagico
	// Autor: MAVH
	// Versi?n: 1.0
	// Fecha: 09/03/2026
	// Descripci?n: Verificar un n?mero m?gico
	
	// Declaraci?n de variables
	Definir nombreApostador como cadena
	Definir numeroMagic, numeroIngresado como entero
	
	// Inicializaci?n de variables
	numeroMagic=7
	numeroIngresado=0
	nombreApostador=""
	
	Escribir "---------------------------------------------"
	Escribir " EMPRESA DE APUESTAS DEL SUR"
	Escribir " SISTEMA DE APUESTAS"
	Escribir " EL N?MERO M?GICO"
	Escribir "---------------------------------------------"
	
	// Datos de entrada
	Escribir "Se?or apostador, tendr? una oportunidad para acertar"
	Escribir "Ingrese su nombre:"
	leer nombreApostador
	Escribir sin saltar "Ingrese el n?mero: "
	Leer numeroIngresado 
	
	// Proceso
	Si (numeroIngresado>numeroMagic) entonces
		Escribir "El n?mero ingresado es mayor que el n?mero m?gico"
	SiNo
		Si(numeroIngresado<numeroMagic) entonces
			Escribir "El n?mero ingresado es menor que el n?mero m?gico"
		SiNo
			Escribir "???Felicitaciones!!!", nombreApostador, " " , "Acert? el n?mero m?gico:", numeroMagic
		FinSi
	FinSi
FinProceso