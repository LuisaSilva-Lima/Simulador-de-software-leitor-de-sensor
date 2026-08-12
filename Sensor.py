
#def
def media(leituras):
    resultado = sum(leituras) / len(leituras)
    return resultado

print("__________ SPACE MODULE MONITORING SYSTEM __________")
print( )

#array
vibração = []
temperatura = []
latencia = []
cpu = []

# entradas 
while True:
   ciclos = int(input("Ciclos de leitura a serem registrados: "))
   if ciclos < 3:
      print("O mínimo de leituras é 3! Por favor, insira outro valor.")
   else:
    break 
#entradas "sensores"
for coleta in range(ciclos):
    for i in range(5):
        print("----- Ciclo", coleta + 1,"-----")
        vibração.append(float(input("Ponto S" + str(i + 1) +"- Leitura da vibração estrutural (g): ")))
        temperatura.append(float(input("Ponto S"+ str(i + 1) +"- Leitura da temperatura externa (°C): ")))
        latencia.append(float(input("Ponto S"+ str(i + 1) +"- Leitura da latência de comunicação (ms): ")))
        cpu.append(float(input("Ponto S"+ str(i + 1) +"- Leitura do uso de CPU do computador de bordo (%): ")))

print()
print("========== RELATÓRIO FINAL ==========")

# alertas críticos
criticas = 0
for coleta in range(ciclos):
    for i in range(5):
        p = coleta * 5 + i
        if vibração [p] > 5 or vibração [p] < -5:
            print("ALERTA: vibração estrutural crítica de",vibração [p],"g detectada no ponto S",i + 1,"(ciclo ",coleta + 1, ")!" )
            criticas += 1
        if temperatura [p] > 120 or temperatura [p] < -150:
            print("ALERTA: temperatura externa crítica de",temperatura [p],"°C detectada no ponto S",i + 1," (ciclo ", coleta + 1, ")!" )
            criticas += 1
        if latencia [p] > 800:
            print("ALERTA: latência de comunicação crítica de",latencia [p],"ms detectada no ponto S",i + 1," (ciclo", coleta + 1, ")!")
            criticas += 1
        if cpu [p] > 85:
            print("ALERTA: uso de CPU do computador de bordo crítico de",cpu [p],"% detectada no ponto S",i + 1," (ciclo", coleta + 1, ")!")
            criticas += 1
#alerta tudo normal
    if vibração [p] <= 5 and vibração [p] >= -5 and temperatura [p] <= 120 and temperatura [p] >= -150 and latencia [p] < 800 and cpu [p] < 85:
        print("Leituras dentro dos parâmetros!")

#saidas todas as leituras
print()
print("VIBRAÇÃO ESTRUTURAL -- média ->",f"{media(vibração):.2f}","g | máximo ->",max(vibração),"g | mínimo ->",min(vibração),"g.")
print("TEMPERATURA EXTERNA -- média ->",f"{media(temperatura):.2f}","°C | máximo ->",max(temperatura),"°C | mínimo ->",min(temperatura),"°C.")
print("LATÊNCIA DE COMUNICAÇÃO -- média ->",f"{media(latencia):.2f}","ms | máximo ->",max(latencia),"ms | mínimo ->",min(latencia),"ms.")
print("USO DE CPU -- média ->",f"{media(cpu):.2f}","% | máximo ->",max(cpu),"% | mínimo ->",min(cpu),"%.")

# saida estado geral 
#criticas = 0
#for coleta in range(ciclos):
#    if vibração[coleta] > 5 or vibração[coleta] < -5:
#        criticas += 1
#    if temperatura[coleta] > 120 or temperatura[coleta] < -150:
#        criticas += 1
#    if latencia[coleta] > 800:
#        criticas += 1
#    if cpu[coleta] > 85:
#        criticas += 1

porcentagem = (criticas / (ciclos * 4 * 5)) * 100
print()
if porcentagem > 30:
    print("ESTADO GERAL: RISCO ELEVADO – Acionar protocolo de emergência")
elif porcentagem > 10:
    print("ESTADO GERAL: ATENÇÃO – Monitoramento intensificado recomendado")
else: 
    print("ESTADO GERAL: NORMAL – Módulo operando dentro dos limites de segurança")

