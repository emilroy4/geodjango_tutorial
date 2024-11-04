FROM continuumio/miniconda3
LABEL maintainer="emil"

ENV PYTHONBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=geodjango_tutorial.settings

# Set up the work directory
RUN mkdir -p /app
WORKDIR /app

# Copy environment file and create environment
COPY ENV.yml .
RUN conda config --add channels conda-forge && conda env create -f ENV.yml

# Install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client

# Activate environment and set as default shell
RUN echo "conda activate awm-env" >> ~/.bashrc
ENV PATH /opt/conda/envs/awm-env/bin:$PATH

# Copy application files
COPY . /app
ENV PYTHONPATH="/app"

# Ensure the entrypoint script is executable
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

# Use the entrypoint to activate the environment
ENTRYPOINT ["/app/docker-entrypoint.sh"]

# Expose port for the Django app
EXPOSE 8001

# Start Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
