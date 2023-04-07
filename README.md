# bc-project
Biocomputing Project

A Biocomputing project investigaing a DNA sequence from an unknown dog type, and constructing a phylogeny tree comparing this sequence with a predefined database of related sequences. This project uses EBI's clustal-omega Web Services to create a multiple-sequence alignment for this database (including the mystery sequence), and then uses the output of this request to assess the closest relative within the database and construct a simple phylogenetic tree, showing the relation of the mystery sequence to all others within the database.

At present, this project is not pipelined: I could not figure out how to do the command-line step from within the python file, or even if this is possible. As such, there is a command-line step that requires manual input by the user. More information about this is described by the first python file, named "precommand". After this request is returned, the python file named "postcommand" should be able to take the correct file(s) from the output provided by the EBI service and construct a functional phylogenetic tree, as well as various metrics assessing similarity to the target sequence.

The command-line will return other files in addition to the ones necessary for the postcommand.py, these can be discarded if desired. They can be useful for verifying the dataset that was used to generate the results and to visually inspect the MSA performed by the EBI Web Service however, so they will be returned alongside the relevant files.

The following files should be present in the project folder:
  - mystery.fasta
  - dog_breeds.fasta
  - clustalo.py
  - precommand.py
  - postcommand.py
  - clustalo-[jobtitle]
    - .tree.dnd
    - .pim.pim

Additional files that will result from running this project from start to finish:
  - clustalo-[jobtitle]
    - .tree.nh (own creation)
    - .submission.params
    - .sequence.txt
    - .phylotree.ph
    - .out.txt
    - .aln-clustal_num.clustal_num
 
Author's note:
At present, no tests are included. To be fair, I don't think you could really "screw up" the inputs in a way that would be meaningful to test, but if I find the time tomorrow morning I'll include a few tests. The two methods for finding potential "mostest closest" sequences return different answers. The "output" requirement of the coursework was vague enough that I felt discounting one of them was unfair, and also would not show the effort and hairpulling I went through when they did return different answers. Personally I would prefer the percentage identity matrix result, as that directly compares the sequences, whereas the phylogenic tree results may be affected by the clade distance being increased because of sequences that are "more similar" to the  
