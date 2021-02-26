

def getdamage():

    # read in DamageFunctionVariables.xlsx

    # BldgTypes = list of building types
    BldgTypes = ["C1HHC", "C1HMC", "C1HLC", "C1HPC",
                 "C1MHC", "C1MMC", "C1MLC", "C1MPC",
                 "C1LHC", "C1LMC", "C1LLC", "C1LPC",
                 "C2HHC", "C2HMC", "C2HLC", "C2HPC",
                 "C2MHC", "C2MMC", "C2MLC", "C2MPC",
                 "C2LHC", "C2LMC", "C2LLC", "C2LPC",
                 "C3HLC", "C3HPC",
                 "C3MLC", "C3MPC",
                 "C3LLC", "C3LPC",
                 "MHHC", "MHMC", "MHLC", "MHPC",
                 "PC1HC", "PC1MC", "PC1LC", "PC1PC",
                 "PC2HHC", "PC2HMC", "PC2HLC", "PC2HPC",
                 "PC2MHC", "PC2MMC", "PC2MLC", "PC2MPC",
                 "PC2LHC", "PC2LMC", "PC2LLC", "PC2LPC",
                 "RM1MHC", "RM1MMC", "RM1MLC", "RM1MPC",
                 "RM1LHC", "RM1LMC", "RM1LLC", "RM1LPC",
                 "RM2HHC", "RM2HMC", "RM2HLC", "RM2HPC",
                 "RM2MHC", "RM2MMC", "RM2MLC", "RM2MPC",
                 "RM2LHC", "RM2LMC", "RM2LLC", "RM2LPC",
                 "S1HHC", "S1HMC", "S1HLC", "S1HPC",
                 "S1MHC", "S1MMC", "S1MLC", "S1MPC",
                 "S1LHC", "S1LMC", "S1LLC", "S1LPC",
                 "S2HHC", "S2HMC", "S2HLC", "S2HPC",
                 "S2MHC", "S2MMC", "S2MLC", "S2MPC",
                 "S2LHC", "S2LMC", "S2LLC", "S2LPC",
                 "S3HC", "S3MC", "S3LC", "S3PC",
                 "S4HHC", "S4HMC", "S4HLC", "S4HPC",
                 "S4MHC", "S4MMC", "S4MLC", "S4MPC",
                 "S4LHC", "S4LMC", "S4LLC", "S4LPC",
                 "S5HLC", "S5HPC",
                 "S5MLC", "S5MPC",
                 "S5LLC", "S5LPC",
                 "URMMLC", "URMMPC",
                 "URMLLC", "URMLPC",
                 "W1HC", "W1MC", "W1LC", "W1PC",
                 "W2HC", "W2MC", "W2LC", "W2PC"]

    # get row number
    # rowNum = find(BldgTypes==bldgType);

    # run graph damage function
    # [Pslight,Pmoderate,Pextensive,Pcomplete] = graphDamFunct(bldgType, PGA, DFV, rowNum);

    return