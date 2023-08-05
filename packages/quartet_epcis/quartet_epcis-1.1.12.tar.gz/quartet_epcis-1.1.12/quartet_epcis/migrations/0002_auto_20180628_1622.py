# Generated by Django 2.0 on 2018-06-28 21:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import quartet_epcis.models.abstractmodels
import quartet_epcis.models.headers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quartet_epcis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biz_transaction', models.CharField(help_text='The business transaction.', max_length=200, verbose_name='Business Transaction')),
                ('type', models.CharField(help_text='The type of business transaction.', max_length=200, null=True, verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Business Transaction',
                'verbose_name_plural': 'Business Transactions',
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID', primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When this record was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='When this record was last modified.', verbose_name='Modified')),
                ('type', models.CharField(help_text='The source type.', max_length=150, verbose_name='Type')),
                ('destination', models.CharField(help_text='The Destination identifier.', max_length=150, verbose_name='Destination')),
            ],
            options={
                'verbose_name': 'Destination',
                'verbose_name_plural': 'Destinations',
            },
        ),
        migrations.CreateModel(
            name='DestinationEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.ForeignKey(help_text='A destination within the event.', on_delete=django.db.models.deletion.CASCADE, to='quartet_epcis.Destination', verbose_name='Destination')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentIdentification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(default='EPCglobal', help_text='The originator of the standard that the following document falls under.  Default is EPCglobal.', max_length=20, verbose_name='Standard')),
                ('type_version', models.CharField(default='1.0', help_text='Descriptor which contains versioning information or number of the standard that defines the documentwhich is specified in the ’Type’ data element, e.g. values could be ‘1.3’ or ‘D.96A’, etc.', max_length=10, verbose_name='Version')),
                ('instance_identifier', models.CharField(db_index=True, help_text='Descriptor which contains reference information which uniquely identifies this instance of the SBD between the sender and the receiver.', max_length=100, verbose_name='Instance Identifier')),
                ('document_type', models.CharField(choices=[('Events', 'Events'), ('MasterData', 'MasterData'), ('QueryControl-Request', 'QueryControl-Request'), ('QueryControl-Response', 'QueryControl-Response'), ('QueryCallback', 'QueryCallback'), ('Query', 'Query')], help_text='A logical indicator representing the type of Business Data being sent or the named type of business data.', max_length=25, verbose_name='Type')),
                ('multiple_type', models.NullBooleanField(default=False, help_text='A flag to indicate that there is more than one type of Document in the instance.', verbose_name='Multiple Type')),
                ('creation_date_and_time', models.CharField(help_text='Descriptor which contains date and time of SBDH/document creation.', max_length=35, null=True, verbose_name='Creation Date and Time')),
            ],
            options={
                'verbose_name': 'Document Identification',
                'verbose_name_plural': 'Document Identifications',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID', primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When this record was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='When this record was last modified.', verbose_name='Modified')),
                ('identifier', models.CharField(db_index=True, help_text='The primary unique id for the entry.', max_length=150, unique=True, verbose_name='EPC URN')),
                ('last_event_time', models.DateTimeField(help_text='The time of the event that last affected the status ofthis entry.', null=True, verbose_name='Last Event Time')),
                ('last_disposition', models.CharField(help_text='The business condition of the objects associated with the EPCs, presumed to hold true until contradicted by a subsequent event..', max_length=150, null=True, verbose_name='Last Disposition')),
                ('last_aggregation_event_time', models.DateTimeField(help_text='The time of the event that last affected the status ofthis entries hierarchical relation to other entries.', null=True, verbose_name='Last Aggregation Event Time')),
                ('last_aggregation_event_action', models.CharField(choices=[('ADD', 'Add'), ('OBSERVE', 'Observe'), ('DELETE', 'Delete')], help_text='The action (ADD or DELETE) of the last aggregation event that affected this entry.  Observation events are not noted.', max_length=10, null=True, verbose_name='Last Aggregation Action')),
                ('is_parent', models.BooleanField(default=False, help_text='True if this entry is a parent in any hierarchies. Falseif not.', verbose_name='Is Parent')),
                ('decommissioned', models.BooleanField(default=False, help_text='Whether or not the entry has been decommissioned.  Oncean entry is decommissioned, it can no longer take placein business processes.', verbose_name='Decommissioned')),
            ],
            options={
                'verbose_name': 'Entry',
                'verbose_name_plural': 'Entries',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='EntryEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('ag', 'Aggregation'), ('ob', 'Object'), ('tx', 'Transaction'), ('tf', 'Transformation')], help_text='The type of event (Aggregation, Object, Transaction or Transformation.', max_length=3, verbose_name='Event Type')),
                ('event_time', models.DateTimeField(db_index=True, help_text="The Event's eventTime.", verbose_name='Event Time')),
                ('identifier', models.CharField(db_index=True, help_text='A redundant entry ID entry for fast event composition.', max_length=150, verbose_name='EPC URN')),
                ('is_parent', models.BooleanField(default=False, help_text="Whether or not this entry was the parent of it's constituent event.", verbose_name='Is Event Parent')),
                ('output', models.BooleanField(default=False, help_text='Whether or not the entry was the output of a Transformation event.', verbose_name='Transformation Output')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When this record was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='When this record was last modified.', verbose_name='Modified')),
                ('entry', models.ForeignKey(help_text='The Unique ID of the Entry', on_delete=django.db.models.deletion.CASCADE, to='quartet_epcis.Entry', verbose_name='Entry ID')),
            ],
            options={
                'verbose_name': 'Entry Event Record',
                'verbose_name_plural': 'Entry Event Records',
            },
        ),
        migrations.CreateModel(
            name='ErrorDeclaration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('declaration_time', models.DateTimeField(default=django.utils.timezone.now, help_text='The time at which the error was declared.', verbose_name='Declaration Time')),
                ('reason', models.CharField(help_text='The reason for the error.', max_length=150, null=True, verbose_name='Reason')),
                ('corrective_event_ids', models.TextField(help_text='A delimited list of EPCIS event ids.', null=True, verbose_name='Corrective Event IDs')),
            ],
            options={
                'verbose_name': 'Error Declaration',
                'verbose_name_plural': 'Error Declarations',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID', primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When this record was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='When this record was last modified.', verbose_name='Modified')),
                ('event_time', models.DateTimeField(db_index=True, editable=False, help_text='The date and time at which the EPCIS Capturing Application asserts the event occurred.', verbose_name='Event Time')),
                ('event_timezone_offset', models.CharField(default='+00:00', help_text='The time zone offset in effect at the time and place the event occurred, expressed as an offset from UTC', max_length=6, null=True, verbose_name='Event Timezone Offset')),
                ('record_time', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time at which this event was recorded by an EPCIS Repository.', null=True, verbose_name='Record Time')),
                ('event_id', models.CharField(db_index=True, default=quartet_epcis.models.abstractmodels.haikunate, help_text='An identifier for this event as specified by the capturing application, globally unique across all events other than error declarations. Not to be confused with the unique id/primary key for events within a database.', max_length=150, null=True, verbose_name='Event ID')),
                ('action', models.CharField(choices=[('ADD', 'Add'), ('OBSERVE', 'Observe'), ('DELETE', 'Delete')], help_text='How this event relates to the lifecycle of the EPCs named in this event.', max_length=10, verbose_name='Action')),
                ('biz_step', models.CharField(help_text='The business step of which this event was a part.', max_length=150, null=True, verbose_name='Business Step')),
                ('disposition', models.CharField(help_text='The business condition of the objects associated with the EPCs, presumed to hold true until contradicted by a subsequent event..', max_length=150, null=True, verbose_name='Disposition')),
                ('read_point', models.CharField(help_text='The read point at which the event took place.', max_length=150, null=True, verbose_name='Read Point')),
                ('biz_location', models.CharField(help_text='The business location where the objects associated with the EPCs may be found, until contradicted by a subsequent event.', max_length=150, null=True, verbose_name='Business Location')),
                ('type', models.CharField(choices=[('ag', 'Aggregation'), ('ob', 'Object'), ('tx', 'Transaction'), ('tf', 'Transformation')], help_text='The type of event.', max_length=2, verbose_name='Event Type')),
                ('message_id', models.CharField(help_text='The unique id of the originating message.', max_length=100, verbose_name='Message ID')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['event_time'],
            },
        ),
        migrations.CreateModel(
            name='InstanceLotMasterData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the ILMD entry.', max_length=150, verbose_name='Name')),
                ('value', models.CharField(help_text='The value of the ILMD entry.', max_length=255, verbose_name='Value')),
                ('event', models.ForeignKey(help_text='The source event.', on_delete=django.db.models.deletion.CASCADE, to='quartet_epcis.Event', verbose_name='Event')),
            ],
            options={
                'verbose_name': 'ILMD Entry',
                'verbose_name_plural': 'ILMD Entries',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.CharField(default=quartet_epcis.models.headers.haikunate, help_text='The unique name of the job- autogenerated.', max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_type', models.CharField(choices=[('Sender', 'Sender'), ('Receiver', 'Receiver')], help_text='The type of partner.  Either Sender or Receiver.', max_length=20, verbose_name='Partner Type')),
                ('authority', models.CharField(default='SGLN', help_text='The identifying authority/format for the identification field. Default is SGLN.', max_length=20, null=True, verbose_name='authority')),
                ('identifier', models.CharField(help_text='An identifier that is in line with the authority specified in the authority field.  Typically an SGLN URN value.', max_length=100, null=True, verbose_name='Identifier')),
                ('contact', models.CharField(help_text='The contact/name info.', max_length=50, null=True, verbose_name='Contact')),
                ('email_address', models.EmailField(help_text='The email address for the partner.', max_length=100, null=True, verbose_name='Email Address')),
                ('fax_number', models.CharField(help_text='Fax number.', max_length=20, null=True, verbose_name='Fax Number')),
                ('telephone_number', models.CharField(help_text='Telephone number for the partner.', max_length=20, null=True, verbose_name='Telephone number.')),
                ('contact_type_identifier', models.CharField(help_text='The type of contact- for example, ', max_length=40, null=True, verbose_name='Role of the contact in this business process.')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
            },
        ),
        migrations.CreateModel(
            name='QuantityElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epc_class', models.CharField(help_text='The EPC class.', max_length=200, verbose_name='EPC Class')),
                ('quantity', models.FloatField(help_text='The Quantity value.', verbose_name='Quantity')),
                ('uom', models.CharField(help_text='The unit of measure relative to the quantity.', max_length=150, null=True, verbose_name='Unit of Measure (UOM)')),
                ('is_output', models.BooleanField(default=False, help_text='True if this quantity element was provided as the output as part of a transformation event.', verbose_name='Is Output')),
                ('event', models.ForeignKey(help_text='The source event.', on_delete=django.db.models.deletion.CASCADE, to='quartet_epcis.Event', verbose_name='Event')),
            ],
            options={
                'verbose_name': 'Quantity Element',
                'verbose_name_plural': 'Quantity Elements',
            },
        ),
        migrations.CreateModel(
            name='SBDH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_version', models.CharField(default='1.0', help_text='Descriptor which contains version information for the SBDH.  Default is 1.0', max_length=10, verbose_name='Header Version')),
                ('document_identification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quartet_epcis.DocumentIdentification')),
                ('message', models.ForeignKey(help_text='The message this header was associated with.', on_delete=django.db.models.deletion.CASCADE, to='quartet_epcis.Message', verbose_name='Message')),
            ],
            options={
                'verbose_name': 'SBDH',
                'verbose_name_plural': 'SBDHs',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID', primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When this record was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='When this record was last modified.', verbose_name='Modified')),
                ('type', models.CharField(help_text='The source type.', max_length=150, verbose_name='Type')),
                ('source', models.CharField(help_text='The source identifier.', max_length=150, verbose_name='Source')),
            ],
            options={
                'verbose_name': 'Source',
                'verbose_name_plural': 'Sources',
            },
        ),
        migrations.CreateModel(
            name='SourceEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(help_text='The event within which the source was reported.', on_delete=django.db.models.deletion.CASCADE, to='quartet_epcis.Event', verbose_name='Event')),
                ('source', models.ForeignKey(help_text='A source within the event.', on_delete=django.db.models.deletion.CASCADE, to='quartet_epcis.Source', verbose_name='Source')),
            ],
        ),
        migrations.CreateModel(
            name='TransformationID',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID', primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When this record was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='When this record was last modified.', verbose_name='Modified')),
                ('identifier', models.CharField(help_text='The Transformation event ID.', max_length=150, verbose_name='TransformationID')),
                ('event', models.ForeignKey(help_text='The source event.', on_delete=django.db.models.deletion.CASCADE, to='quartet_epcis.Event', verbose_name='Event')),
            ],
            options={
                'verbose_name': 'Transformation ID',
                'verbose_name_plural': 'Transformation IDs',
            },
        ),
        migrations.AddField(
            model_name='partner',
            name='header',
            field=models.ForeignKey(help_text='The related SBDH.', on_delete=django.db.models.deletion.CASCADE, to='quartet_epcis.SBDH', verbose_name='SBDH'),
        ),
        migrations.AddField(
            model_name='errordeclaration',
            name='event',
            field=models.ForeignKey(help_text='The source event.', on_delete=django.db.models.deletion.CASCADE, to='quartet_epcis.Event', verbose_name='Event'),
        ),
        migrations.AddField(
            model_name='entryevent',
            name='event',
            field=models.ForeignKey(help_text='The UUID of the event.', on_delete=django.db.models.deletion.CASCADE, to='quartet_epcis.Event', verbose_name='Event ID'),
        ),
        migrations.AddField(
            model_name='entry',
            name='last_aggregation_event',
            field=models.ForeignKey(help_text='Used mostly for internal tracking and performance duringparsing.  This tracks the last aggregation event thataffected the entry.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_agg_event', to='quartet_epcis.Event', verbose_name='Last Aggregation Event'),
        ),
        migrations.AddField(
            model_name='entry',
            name='last_event',
            field=models.ForeignKey(help_text='The last event to affect the status of this entry.', null=True, on_delete=django.db.models.deletion.PROTECT, to='quartet_epcis.Event', verbose_name='Last Event'),
        ),
        migrations.AddField(
            model_name='entry',
            name='parent_id',
            field=models.ForeignKey(help_text='The parent of this identifier (if any).', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_identifier', to='quartet_epcis.Entry', verbose_name='Parent ID'),
        ),
        migrations.AddField(
            model_name='entry',
            name='top_id',
            field=models.ForeignKey(help_text='The top level id (if any).', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='top_identifier', to='quartet_epcis.Entry', verbose_name='Top ID'),
        ),
        migrations.AddField(
            model_name='destinationevent',
            name='event',
            field=models.ForeignKey(help_text='The event within which the destination was reported.', on_delete=django.db.models.deletion.CASCADE, to='quartet_epcis.Event', verbose_name='Event'),
        ),
        migrations.AddField(
            model_name='businesstransaction',
            name='event',
            field=models.ForeignKey(help_text='The source event.', on_delete=django.db.models.deletion.CASCADE, to='quartet_epcis.Event', verbose_name='Event'),
        ),
        migrations.AlterIndexTogether(
            name='entryevent',
            index_together={('event', 'entry')},
        ),
    ]
