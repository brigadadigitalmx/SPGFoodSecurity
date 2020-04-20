FROM continuumio/miniconda
COPY environment.yml /app/environment.yml
RUN conda env update -f /app/environment.yml
COPY . /app
RUN conda activate SPGFoodSecurity
CMD python /app/main.py
