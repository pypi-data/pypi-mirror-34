from django.core.management.base import BaseCommand
from election.models import Race
from geography.models import DivisionLevel
from raceratings.views import Home, RacePage
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Publishes our race pages'

    def bake_home_page(self):
        view = Home()
        view.publish_statics()
        view.publish_serialized_data()
        view.publish_template()

    def bake_race_pages(self, races):
        stub = RacePage()
        stub.publish_statics()

        for race in tqdm(races):
            if race.office.division.level.name == DivisionLevel.DISTRICT:
                division = race.office.division.parent.slug
                code = race.office.division.code
            else:
                division = race.office.division.slug
                code = None

            if race.special:
                code = 'special'

            if 'governor' in race.office.slug:
                body = 'governor'
            else:
                body = race.office.body.slug

            self.stdout.write('> {}'.format(race.office.label))
            kwargs = {
                'division': division,
                'body': body,
                'code': code
            }

            view = RacePage(**kwargs)
            view.publish_serialized_data()
            view.publish_template(**kwargs)

    def handle(self, *args, **kwargs):
        self.bake_home_page()

        races = Race.objects.filter(cycle__slug='2018').order_by(
            'office__division__label', 'office__label'
        )

        self.bake_race_pages(races)
