# Qiskit_on_Qubit
![QiskitLogo](https://user-images.githubusercontent.com/80598737/135030625-6384639a-5b11-4322-878f-5d6cb5dd44d9.png)
Quantum computing brings together ideas from classical information theory, computer science, and quantum physics. This review aims to summarize not just quantum computing, but the whole subject of quantum information theory. Information can be identified as the most general thing which must propagate from a cause to an effect. It therefore has a fundamentally important role in the science of physics.

## What is quantum?
The quantum in "quantum computing" refers to the quantum mechanics that the system uses to calculate outputs. In physics, a quantum is the smallest possible discrete unit of any physical property. It usually refers to properties of atomic or subatomic particles, such as electrons, neutrinos and photons.

## What is a qubit?
A qubit is the basic unit of information in quantum computing. Qubits play a similar role in quantum computing as bits play in classical computing, but they behave very differently. Classical bits are binary and can hold only a position of 0 or 1, but qubits can hold a superposition of all possible states.

## What is quantum computing?
Quantum computers harness the unique behaviour of quantum physics: such as superposition, entanglement and quantum interference and apply it to computing. This introduces new concepts to traditional programming methods.

## What does this repository contain?
Fundamentals of Quantum Algorithms implemented using Qiskit at [IBM Quantum Experience](https://quantum-computing.ibm.com/). In this repository I will be sharing my experiences, daily learnings and accomplishments with regard to this booming technology.

## Quantum Variational Autoencoder (QVAE)
This repository includes an implementation of a Quantum Variational Autoencoder (QVAE) using Qiskit. The QVAE is trained on the MNIST dataset for encoding and decoding images. The implementation can be found in the `Quantum_VAE.ipynb` notebook.

### Usage Instructions
1. Load and preprocess the MNIST dataset.
2. Define the QVAE model with parameterized quantum circuits as the encoder and decoder.
3. Train the QVAE model on the MNIST dataset.
4. Visualize the reconstructed and generated data.

## Raytracing with QVAE
This repository also includes an implementation of a raytracing algorithm integrated with the QVAE. The QVAE is used to encode data into a lower-dimensional latent space, which is then used as input to the raytracing algorithm. The implementation can be found in the `Raytracing.ipynb` notebook.

### Usage Instructions
1. Load the trained QVAE parameters.
2. Define the QVAE encoder and decoder functions.
3. Define a function to generate a scene based on QVAE encoded data.
4. Generate and visualize the raytraced image using the QVAE encoded data.

## GitHub Pages
This repository has a GitHub Pages site that provides detailed explanations about the repository and includes a code space. You can visit the site [here](https://ryukijano.github.io/Qiskit_on_Qubit/).
