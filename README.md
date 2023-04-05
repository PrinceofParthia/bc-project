# bc-project
Biocomputing Project

A Biocomputing project investigaing a DNA sequence from an unknown dog type, and constructing a phylogeny tree comparing this sequence with a predefined database of related sequences. This project uses EBI's clustal-omega Web Services to create a multiple-sequence alignment for this database (including the mystery sequence), and then uses the output of this request to assess the closest relative within the database and construct a simple phylogenetic tree, showing the relation of the mystery sequence to all others within the database.

At present, this project is not pipelined: I could not figure out how to do the command-line step from within the python file, or even if this is possible. As such, there is a command-line step that requires manual input by the user. More information about this is described by the first python file, named "precommand". After this request is returned, the python file named "postcommand" should be able to take the correct file(s) from the output provided by the EBI service and construct a functional phylogenetic tree, as well as various metrics associated with the multiple sequence alignment.

The following files should be present in the project folder:
  - mystery.fasta
  - dog_breeds.fasta
  - clustalo.py
  - precommand.py
  - postcommand.py
  - clustalo-[jobtitle]
    - .tree.dnd
    - .pim.pim

At present, no tests are included. I will attempt to write them before Friday night.
