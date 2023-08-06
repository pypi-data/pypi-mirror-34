import os
from optparse import make_option

from django.core.management.base import BaseCommand
from django.utils import timezone

from devilry.devilry_dumpv2database import modeldumpers


class TimeExecution(object):
    def __init__(self, label, command):
        self.start_time = None
        self.label = label
        self.command = command

    def __enter__(self):
        self.start_time = timezone.now()

    def __exit__(self, ttype, value, traceback):
        end_time = timezone.now()
        duration_minutes = (end_time - self.start_time).total_seconds() / 60.0
        self.command.stdout.write('{}: {}min'.format(self.label, duration_minutes))
        self.command.stdout.write('')


class Command(BaseCommand):
    args = '<output-directory>'
    help = 'Dump the entire database to a directory of json files.'

    option_list = BaseCommand.option_list + (
        make_option('--fake',
                    dest='fake', action='store_true',
                    default=False,
                    help='Print the serialized objects and filepaths, do not write them.'),
    )

    def __abort_if_output_directory_exists(self):
        if self.fake:
            return

        if os.path.exists(self.output_directory):
            self.stderr.write('The output directory, {}, already exists. Aborting.'.format(
                self.output_directory
            ))
            raise SystemExit()

    def handle(self, *args, **kwargs):
        if len(args) < 1:
            self.stderr.write('<output-directory> is required. See --help.')
            raise SystemExit()
        self.output_directory = args[0]
        self.fake = kwargs['fake']
        self.__abort_if_output_directory_exists()
        self.__run()

    def __get_dumper_classes(self):
        return [
            modeldumpers.UserDumper,
            modeldumpers.NodeDumper,
            modeldumpers.SubjectDumper,
            modeldumpers.PeriodDumper,
            modeldumpers.AssignmentDumper,
            modeldumpers.PointToGradeMapDumper,
            modeldumpers.PointRangeToGradeDumper,
            modeldumpers.AssignmentGroupDumper,
            modeldumpers.DeadlineDumper,
            modeldumpers.RelatedExaminerDumper,
            modeldumpers.RelatedStudentDumper,
            modeldumpers.ExaminerDumper,
            modeldumpers.CandidateDumper,
            modeldumpers.DeliveryDumper,
            modeldumpers.StaticFeedbackDumper,
            modeldumpers.FileMetaDumper,
            modeldumpers.QualifiesForExamStatusDumper,
            modeldumpers.QualifiesForFinalExamDumper
        ]

    def __run(self):
        dumper_classes = self.__get_dumper_classes()
        for index, dumper_class in enumerate(dumper_classes, start=1):
            with TimeExecution(dumper_class.__name__, self):
                dumper = dumper_class(output_root=self.output_directory)
                self.stdout.write('Dumping model {index}/{count} {model!r} - {object_count} objects'.format(
                    index=index,
                    count=len(dumper_classes),
                    model=dumper.prettyformat_model_name(),
                    object_count=dumper.get_object_count()))
                dumper.serialize_all_objects_to_output_directory(fake=self.fake)
