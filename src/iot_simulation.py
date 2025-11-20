import pandas as pd

def apply_iot_logic(df):
    df = df.copy()
    df['iot_ac_action'] = df.apply(lambda r: 'ligar' if r['outdoor_temp_c']>=24 and r['solar_generation_kwh']>=r['total_consumption_kwh'] else 'desligar', axis=1)
    df['iot_light_action'] = df.apply(lambda r: 'reduzir' if r['solar_irradiance_w_m2']>500 else 'normal', axis=1)
    df['iot_tariff_save'] = df.apply(lambda r: 'evitar_uso' if r['tariff']=='ponta' else 'usar_normal', axis=1)
    return df
