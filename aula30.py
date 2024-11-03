

velocidade = 61 # velocidade atual do carro
local_carro = 101 # kilometro onde o carro está

RADAR_1 = 60
LOCAL_1 = 100 
RADAR_RANGE = 1

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Você passou no radar 1')

if carro_multado_radar_1:
    print('carros multado no radar 1')
