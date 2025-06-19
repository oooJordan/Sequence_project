import numpy as np
import matplotlib.pyplot as plt

# Numero di processi/thread disponibili (1-20)
num_processes = np.arange(1, 21)

# Tempo di esecuzione della versione sequenziale
time_seq = 49.922596  # Modifica con il tempo reale della tua versione sequenziale

# Tempi delle versioni parallele
time_mpi = [51.04304, 26.222787, 17.97058, 13.548413, 11.140045, 9.530356, 8.207681, 7.193344, 8.162377, 7.374963, 
            7.138544, 6.629577, None, None, None, None, None, None, None, None]

time_mpi_omp = [49.231953, 20.177057, 12.597835, 10.84241, 9.781488, 9.1402, 7.897289, 6.896774, 7.307672, 6.687764, 
                6.422922, 5.977238, None, None, None, None, None, None, None, None]

time_omp = [49.116158, 25.605062, 17.140224, 13.05681, 10.528237, 8.846968, 7.758383, 6.79358, 6.183331, 5.721987, 
            5.348702, 4.963277, 4.788465, 4.614897, 4.458621, 4.306215, 4.193854, 4.05926, 4.013421, 3.889557]

# Calcolo dello speedup per ogni algoritmo (escludendo valori NULL)
speedup_mpi = [time_seq / t if t is not None else None for t in time_mpi]
speedup_mpi_omp = [time_seq / t if t is not None else None for t in time_mpi_omp]
speedup_omp = [time_seq / t if t is not None else None for t in time_omp]

# Creazione del grafico
plt.figure(figsize=(12, 8))
plt.xticks(np.arange(1, 21, 1))  # Mostra solo numeri interi da 1 a 20
plt.yticks(np.arange(1,21, 1))
# Disegna le curve per MPI, MPI+OMP e OpenMP
plt.plot(num_processes[:len(speedup_mpi)], speedup_mpi, marker='o', linestyle='-', label="Speedup MPI", color="blue")
plt.plot(num_processes[:len(speedup_mpi_omp)], speedup_mpi_omp, marker='s', linestyle='-', label="Speedup MPI+OMP", color="green")
plt.plot(num_processes, speedup_omp, marker='^', linestyle='-', label="Speedup OMP", color="orange")

# Aggiunta della linea dello speedup ideale (S = P)
plt.plot(num_processes, num_processes, linestyle="--", color="red", label="Ideal Speedup (S = P)")

# Impostazioni del grafico
plt.xlabel("Number of Processes/Threads")
plt.ylabel("Speedup")
plt.title("Strong Scaling Speedup")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)

# Mostrare il grafico
plt.show()
