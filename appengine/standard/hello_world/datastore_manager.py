from google.cloud import datastore

# The kind for the new entity
kind = 'Task'
# The name/ID for the new entity
name = 'sampletask1'
# The Cloud Datastore key for the new entity
task_key = datastore_client.key(kind, name)

# Prepares the new entity
task = datastore.Entity(key=task_key)
task['description'] = 'Buy milk'

# Saves the entity
datastore_client.put(task)

print('Saved {}: {}'.format(task.key.name, task['description']))

class DatastoreManager(object):
	def __init__(self, id):
		self._client = datastore.Client()
		self._id = id
	
	def has_id(self):
		return False
