import numpy as np
import pandas as pd
pd.set_option('precision', 4)

data = pd.read_csv("sampleFile.txt", sep="\t")

data["RAFs"] = data["ReferenceAlleleCount"] / (data["ReferenceAlleleCount"] + data["AlternateAlleleCount"])
data["AAFs"] = data["AlternateAlleleCount"] / (data["ReferenceAlleleCount"] + data["AlternateAlleleCount"])

data["MAFs"] = np.where(data["RAFs"] < data["AAFs"], data["RAFs"], data["AAFs"])

print('\n')
print(data[["SNPname", "MAFs"]])

data["matches"] = data["MAFs"].between(0.0200, 0.3000, inclusive='both')
data["matches"] = np.where(data["matches"] == True, 1, 0)

print('\n' + "In the file, sampleFile.txt, there are " + str(sum(data["matches"])) + " MAFs between 0.02 and 0.30.")
