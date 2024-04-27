### Capstone Project Title: *Repurposing of Approved Drugs for Alzheimer’s Disease*
### Created by **Devaraja Mudeppa**

**The folder contains the following data files** 
1. Data cleaning and Exploratory data analysis of downloaded approved and BACE1 inhibitor molecules from ChEMBL website(**BASE_inhibiors_EDA.ipynb**, and **approved_EDA.ipynb**)
2. Converting of molecules into fingerprints and testing with different models (**RFC_SVM_NN_baseallinhibitors.ipynb** and **KNN.ipynb** )
3. Ligand Based Virtual Screening(LBVS) of approved molecules(**LBVS.ipynb**)
4. Identification of hydrogen donors and acceptors, and hydrophobic pharamcofeatures for each ligand (**Lig_pharmacophore.ipynb**)
5. Retriving and aligning of inhibitor bound BASE1 structures (**PDB_BACE.ipynb**)
6. Docking of lingad to BASE1 structure (**docking_protein_ligand.ipynb**)
7. As docking of FDA drugs was not possible on jupyterlab, a semi_GUI based AutoDock Vina was used for docking of potential inhibitors of BASE1 isolated from approved drugs. The folders (**Autodock_BASE1_inhibitors** and **Autodock_approved_drugs**) are saved in data folder of this project.
8. Slide deck (**project_capstone.pdf**)


**The data subfolder has the downloaded molecule data .tsv files, filtered molecules of .csv files, .pdb and .pdbqt files**

## Executive Summary:
    Alzheimer’s disease (AD) is a brain disorder that gradually declines memory and cognitive abilities over time and primarily affects older individuals. AD is the leading cause of dementia in Western societies. It impacts more than seven million people in the United States and an estimated 55 million worldwide (1). Each year, approximately 10 million new cases are diagnosed. The global economic burden of the AD is about 1.3 trillion US dollars. The slow progressive loss of memory and cognitive impairments in AD are due to the accumulation of amyloid-beta (AB, B is a Greek letter beta) peptides deposition in the brain (2). Therapeutic interventions that reduce the accumulation of AB peptides in the brain are implied effective for the treatment of AD. Beta-secretase-1(BACE1), a protease, is one of the key enzymes responsible for generating AB peptides (2). Inhibition of BACE1 with small molecules has been proven to reduce the accumulation of AB peptides in the brain. 
    
    In this capstone project, I set an aim to find inhibitors against the BACE1 target from the list of approved drugs using data science tools. A complete list of approved drugs and known BACE1 inhibitors was retrieved separately from the chEMBL database, cleaned, retained the necessary features, and performed exploratory data analysis. The inhibitory activities of molecules measured as half-maximal inhibitory concentrations (IC50) values (nanomolar, nM) were converted into moles per liter values(pIC50) on a logarithmic scale. The SMILES (Simplified Molecular Input Line Entry Systems) string of each molecule to a fingerprint of binary digits. The molecular fingerprints of BACE1 inhibitors as feature (X-variable) and their activities(pIC50) as target (y-label) were fed to train and test the  convolutional Neural network (CNN). The CNN model gave the best MAE and MSE values of 0.71 and 0.86 respectively.  The trained and tested CNN model was deployed to predict the potency (pIC50 values) of approved drugs against the BACE1 target. Next, to know if BACE1 has multiple inhibitor binding sites, five 3D structures of inhibitor-bound BACE1 with high resolution (equal or less than 2 Angstrom) were retrieved from the RCSB PDB database, extracted ligands(inhibitors) from BACE1 and aligned to visualize the ligand binding site. All five inhibitors are bound on the same site on the BACE1 structures. Finally, ten predicted potential inhibitors were further confirmed by docking them to the BACE1 structures on AutoDock Vina. Of the ten picked predicted inhibitors, 9 of them bound to BACE1 with various affinities. The initial concept presented here for virtually screening approved drugs and inhibitors against BACE1 opens opportunities to enhance the model by applying rigorous filters and incorporating molecular graphs.

**References**
1.	https://www.who.int/news-room/fact-sheets/detail/dementia
2.	The β-secretase enzyme BACE1 as a therapeutic target for Alzheimer's disease | Alzheimer's Research & Therapy (springer.com)(https://link.springer.com/article/10.1186/alzrt82)


