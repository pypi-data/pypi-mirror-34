from verkhovna_rada_ukr_pl.rada_factories import UkraineRadaFactory, PolandRadaFactory

simulation_config_file = {'rada': 'Poland'}


def main():
    if simulation_config_file['rada'] == 'Ukraine':
        UkraineRadaFactory()().run()
    else:
        PolandRadaFactory()().run()


if __name__ == "__main__":
    main()
