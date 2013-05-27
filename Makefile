PROJECT_NAME=photoplanet
PYTHONPATH=$(CURDIR):$(CURDIR)/$(PROJECT_NAME)

MANAGE= PYTHONPATH=$(PYTHONPATH) python $(PROJECT_NAME)/manage.py

runserver:
	$(MANAGE) runserver --settings=photoplanet.settings.local

shell:
	$(MANAGE) shell --settings=photoplanet.settings.local

syncdb:
	$(MANAGE) syncdb --settings=photoplanet.settings.local

migrate:
	$(MANAGE) migrate feedback --settings=photoplanet.settings.local
	$(MANAGE) migrate photoplanet --settings=photoplanet.settings.local
