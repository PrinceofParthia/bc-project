# Already run, appends the mystery sequence to the database so that the entire database could be aligned. Run this only for the first time you use
# a new mystery file.

def addmysteryfile(mysteryfile = "mystery.fasta", database = "dog_breeds.fasta"):
    mystery = open(mysteryfile, "r")
    database = open(database, "a")
    database.write(mystery.read())
    database.close()
    mystery.close()
    return

#addmysteryfile()

# This function simply creates the command-line term to be used in the manual command-line step.

def commandlineterm(web_service = "python clustalo.py", database = "dog_breeds.fasta"):
    email = input("Enter email: ")
    search_term = "Your request term is: " + str(web_service) + " --asyncjob --email " + str(email) + " --stype dna --sequence " + str(database)
    return search_term

commandlineterm()

#### Test could be test for proper email format

# If successful, a jobid should be produced: example "clustalo-R20230405-221208-0798-28169415-p1m" 
# The mutliple-sequence-alignment will be performed by the EBI servers. Use the status request line generated by the command line to
# check on the progress of the multiple sequence alignment:
# example "python clustalo.py --status --jobid clustalo-R20230405-221208-0798-28169415-p1m"

# Once completed, the command line will download multiple files into the directory. Primarily, we are interested in the files ending
# tree.dnd: example "clustalo-R20230405-221208-0798-28169415-p1m.tree.dnd" and
# pim.pim: example "clustalo-R20230405-221208-0798-28169415-p1m.pim.pim"

# For convenience (the MSA will take multiple hours) I have provided those two files produced by this dataset.
# Keep a hold of the project ID, it will be useful if you run this multiple times!