# This container will contain the neural network itself with its consumer and responder module (one direct message to
# received chat ID
FROM continuumio/miniconda3

# Setting working directory
WORKDIR /usr/src/app

# Copying packages list
COPY environment.yml /usr/src/app

# Creating new conda environment
RUN conda env create -f environment.yml

# RUN commands now will use this environment
SHELL ["conda", "run", "-n", "neural-network-env", "/bin/bash", "-c"]

# Copying another packages list (for pika and aiogram)
COPY requirements.txt /usr/src/app

# Installing pika and aiogram
RUN pip install -r requirements.txt

# Copying the rest of directory
COPY . /usr/src/app

# Starting command inside new environment via conda run
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "neural-network-env", "python", "consumer.py"]
