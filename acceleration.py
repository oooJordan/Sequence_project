import numpy as np
import matplotlib.pyplot as plt

# Tempi di esecuzione per ogni implementazione
time_seq = 49.922596  # Tempo della versione sequenziale

# Tempi delle versioni parallele
time_cuda = 0.532722  # Tempo CUDA
time_mpi = 7.374963  # Tempo MPI (con n processi)
time_omp = 3.889557  # Tempo OpenMP (con n thread)
time_mpi_omp = 6.687764  # Tempo MPI+OMP (n processi + n thread)

# Calcolo dello Speedup (Acceleration Factor)
speedup_cuda = time_seq / time_cuda
speedup_mpi = time_seq / time_mpi
speedup_omp = time_seq / time_omp
speedup_mpi_omp = time_seq / time_mpi_omp

# Etichette per le implementazioni
implementations = ["CUDA", "MPI", "OpenMP", "MPI+OMP"]
speedup_values = [speedup_cuda, speedup_mpi, speedup_omp, speedup_mpi_omp]

# Creazione del grafico
plt.figure(figsize=(12, 8))
plt.bar(implementations, speedup_values, color=["blue", "orange", "green", "red"])

# Etichette e titolo
plt.xlabel("Implementazione")
plt.ylabel("Acceleration Factor")
plt.title("Miglioramento prestazioni rispetto alla versione Sequenziale")
plt.grid(axis='y', linestyle="--", alpha=0.7)

# Mostrare il grafico
plt.show()

