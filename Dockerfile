FROM continuumio/miniconda3:25.3.1-1

# Create and cd into workspace inside image
WORKDIR /workspace

# Copy the repo into the image
COPY . .

# Set up conda environment
RUN conda update conda -y
RUN conda config --add channels conda-forge

# Customize environment name from cli
ARG CONDA_ENV_NAME=xaqlab
ENV CONDA_ENV_NAME=$CONDA_ENV_NAME

# Create conda environment
RUN conda env create -n $CONDA_ENV_NAME -y --file environment.yml

# Install package in development mode within conda environment
RUN conda run -n $CONDA_ENV_NAME pip install -e .[dev]

# Launch Jupyter Lab when container starts
CMD ["bash", "-c", "source activate $CONDA_ENV_NAME && python -m ipykernel install --user --name $CONDA_ENV_NAME --display-name \"$CONDA_ENV_NAME\" && jupyter lab --ip=0.0.0.0 --no-browser --allow-root"]
EXPOSE 8888
