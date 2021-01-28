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
# So we need to create new columns with $\Delta log(D_p)$, $\Delta S$ and $\Delta V$
# x axis can be done by specifying log scale on the plotting function

# %%
# create the columns
in_data["Delta log Dp"] = np.log10(in_data["max size (um)"]) - np.log10(
    in_data["min size (um)"]
)
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
# N plot for Q1
fig1, ax = plt.subplots()
ax.bar(
    in_data["min size (um)"],
    in_data["Number of Particles in int"] / in_data["Delta log Dp"],
    align="edge",
    width=in_data["max size (um)"] - in_data["min size (um)"],
    edgecolor="black",
)
ax.set_title("Number Distribution with Particle Diameter")
ax.set_ylabel("$\Delta N / \Delta log(D_p)$")
ax.set_xlabel("$D_p (\mu m)$")
ax.set_xscale("log")
ax.set_xticks([1e-1, 1e0, 1e1])

# %%
# SA plot for Q3
fig2, ax = plt.subplots()
ax.bar(
    in_data["min size (um)"],
    in_data["Delta S"] / in_data["Delta log Dp"],
    color="orange",
    alpha=0.7,
    align="edge",
    width=in_data["max size (um)"] - in_data["min size (um)"],
    edgecolor="black",
)
ax.set_title("Surface Area Distribution with Particle Diameter")
ax.set_ylabel("$\Delta S / \Delta log(D_p)$")
ax.set_xlabel("$D_p (\mu m)$")
ax.set_xscale("log")
ax.set_xticks([1e-1, 1e0, 1e1])

# %%
# V plot for Q3
fig3, ax = plt.subplots()
ax.bar(
    in_data["min size (um)"],
    in_data["Delta V"] / in_data["Delta log Dp"],
    color="green",
    alpha=0.7,
    align="edge",
    width=in_data["max size (um)"] - in_data["min size (um)"],
    edgecolor="black"
)
ax.set_title("Volume Distribution with Particle Diameter")
ax.set_ylabel("$\Delta V / \Delta log(D_p)$")
ax.set_xlabel("$D_p (\mu m)$")
ax.set_xscale("log")
ax.set_xticks([1e-1, 1e0, 1e1])

# %%
