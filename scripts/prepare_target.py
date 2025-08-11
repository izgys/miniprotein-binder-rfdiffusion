#!/usr/bin/env python3
import os
import pathlib
import requests
from Bio.PDB.MMCIFParser import MMCIFParser
from Bio.PDB.PDBIO import PDBIO, Select
from Bio.PDB.Polypeptide import PPBuilder, is_aa

PDB_ID = "6M0J"   # SARS-CoV-2 spike RBD
CHAIN_ID = "E"    # Target chain
OUT_DIR = pathlib.Path("data/target")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def download_cif(pdb_id: str, out_path: pathlib.Path):
    """Download the mmCIF file from RCSB."""
    url = f"https://files.rcsb.org/download/{pdb_id}.cif"
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    out_path.write_bytes(r.content)
    return out_path

class ChainSelect(Select):
    """Select only the desired chain."""
    def __init__(self, chain_id):
        self.chain_id = chain_id
    def accept_chain(self, chain):
        return chain.id == self.chain_id

def chain_sequence(structure, chain_id):
    """Extract amino acid sequence from a chain."""
    for model in structure:
        chain = model[chain_id]
        ppb = PPBuilder()
        seq = ""
        for pp in ppb.build_peptides(chain):
            seq += str(pp.get_sequence())
        return seq
    return ""

def main():
    cif_path = OUT_DIR / f"{PDB_ID}.cif"
    if not cif_path.exists():
        print(f"Downloading {PDB_ID}.cif …")
        download_cif(PDB_ID, cif_path)
    else:
        print(f"{cif_path} already exists.")

    parser = MMCIFParser(QUIET=True)
    structure = parser.get_structure(PDB_ID, str(cif_path))

    # Save chain-only PDB
    io_pdb = PDBIO()
    io_pdb.set_structure(structure)
    out_chain_pdb = OUT_DIR / f"{PDB_ID}_chain{CHAIN_ID}.pdb"
    io_pdb.save(str(out_chain_pdb), ChainSelect(CHAIN_ID))
    print(f"Wrote {out_chain_pdb}")

    # Save FASTA
    seq = chain_sequence(structure, CHAIN_ID)
    fasta_path = OUT_DIR / f"{PDB_ID}_chain{CHAIN_ID}.fasta"
    with open(fasta_path, "w") as fh:
        fh.write(f">{PDB_ID}_{CHAIN_ID}\n{seq}\n")
    print(f"Wrote {fasta_path} (length {len(seq)})")

if __name__ == "__main__":
    main()
