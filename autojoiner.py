import time

def join_jobid(jobid):
    print(f"Intentando unir a JobId: {jobid}")
    # Aquí pondrías la lógica para unirte al servidor Roblox usando el JobId

def main():
    while True:
        with open("jobid.txt", "r") as f:
            jobid = f.read().strip()
        if jobid:
            join_jobid(jobid)
        else:
            print("No hay JobId en jobid.txt. Esperando...")
        time.sleep(5)  # Espera 5 segundos antes de volver a intentar

if __name__ == "__main__":
    main()