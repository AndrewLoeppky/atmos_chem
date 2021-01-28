# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
# import the data
in_data = pd.read_csv("C:/Users/Owner/UBC_S2021/atmos_chem/problemset2.csv")

# %% [markdown]
# We want to plot
#
# a) $\Delta N / \Delta log(D_p)$ versus $log(D_p)$
#
# b) $\Delta S / \Delta log(D_p)$ versus $log(D_p)$
#
# c) $\Delta V / \Delta log(D_p)$ versus $log(D_p)$
#
# So we need to create new columns with $\Delta log(D_p)$, $log(D_p)$, $\Delta S$ and $\Delta V$

# %%
# create the columns
in_data["Delta log Dp"] = np.log10(in_data["max size (um)"]) - np.log10(
    in_data["min size (um)"]
)
in_data["log Dp"] = np.log10(in_data["Mean of Size int (um)"])
in_data["Delta S"] = (
    4
    * np.pi
    * (in_data["Mean of Size int (um)"] / 2) ** 2
    * in_data["Number of Particles in int"]
)
in_data["Delta V"] = (
    4
    / 3
    * np.pi
    * (in_data["Mean of Size int (um)"] / 2) ** 3
    * in_data["Number of Particles in int"]
)

in_data
# %%
# plot for Q1
fig1, ax = plt.subplots()
ax.plot(
    in_data["Mean of Size int (um)"],
    in_data["Number of Particles in int"] / in_data["Delta log Dp"],
)
ax.set_title("Number Distribution with Particle Diameter")
ax.set_ylabel("$\Delta N / \Delta log(D_p)$")
ax.set_xlabel("$D_p (\mu m)$")
ax.set_xscale("log")

# %%
# SA plot for Q3
fig2, ax = plt.subplots()
ax.plot(
    in_data["Mean of Size int (um)"],
    in_data["Delta S"] / in_data["Delta log Dp"],
)
ax.set_title("Surface Area Distribution with Particle Diameter")
ax.set_ylabel("$\Delta S / \Delta log(D_p)$")
ax.set_xlabel("$D_p (\mu m)$")
ax.set_xscale("log")

# %%
# V plot for Q3
fig3, ax = plt.subplots()
ax.plot(
    in_data["Mean of Size int (um)"],
    in_data["Delta V"] / in_data["Delta log Dp"],
)
ax.set_title("Volume Distribution with Particle Diameter")
ax.set_ylabel("$\Delta V / \Delta log(D_p)$")
ax.set_xlabel("$D_p (\mu m)$")
ax.set_xscale("log")

# %%
