#Imports
import numpy as np
import pandas as pd

#Setting float decimal precision to 4
pd.set_option('precision', 4)

#Reading in file
data = pd.read_csv("sampleFile.txt", sep="\t")

#Calculating allele frequencies and adding them as new Series to the pandas dataset (data)
data["RAFs"] = data["ReferenceAlleleCount"] / (data["ReferenceAlleleCount"] + data["AlternateAlleleCount"])
data["AAFs"] = data["AlternateAlleleCount"] / (data["ReferenceAlleleCount"] + data["AlternateAlleleCount"])

#Calculating MAF by using numpy "where" function (giving a conditional and the possible executions)
data["MAFs"] = np.where(data["RAFs"] < data["AAFs"], data["RAFs"], data["AAFs"])

#Printing two Series as a dataset (names + MAFs)
print('\n')
print(data[["SNPname", "MAFs"]])

#Creating a new Series with the between function (True if numbers are within the range, False if they are not)
data["matches"] = data["MAFs"].between(0.0200, 0.3000, inclusive='both')
#Converting Series "matches" to numbers (1 for True, 0 for False)
data["matches"] = np.where(data["matches"] == True, 1, 0)

#Sum of Series gives # of values within range, since only matches are given quantity (1)
AllelesWithinRange = sum(data["matches"])

#Printing # of matches
print('\n' + "In the file, sampleFile.txt, there are " + str(AllelesWithinRange) + " MAFs between 0.02 and 0.30.")
