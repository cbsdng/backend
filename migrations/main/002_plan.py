import peewee as pw

SQL = pw.SQL


def migrate(migrator, database, fake=False, **kwargs):
    """Write your migrations here."""
    @migrator.create_model
    class Plan(pw.Model):
        id = pw.AutoField()
        name = pw.TextField()
        memory = pw.IntegerField()

        class Meta:
            table_name = "plan"


def rollback(migrator, database, fake=False, **kwargs):
    """Write your rollback migrations here."""
    migrator.remove_model('plan')
    migrator.remove_model('basemodel')
