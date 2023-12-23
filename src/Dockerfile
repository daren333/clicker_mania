#FROM python:3
#
#WORKDIR /app
#
## Install base utilities
#RUN apt-get update \
#    && apt-get install -y build-essential \
#    && apt-get install -y wget \
#    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/*
#
## Install miniconda
#ENV CONDA_DIR /opt/conda
#RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
#    /bin/bash ~/miniconda.sh -b -p /opt/conda
## Put conda in path so we can use conda activate
#ENV PATH=$CONDA_DIR/bin:$PATH
#
#COPY environment.yml /app/
#COPY src /app/src/
#
#RUN conda env create -f environment.yml
#RUN conda init && conda activate clicker_mania
#
#CMD ["python", "/app/src/app.py"]

FROM python:3

# Create a non-root user
RUN useradd -m -s /bin/bash appuser

# Set the working directory and assign ownership to the new user
WORKDIR /home/appuser
RUN chown -R appuser:appuser /home/appuser

# Install base utilities
RUN apt-get update \
    && apt-get install -y build-essential wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install miniconda
ENV CONDA_DIR /home/appuser/miniconda
ENV PYTHONUNBUFFERED 1
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /home/appuser/miniconda.sh && \
    /bin/bash /home/appuser/miniconda.sh -b -p $CONDA_DIR \

# Switch to the non-root user
USER appuser

# Update python paths
ENV PATH=$CONDA_DIR/bin:$PATH
#ENV PATH=$PATH:/home/appuser

# Copy environment.yml and create conda environment without activating it
COPY environment.yml /home/appuser
COPY src /home/appuser/src/

RUN conda env create -f /home/appuser/environment.yml

ENV FLASK_APP=src.app
ENV FLASK_CONFIG=development

# Set the command to run your application
CMD ["conda", "run", "-n", "clicker_mania", "flask", "run", "--host", "0.0.0.0"]