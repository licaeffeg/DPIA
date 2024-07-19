import pandas as pd
from cryptography.fernet import Fernet

# Genera una chiave per la cifratura
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def pseudonymize(value):
    encoded_value = value.encode()
    pseudonymized_value = cipher_suite.encrypt(encoded_value)
    return pseudonymized_value

# Funzione per la pseudonimizzazione di un DataFrame
def pseudonymize_dataframe(df):
    pseudonymized_df = df.copy()
    for column in pseudonymized_df.columns:
        pseudonymized_df[column] = pseudonymized_df[column].apply(lambda x: cipher_suite.encrypt(str(x).encode()))
    return pseudonymized_df

# Funzione per mappare stringhe a interi
def map_diagnosis(df, mapping_dict):
    mapped_df = df.copy()
    for column in mapping_dict.keys():
        if column in mapped_df.columns:
            mapped_df[column] = mapped_df[column].map(mapping_dict[column])
    return mapped_df

# Esempio di dati
data = {
    'Nome': ['Mario', 'Luigi', 'Giovanni'],
    'Cognome': ['Rossi', 'Verdi', 'Bianchi'],
    'Email': ['mario.rossi@example.com', 'luigi.verdi@example.com', 'giovanni.bianchi@example.com'],
    'Indirizzo': ['Via Roma 1', 'Corso Italia 22', 'Piazza Duomo 3'],
    'Abilità manuali acquisite': ['Buone', 'Scarse', 'Nulle'],
    'Linguaggio espressivo acquisito': ['Limitato', 'Buono', 'Assente'],
    'Cammino anormale': ['Presente', 'Assente', 'Presente'],
    'Movimenti stereotipati delle mani': ['Frequente', 'Raro', 'Frequente'],
    'Pattern del sonno alterati': ['Disturbi frequenti', 'Normale', 'Disturbi occasionali'],
    'Ridotta soglia del dolore': ['Si', 'No', 'Si'],
    'Ritardo di crescita': ['Moderato', 'Lieve', 'Grave'],
    'Tono muscolare': ['Ipotonia', 'Normale', 'Ipertonia'],
    'Mani e piedi piccoli e freddi': ['Sì', 'No', 'Sì'],
    'Scoliosi': ['Lieve', 'Moderata', 'Grave'],
    'Epilessia': ['Assente', 'Presente', 'Assente'],
    'Difficoltà respiratorie': ['Moderate', 'Gravi', 'Lieve'],
    'Problemi gastrointestinali': ['Frequenti', 'Occasionali', 'Assenti'],
    'Alterazioni cardiache': ['Assenti', 'Moderate', 'Gravi']
}

df = pd.DataFrame(data)

# Creazione di un dizionario di mapping per convertire le stringhe in interi
mapping_dict = {
    'Abilità manuali acquisite': {'Buone': 2, 'Scarse': 1, 'Nulle': 0},
    'Linguaggio espressivo acquisito': {'Limitato': 1, 'Buono': 2, 'Assente': 0},
    'Cammino anormale': {'Presente': 1, 'Assente': 0},
    'Movimenti stereotipati delle mani': {'Frequente': 2, 'Raro': 1, 'Assente': 0},
    'Pattern del sonno alterati': {'Disturbi frequenti': 2, 'Normale': 0, 'Disturbi occasionali': 1},
    'Ridotta soglia del dolore': {'Si': 1, 'No': 0},
    'Ritardo di crescita': {'Moderato': 1, 'Lieve': 0, 'Grave': 2},
    'Tono muscolare': {'Ipotonia': 0, 'Normale': 1, 'Ipertonia': 2},
    'Mani e piedi piccoli e freddi': {'Sì': 1, 'No': 0},
    'Scoliosi': {'Lieve': 0, 'Moderata': 1, 'Grave': 2},
    'Epilessia': {'Assente': 0, 'Presente': 1},
    'Difficoltà respiratorie': {'Moderate': 1, 'Gravi': 2, 'Lieve': 0},
    'Problemi gastrointestinali': {'Frequenti': 2, 'Occasionali': 1, 'Assenti': 0},
    'Alterazioni cardiache': {'Assenti': 0, 'Moderate': 1, 'Gravi': 2}
}

# Mappare le stringhe ai rispettivi interi
mapped_df = map_diagnosis(df, mapping_dict)

# Pseudonimizzazione del DataFrame mappato
pseudonymized_df = pseudonymize_dataframe(mapped_df)

print("Dati Mappati e Pseudonimizzati:")
print(pseudonymized_df)
