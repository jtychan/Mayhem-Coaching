import pandas as pd
import numpy as np

sheet_template = {'DAY X': ['Competition Squat', 'Competition Bench', 'Close Grip Bench', 'Accessory', 'Accessory'],
                  'Sets': ['3', '3', '3', '3', '3'],
                  'Reps': ['8', '9', '8', '12', '12'],
                  'Rpe': ['6', '6', '7', '6', '8'],
                  'Load': ['', '', '', '', ''],
                  'Comments':['', '', '', '', '']
                    }
df = pd.DataFrame(sheet_template, columns=['DAY X', 'Sets', 'Reps', 'Rpe', 'Load', 'Comments'])
print(df)