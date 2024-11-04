FROM continuumio/miniconda3
LABEL maintainer="emil"


ENV PYTHONBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=geodjango_tutorial.settings

RUN mkdir -p /app
WORKDIR /app

COPY ENV.yml .

# Add the conda-forge channel -> fix for whitenoise missing
RUN conda config --add channels conda-forge
RUN conda env create -f ENV.yml


RUN echo "conda activate awm-env" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]
# RUN command should use the new environment
SHELL ["conda", "run", "-n", "awm-env", "/bin/bash", "-c"]



# Copy everything in your Django project to the image.

COPY . /app
ENV PYTHONPATH="/app"

# The code to run when container is started:
COPY manage.py .

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "awm-env"]


# EXPOSE the port that container will operate on 
EXPOSE 8001

# SHELL [ "python", "manage.py", "createsuperuser" ]
# Finally, start the server
CMD ["conda", "run", "--no-capture-output", "-n", "awm-env", "python", "manage.py", "runserver", "0.0.0.0:8001"]
