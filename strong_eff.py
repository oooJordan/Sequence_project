import numpy as np
import matplotlib.pyplot as plt

cores_omp = np.arange(1, 21)
times_omp = np.array([
    49.116158, 25.605062, 17.140224, 13.05681, 10.528237,
    8.8469680, 7.7583830, 6.7935800, 6.183331, 5.7219870,
    5.3487020, 4.9632770, 4.7884650, 4.614897, 4.4586210,
    4.3062150, 4.1938540, 4.0592600, 4.013421, 3.8895570
])

# Dati per la versione MPI_OMP: uso 1-12 core (oltre il core 12 non ci sono dati)
cores_mpi_omp = np.arange(1, 13)
times_mpi_omp = np.array([
    49.231953, 20.177057, 12.597835, 10.84241, 9.781488,
    9.1402000, 7.8972890, 6.8967740, 7.307672, 6.687764, 
    6.4229220, 5.977238
])

# Dati per la versione MPI: uso 1-12 core (oltre il core 12 non ci sono dati)
cores_mpi = np.arange(1, 13)
times_mpi = np.array([
    51.04304, 26.222787, 17.97058, 13.548413, 11.140045,
    9.530356, 8.2076810, 7.193344, 8.1623770, 7.3749630, 
    7.138544, 6.6295770
])

# Calcolo dello Speedup Strong Scaling
eff_omp = np.clip(times_omp[0] / (times_omp * cores_omp), a_min=0, a_max=1)
eff_mpi_omp = np.clip(times_mpi_omp[0] / (times_mpi_omp * cores_mpi_omp), a_min=0, a_max=1)
eff_mpi = np.clip(times_mpi[0] / (times_mpi * cores_mpi), a_min=0, a_max=1)

# Creazione del grafico
plt.figure(figsize=(12, 7))
plt.xticks(np.arange(1, 21, 1))
plt.yticks(np.arange(0, 2, 0.05))
plt.plot(cores_omp, eff_omp, marker='o', linestyle='-', label='OMP')
plt.plot(cores_mpi_omp, eff_mpi_omp, marker='s', linestyle='-', label='MPI_OMP')
plt.plot(cores_mpi, eff_mpi, marker='^', linestyle='-', label='MPI')

plt.xlabel('Number of Processes/Threads')
plt.ylabel('Efficiency')
plt.title('Strong Scaling Efficiency')
plt.grid(True)
plt.legend()
plt.show()

