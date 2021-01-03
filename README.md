## Roadmap Builder

A side-project for composing learning roadmaps using _Django Treebeard_ plugin and _d3.js_ library.
The idea was to enhance my learning process by composing roadmaps, which visualize a structure of what I need to learn to acquire a skill. 


### Usage

Run from the app directory
```python
pip install -r requirements.txt

python manage.py runserver 0.0.0.0:8000 --settings=roadmap_builder.settings
```

or run in the docker container
```
docker-compose -f docker-compose.yml up -d --build --force-recreate roadmap-builder-app
```

Go to localhost:8000/admin