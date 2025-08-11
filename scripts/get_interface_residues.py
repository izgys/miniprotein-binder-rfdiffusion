#!/usr/bin/env python3
import pathlib, json
from Bio.PDB import MMCIFParser, NeighborSearch, Selection, is_aa

PDB_ID = "6M0J"
TARGET_CHAIN = "E"  # RBD
CUTOFF = 8.0        # Å; common interface cutoff (6–10 Å)

in_cif = pathlib.Path("data/target") / f"{PDB_ID}.cif"
out_json = pathlib.Path("data/target") / f"{PDB_ID}_chain{TARGET_CHAIN}_interface_residues.json"
out_txt  = pathlib.Path("data/target") / f"{PDB_ID}_chain{TARGET_CHAIN}_interface_residues.txt"

parser = MMCIFParser(QUIET=True)
structure = parser.get_structure(PDB_ID, str(in_cif))
model = structure[0]
target = model[TARGET_CHAIN]

# Partner chains = all protein chains except TARGET_CHAIN
partners = [ch for ch in model if ch.id != TARGET_CHAIN]

# Build a NeighborSearch over all atoms from partner chains
partner_atoms = []
for ch in partners:
    for res in ch:
        if is_aa(res, standard=True):
            for atom in res:
                if atom.element != 'H':
                    partner_atoms.append(atom)
ns = NeighborSearch(partner_atoms)

# Identify target residues that have any atom within CUTOFF to any partner atom
interface_positions = set()
for res in target:
    if not is_aa(res, standard=True):
        continue
    for atom in res:
        if atom.element == 'H':
            continue
        if ns.search(atom.coord, CUTOFF):
            interface_positions.add(res.id[1])
            break

interface_list = sorted(interface_positions)
print(f"Found {len(interface_list)} interface residues on chain {TARGET_CHAIN} within {CUTOFF} Å.")
print(interface_list)

# Save
out_json.write_text(json.dumps({
    "pdb_id": PDB_ID,
    "chain": TARGET_CHAIN,
    "cutoff_A": CUTOFF,
    "residue_indices": interface_list
}, indent=2))
out_txt.write_text(" ".join(map(str, interface_list)))

print(f"Wrote {out_json}")
print(f"Wrote {out_txt}")
