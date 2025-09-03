import pandas as pd

df = pd.read_csv("convocatoria.csv")
def get_emails_from_pillar(pillar_name):
    filtered = df[(df["🔗 Selecciona el Pilar al que quieres postular"] == pillar_name) &
                  (df["🔗 Selecciona el Pilar al que quieres postular (SEGUNDA OPCIÓN)"] != "Marketing")]

    return list(filtered[["✉️ Dirección de correo electrónico", "🧑Nombres y Apellidos"]].itertuples(index=False, name=None))
