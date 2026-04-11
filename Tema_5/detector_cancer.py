"""
features= ['potential', 'crossing', 'finishing', 'heading_accuracy',
       'short_passing', 'volleys', 'dribbling', 'curve', 'free_kick_accuracy',
       'long_passing', 'ball_control', 'acceleration', 'sprint_speed',
       'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina',
       'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
       'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle',
       'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning',
       'gk_reflexes']

       
Se intentó eliminar algunas variables para mejorar la precisión del modelo, pero al hacerlo, el resultado empeoró (bajó de aproximadamente 0.8412690897596591 a 0.84027571791874067). 
Esto indica que las variables numéricas utilizadas sí aportan información importante para la predicción.
También se intentó eliminar features que parecían similares o redundantes, como shot_power, acceleration, dribbling, sliding_tackle y long_passing, pero al quitarlas el desempeño del modelo también disminuyó.
Por esta razón, se decidió mantener todas esas características. Solo se eliminaron datos que no aportan valor, como identificadores y fechas.
Las variables preferred_foot, attacking_work_rate y defensive_work_rate no se utilizaron porque son datos de tipo texto y el modelo solo trabaja con números. 
Además, su uso no haría una gran diferencia sin convertirlas previamente.
En conclusión, mantener las variables numéricas fue la mejor opción para obtener una mejor precisión.
"""
# Eliminar Features relacionados con otros similares 'shot_power', 'acceleration' , 'dribbling' ,'sliding_tackle' 
features = [
 'potential', 'crossing', 'finishing', 'heading_accuracy',
 'short_passing', 'volleys', 'curve',
 'free_kick_accuracy', 'long_passing', 'ball_control',
  'sprint_speed', 'agility', 'reactions',
 'balance','jumping', 'stamina', 'strength',
 'long_shots', 'aggression', 'interceptions', 'positioning', 'vision','standing_tackle',
  'penalties', 'marking', 'gk_diving', 'gk_handling',
 'gk_kicking', 'gk_positioning', 'gk_reflexes'
]