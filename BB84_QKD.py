

!pip install cirq --quiet
import cirq

from random import choices

# set up dictionaries for encoding bits and gates

encode_gates = {0: cirq.I, 1: cirq.X}
basis_gates = {'Z': cirq.I, 'X': cirq.H}

num_bits = 100
qubits = cirq.NamedQubit.range(num_bits, prefix = 'q')

# Step #1 Alice creates her key randomly chosen as 1 or 0
alice_key = choices([0, 1], k = num_bits)

print('Alice\'s initial key: ', alice_key)

# Step #2 Alice creates a list of gates randomly chosen as Z or X
alice_bases = choices(['Z', 'X'], k = num_bits)

print('\nAlice\'s randomly chosen bases: ', alice_bases)

# Step #3 Alice encodes her qubits and appends corresponding gates.

alice_circuit = cirq.Circuit()

for bit in range(num_bits): # creates bit variable to represent current index

  encode_value = alice_key[bit] # finds next item in alice's random key list (0 or 1), assigns to "encode_value" variable
  # encode_value now = 0 or 1
  encode_gate = encode_gates[encode_value] # finds corresponding gate in encode_gates dictionary (0 = cirq.I, 1 = cirq.X), assigns to encode_gate
  # encode_gate value now = cirq.I or cirq.X
  
  basis_value = alice_bases[bit] # finds next item on alice's random basis list (Z or X), assigns to variable "basis_value"
  # basis_value now Z or X
  basis_gate = basis_gates[basis_value] # finds corresponding basis gates (Z = cirq.I, X = cirq.H), assigns to 'basis_gate'
  # basis_gate now cirq.I or cirq.H  

  qubit = qubits[bit] # finds next qubit name from list and assigns it to "qubit" variable
  # qubit now = 'q0' or 'q1' or 'q2' or ...
  alice_circuit.append(encode_gate(qubit)) # appends currently assigned encoding gate to current qubit
  alice_circuit.append(basis_gate(qubit)) # appends currently assigned basis gate to current qubit and adds qubit to circuit.

print('\nAlice\'s Phase 1 circuit:\n', alice_circuit)

# Step #4: Alice sends qubits to Bob


# Step #5 Bob randomly creates basis states, then appends with predetermined gates.

bob_bases = choices(['Z', 'X'], k = num_bits) # bob creates random base list
print('Bob\'s randomly chosen bases: ', bob_bases)

bob_circuit = cirq.Circuit()

for bit in range(num_bits):

  basis_value = bob_bases[bit] # finds next basis value from bob's random list, assigns to 'basis_value'.
  basis_gate = basis_gates[basis_value] # finds corresponding basis gates (Z = cirq.I, X = cirq.H), assigns to 'basis_gate'
  # basis_gate now cirq.I or cirq.H 

  qubit = qubits[bit] # finds next qubit from list ('q0', 'q1', ...)
  bob_circuit.append(basis_gate(qubit)) # adds qubit to circuit with current basis gate appended.


# Step #6  Bob measures qubits to create key.

bob_circuit.append(cirq.measure(qubits, key = 'bob key'))

print('\nBob\'s Phase 2 circuit:\n', bob_circuit)


# Step #7 Bob creates a BB84 circuit combining Alice and Bob's circuits, then measures, generating key

bb84_circuit = alice_circuit + bob_circuit

sim = cirq.Simulator()
results = sim.run(bb84_circuit)
bob_key = results.measurements['bob key'][0] # Should be more than first bit. Examine this line, why are they creating a combined circuit with all bits instead of just first few? When exactly do they share info about basis states to compare?

print('\nBob\'s initial key: ', bob_key)

# Step #8 Alice and Bob compare basis states and keep matches only, creating final individual keys from matches.

# creates 2 empty lists for final keys
final_alice_key = []
final_bob_key = []

for bit in range(num_bits):

  if alice_bases[bit] == bob_bases[bit]: # checks their random basis choices against each other.
    final_alice_key.append(alice_key[bit]) # appends bit where basis states matched Bob's
    final_bob_key.append(bob_key[bit]) # appends bit where basis matched Alice's.

print('\nAlice\'s key: ', final_alice_key)
print('Bob\'s key: ', final_bob_key)


# Step #9 Alice and Bob compare keys, l

if final_alice_key[0] == final_bob_key[0]: # if their first bits match, they keep the rest, assuming no evesdropper.
  final_alice_key = final_alice_key[1:]
  final_bob_key = final_bob_key[1:]
# Step #9 should probably be altered to check more than just the first bit for a match. The more bits they check,
# .. the less chance that the evesdropper got lucky and guessed the first bits correctly. (confirm this inference with teacher)

  print('\n\nWe can use our keys!')
  print('Alice Key: ', final_alice_key)
  print('Bob Key: ', final_bob_key)

else:
  print('\n\nEve was listening, we need to use a different channel!')
