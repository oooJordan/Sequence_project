# Sequence_project

**Progetto multicore per l’elaborazione parallela di sequenze**, realizzato per il corso di **Programmazione Multicore** – Università La Sapienza.

A partire dal codice base `align.c`, sono state sviluppate e confrontate 4 versioni parallele sfruttando diverse tecnologie:

- **MPI** – Parallelismo distribuito
- **OpenMP** – Parallelismo condiviso (multithreading)
- **MPI + OpenMP** – Ibrido
- **CUDA** – Parallelismo su GPU

---

##  Obiettivo

L’obiettivo è confrontare approcci paralleli all’elaborazione di sequenze (es. DNA/proteine) partendo da una versione sequenziale.  
Le versioni implementano lo stesso algoritmo di base (presumibilmente *sequence alignment*, tipo Needleman-Wunsch o simili), parallelizzato con diversi paradigmi.

---

## Compilazione
```bash
- `mpicc` (MPI)
- `gcc` (OpenMP)
- `nvcc` (CUDA Toolkit)
```
---
### Sequenziale
```bash
gcc -o align align.c
```
