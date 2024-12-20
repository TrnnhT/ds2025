from mpi4py import MPI

def client_program():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()  
    if rank != 0:  

        data = comm.recv(source=0, tag=0)  
        with open(f'client_{rank}_received.txt', 'wb') as file:
            file.write(data)
        print("File saved sucessfully")

if __name__ == '__main__':
    client_program()
