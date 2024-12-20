from mpi4py import MPI
import os

def host_program():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()  
    size = comm.Get_size()  

    if rank == 0:  
        filename = 'file.txt'
        if os.path.exists(filename):  
            print(f"Host: Preparing to send file {filename} to clients.")

            
            with open(filename, 'rb') as file:
                file_data = file.read()
            
            chunk_size = len(file_data) // (size - 1)  
            for i in range(1, size): 
                start = (i - 1) * chunk_size
                end = start + chunk_size if i != size - 1 else len(file_data)
                comm.send(file_data[start:end], dest=i, tag=0)  
                print(f"Host: Sent chunk {i} to client {i}.")
        else:
            print("Error")
    else:
        
        data = comm.recv(source=0, tag=0)  
        with open(f'client_{rank}_output.txt', 'wb') as output_file:
            output_file.write(data) 
        print("Received and saved file successfully")

if __name__ == '__main__':
    host_program()
