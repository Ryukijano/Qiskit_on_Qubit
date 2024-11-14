import cudaq
from typing import List

#cudaq.set_target('qpp-cpu')
cudaq.set_target('nvidia')  # GPU backend which enables scaling to large problem sizes
qubit_count = 5  # Set to around 30 qubits if you have GPU access

secret_string = [1, 1, 0, 1,
                 0]  # Change the secret string to whatever you prefer

assert qubit_count == len(secret_string)

@cudaq.kernel
def oracle(register: cudaq.qview, auxiliary_qubit: cudaq.qubit,
           secret_string: List[int]):

    for index, bit in enumerate(secret_string):
        if bit == 1:
            x.ctrl(register[index], auxiliary_qubit)
            
@cudaq.kernel
def bernstein_vazirani(secret_string: List[int]):

    qubits = cudaq.qvector(len(secret_string))  # register of size n
    auxiliary_qubit = cudaq.qubit()  # auxiliary qubit

    # Prepare the auxillary qubit.
    x(auxiliary_qubit)
    h(auxiliary_qubit)

    # Place the rest of the register in a superposition state.
    h(qubits)

    # Query the oracle.
    oracle(qubits, auxiliary_qubit, secret_string)

    # Apply another set of Hadamards to the register.
    h(qubits)

    mz(qubits)  # measures only the main register


print(cudaq.draw(bernstein_vazirani, secret_string))
result = cudaq.sample(bernstein_vazirani, secret_string)

print(f"secret bitstring = {secret_string}")
print(f"measured state = {result.most_probable()}")
print(
    f"Were we successful? {''.join([str(i) for i in secret_string]) == result.most_probable()}"
)

print(cudaq.__version__)