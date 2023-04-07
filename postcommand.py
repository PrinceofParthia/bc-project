# Imports the libaries needed: re and itertools to parse the mystery file and percent identity matrix, Phylo and Tree to construct proper phylogeny trees.
import re
from Bio import Phylo
from ete3 import Tree
from itertools import chain

# Two regex functions, findall for the pim file.
def regex_findall(input_text):
    pattern = re.findall(r"[A-Za-z0-9]+\|[A-Za-z0-9]+\.\d\|", input_text)
    return pattern

# and search for the mystery file.
def regex_search(input_text):
    pattern = re.search(r"[A-Za-z0-9]+\|[A-Za-z0-9]+\.\d\|", input_text)
    return pattern.group()

# Asks for a job id via user-input, then creates a newick file from the dendrogram file produced by Clustal-Omega. Also returns the job id inputted so that the rest of the functions can be pipelined.
def convertfiletonhformat():
    jobid = input("Enter your job id: ")
    phyfile = str(jobid) + ".tree.dnd"
    tree = Phylo.read(phyfile, "newick")
    Phylo.write(tree, str(jobid +".tree.nh"), "newick")
    return jobid

# Imports the newick file created to construct the visual representation of the phylogenic tree.
def importfile(jobid):
    phyfile = str(jobid) + ".tree.dnd"
    tree = Phylo.read(phyfile, "newick")
    return tree

# Returns the name of the sequence in the mystery file, allowing this sequence to be the target sequence in the similarity testing functions.
def mysterysequencename(mysteryfile = "mystery.fasta"):
    file = open(mysteryfile, "r")
    for line in file:
        mysteryname = regex_search(line)
        if mysteryname != None:
            name = mysteryname
            break
    return name

# Stores the jobid, to use when importing the associated files. This means that multiple requests can be stored in the same directory, but as long as the correct jobid is used, only the files associated with the job are used as analysis.
jobid = convertfiletonhformat()
# Imports a phylogeny tree as part of the Phylo submodule.
phylotree = importfile(jobid)
# Makes a tree out of the tree file created in the function convertfiletonhformat() as part of the Tree submodule.
treefile = str(jobid + ".tree.nh")
nhtree = Tree(treefile)
# Makes sure the correct PIM file is selected and that the right sequence identifier is used during the comparison functions below.
pimfile = str(jobid + ".pim.pim")
mysteryname = mysterysequencename()

# Finds the most similar sequence to the target sequence in terms of percent identity, as calculated by the MSA performed by the EBI Web Service. Returns a string with the results
# embedded. This returns a different result to the below function, and both fit the description of the output outlined in the coursework details, so two functions provide two different measures of "difference". This will only return one result: there may be multiple sequences equally similar with the target sequence.
def mostclosepim(mysteryname = mysteryname, pimfile = pimfile):
    value = 0
    alist = []
    namelist = []
    dictionary = {}
    file = open(pimfile, "r")
    for line in file:
        name = regex_findall(line)
        if name != []:
            namelist.append(name)
        if mysteryname in line:
            splitline = line.split()
            length = len(splitline)
            alist.append(splitline[2:(length-1)])
            blist = list(map(float, chain.from_iterable(alist)))
            for i in blist:
                if i != 100.00:
                    if i > value:
                        value = i
    namelist = list(map(str, chain.from_iterable(namelist)))
    dictionary = dict(zip(namelist, blist))
    for key in dictionary:
        if dictionary[key] == value:
            nearestname = key
    return "By percentage identity, the most similar sequence to " + mysteryname + " is " + nearestname + " with " + str(value) + "% identity."
    
# Finds the most similar sequence to the target sequence in terms of phylogenic distance, as calculated by the MSA performed by the EBI Web Service (using the file with the suffix tree.dnd). Returns a string with the results embedded. This returns a different result to the above function, and both fit the description of the output outlined in the coursework details, so two functions provide two different measures of "difference". This will only return one result: there may be multiple sequences equally similar with the target sequence.
def mostclosephylo(mysteryname = mysteryname, phylotree = phylotree):
    terminallist = []
    namelist = []
    smallestdist = 1
    for terminal in phylotree.get_terminals():
        terminallist.append(terminal)
    for terminal in terminallist:
        string_y = str(terminal)
        splitname = string_y.split("name=")
        namelist.append(splitname[0])
    for name in namelist:
        dist = phylotree.distance(mysteryname, name)
        if dist != 0:
            if dist < smallestdist:
                smallestdist = dist
                smallestname = name
    return "Phylogenically, the most similar sequence to " + mysteryname + " is " + smallestname + ", with a distance of " + str(smallestdist) + ", where 1 is no relation."

# Stored example jobid, so that the command line step need not be performed.
#jobid = "clustalo-R20230405-221208-0798-28169415-p1m"
# Prints the most similar sequence by percentage identity (embedded in string).
print(mostclosepim())
# Prints the most similar sequence by phylogenic distance (embedded in string).
print(mostclosephylo())
# Using the standard print function of the Phylo submodule on a tree that has one hundred terminal nodes produces an unreadable mess and takes a substantial amount of time. Instead, the Tree submodule is used, as this gives a much more readable tree. However, as this tree puts the mystery sequence in its own clade, it is unhelpful in resolving the conflict between the two methods above as to what is the closest sequence. (It looks good and is a stretch goal, however, so I kept it in.) 
#print(phylotree)
print(nhtree)