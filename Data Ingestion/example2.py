from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

import uuid
import datetime

class ExampleModel(Model):
    example_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    example_type = columns.Integer(index=True)
    created_at = columns.DateTime()
    description = columns.Text(required=False)

connection.setup(['127.0.0.1'], "nbatests")
sync_table(ExampleModel)
em1 = ExampleModel.create(example_type=0, description="example1", created_at=datetime.datetime.now())
em2 = ExampleModel.create(example_type=1, description="example2", created_at=datetime.datetime.now())
print(ExampleModel.objects.count())